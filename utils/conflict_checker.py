def check_for_conflicts(timetable, class_obj, trainer, time_slot):
    # Check for trainer conflict with time and class
    for assigned_class, assignments in timetable.trainings.items():
        for assigned_trainer, _ in assignments:
            if assigned_trainer == trainer:
                if assigned_class == class_obj:  # Check for the same class
                    raise ValueError(f"Trainer {trainer.name} is already assigned to {class_obj.name}")
    return False
