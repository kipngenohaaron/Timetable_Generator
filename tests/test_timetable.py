import pytest
from models.classes import Class
from models.trainers import Trainer
from models.subjects import Subject
from models.timetable import Timetable
from utils.conflict_checker import check_conflicts

# Test data setup
@pytest.fixture
def test_data():
    # Creating mock data for classes, trainers, and subjects
    trainer1 = Trainer(name="John Doe", subject="Mathematics")
    trainer2 = Trainer(name="Jane Smith", subject="Science")
    
    subject1 = Subject(name="Mathematics", duration=60)
    subject2 = Subject(name="Science", duration=60)

    class1 = Class(name="Class 1", subjects=[subject1], trainer=trainer1, venue="Room 101", duration=60)
    class2 = Class(name="Class 2", subjects=[subject2], trainer=trainer2, venue="Room 102", duration=60)
    
    timetable = Timetable(classes=[class1, class2])
    
    return {
        'trainer1': trainer1,
        'trainer2': trainer2,
        'subject1': subject1,
        'subject2': subject2,
        'class1': class1,
        'class2': class2,
        'timetable': timetable
    }

# Test timetable generation for each class
def test_timetable_for_class(test_data):
    timetable = test_data['timetable']
    class1 = test_data['class1']
    class2 = test_data['class2']

    # Check if the classes are added to the timetable
    assert class1 in timetable.classes
    assert class2 in timetable.classes

# Test timetable generation for each trainer
def test_timetable_for_trainer(test_data):
    timetable = test_data['timetable']
    trainer1 = test_data['trainer1']
    trainer2 = test_data['trainer2']
    
    # Check if the trainer is assigned to the correct class
    assert trainer1 in [class_obj.trainer for class_obj in timetable.classes if class_obj.trainer == trainer1]
    assert trainer2 in [class_obj.trainer for class_obj in timetable.classes if class_obj.trainer == trainer2]

# Test for conflicts in the timetable (venue conflicts or trainer conflicts)
def test_timetable_conflicts(test_data):
    timetable = test_data['timetable']
    
    # Create a conflict scenario (same venue, same time)
    class3 = Class(name="Class 3", subjects=[test_data['subject1']], trainer=test_data['trainer1'], venue="Room 101", duration=60)
    timetable.add_class(class3)  # Adding a class with the same venue as class1
    
    # Test conflict detection for the same venue
    conflict_found = check_conflicts(timetable)
    assert conflict_found is True, "Conflict should be found due to same venue"
    
    # Adding a different trainer to the same venue
    class4 = Class(name="Class 4", subjects=[test_data['subject2']], trainer=test_data['trainer2'], venue="Room 101", duration=60)
    timetable.add_class(class4)
    
    conflict_found = check_conflicts(timetable)
    assert conflict_found is True, "Conflict should be found due to same venue"

# Test printing of the timetable
def test_print_timetable(test_data):
    timetable = test_data['timetable']
    
    # Test if the printing function works
    # (This assumes `print_timetable` method exists and prints timetable)
    printed_timetable = timetable.print_timetable()
    assert "Class 1" in printed_timetable
    assert "Class 2" in printed_timetable
    assert "Room 101" in printed_timetable
