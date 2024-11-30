# utils/conflict_checker.py
def is_conflict(timetable, trainer, class_name):
    """Check if there is a conflict with the timetable"""
    for slot in timetable:
        if slot["trainer"] == trainer or slot["class"] == class_name:
            return True
    return False
