import pytest
from models.classes import Class
from models.trainers import Trainer
from models.subjects import Subject
from models.timetable import Timetable

def test_trainer_timetable():
    timetable = Timetable()

    # Create trainers
    trainer1 = Trainer("Mr. Smith", "T001")
    trainer2 = Trainer("Ms. Johnson", "T002")

    # Create subjects
    subject1 = Subject("Mathematics", "MATH101")
    subject2 = Subject("Physics", "PHYS101")

    # Create classes with duration and venue
    class1 = Class("Math 101", "M101", "1 hour", "Room 101")
    class2 = Class("Physics 101", "P101", "2 hours", "Room 102")

    # Add classes to timetable
    timetable.add_class(class1)
    timetable.add_class(class2)

    # Assign trainers to classes
    timetable.assign_trainer(class1, trainer1, subject1, "9:00 AM")
    timetable.assign_trainer(class2, trainer2, subject2, "11:00 AM")

    # Print timetables for trainers
    timetable.print_trainer_timetable(trainer1)
    timetable.print_trainer_timetable(trainer2)

    # Print timetable for classes
    timetable.print_timetable()

def test_conflict_check():
    timetable = Timetable()

    # Create trainers and classes
    trainer1 = Trainer("Mr. Smith", "T001")
    trainer2 = Trainer("Ms. Johnson", "T002")
    subject1 = Subject("Math", "MATH101")
    class1 = Class("Math 101", "M101", "1 hour", "Room 101")
    
    # Add class to timetable
    timetable.add_class(class1)

    # Assign trainer1 to class1
    timetable.assign_trainer(class1, trainer1, subject1, "9:00 AM")

    # Attempt to assign trainer1 to the same class at the same time (should raise error)
    with pytest.raises(ValueError):
        timetable.assign_trainer(class1, trainer1, subject1, "9:00 AM")
