# models/timetable.py
from models.classes import get_classes
from models.trainers import get_trainers
from utils.conflict_checker import is_conflict

def generate_timetable():
    """Generate the timetable by matching classes to trainers"""
    classes = get_classes()
    trainers = get_trainers()
    timetable = []

    for cls in classes:
        for trainer in trainers:
            # Assume trainers are available all the time for simplicity
            # Add logic to check availability and time slots
            if not is_conflict(timetable, trainer["name"], cls["name"]):
                timetable.append({
                    "class": cls["name"],
                    "trainer": trainer["name"],
                    "time": "9:00 AM - 10:00 AM",  # Placeholder time slot
                    "venue": "Room 101"          # Placeholder venue
                })
                break

    return timetable
