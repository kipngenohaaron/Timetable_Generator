# def check_for_conflicts(timetable, class_obj, trainer, time_slot):
#     # Check for trainer conflict with time and class
#     for assigned_class, assignments in timetable.trainings.items():
#         for assigned_trainer, _ in assignments:
#             if assigned_trainer == trainer:
#                 if assigned_class == class_obj:  # Check for the same class
#                     raise ValueError(f"Trainer {trainer.name} is already assigned to {class_obj.name}")
#     return False
def check_conflicts(timetable):
    venue_dict = {}
    trainer_dict = {}
    for class_obj in timetable.classes:
        # Check for venue conflict
        if class_obj.venue in venue_dict:
            return True  # Conflict detected (same venue)
        venue_dict[class_obj.venue] = class_obj

        # Check for trainer conflict
        if class_obj.trainer.name in trainer_dict:
            return True  # Conflict detected (same trainer)
        trainer_dict[class_obj.trainer.name] = class_obj
    
    return False  # No conflicts
