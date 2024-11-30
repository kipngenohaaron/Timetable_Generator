# tests/test_timetable.py

# Import necessary modules from the project
from models.classes import Class
from models.trainers import Trainer
from models.subjects import Subject
from timetable import generate_timetable
from utils.conflict_checker import is_conflict

# Sample data for tests
def test_add_class():
    """Test for adding a class."""
    class1 = Class(name="Math 101", schedule="Mon 9-11")
    assert class1.name == "Math 101", f"Expected 'Math 101', but got {class1.name}"
    assert class1.schedule == "Mon 9-11", f"Expected 'Mon 9-11', but got {class1.schedule}"

def test_add_trainer():
    """Test for adding a trainer."""
    trainer = Trainer(name="John Doe", subject="Math")
    assert trainer.name == "John Doe", f"Expected 'John Doe', but got {trainer.name}"
    assert trainer.subject == "Math", f"Expected 'Math', but got {trainer.subject}"

def test_add_subject():
    """Test for adding a subject."""
    subject = Subject(name="Mathematics", code="MATH101")
    assert subject.name == "Mathematics", f"Expected 'Mathematics', but got {subject.name}"
    assert subject.code == "MATH101", f"Expected 'MATH101', but got {subject.code}"

def test_generate_timetable():
    """Test for generating timetable."""
    # Assuming that generate_timetable returns a list of dictionaries
    timetable = generate_timetable()
    
    # Example checks
    assert len(timetable) > 0, "Timetable is empty, expected some entries"
    
    # Check the first entry
    assert "class" in timetable[0], "Class field missing in timetable"
    assert "trainer" in timetable[0], "Trainer field missing in timetable"
    assert "time" in timetable[0], "Time field missing in timetable"
    assert "venue" in timetable[0], "Venue field missing in timetable"
    
    # Check that the class "Math 101" is in the timetable
    class_names = [slot["class"] for slot in timetable]
    assert "Math 101" in class_names, "Math 101 not found in timetable"

def test_conflict_checker_no_conflict():
    """Test conflict checking: No conflict should return False"""
    # Create two classes with no overlapping schedules
    class1 = Class(name="Math 101", schedule="Mon 9-11")
    class2 = Class(name="Science 101", schedule="Mon 11-1")
    
    conflict = is_conflict(class1, class2)
    assert conflict is False, "Expected no conflict, but got a conflict"

def test_conflict_checker_with_conflict():
    """Test conflict checking: Should return True for overlapping schedules"""
    # Create two classes with overlapping schedules
    class1 = Class(name="Math 101", schedule="Mon 9-11")
    class2 = Class(name="History 101", schedule="Mon 10-12")
    
    conflict = is_conflict(class1, class2)
    assert conflict is True, "Expected a conflict, but got no conflict"
