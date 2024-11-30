def print_timetable_for_class(timetable):
    print("Institution Timetable:")
    for class_obj in timetable.classes:
        print(f"\nClass: {class_obj.name}, Code: {class_obj.code}, Duration: {class_obj.duration}, Venue: {class_obj.venue}")
        if class_obj in timetable.trainings:
            for trainer, subject in timetable.trainings[class_obj]:
                print(f"  - Trainer: {trainer.name}, Subject: {subject.name}")

def print_timetable_for_trainer(timetable, trainer):
    print(f"\nTimetable for Trainer: {trainer.name}")
    for class_obj, assignments in timetable.trainings.items():
        for assigned_trainer, subject in assignments:
            if assigned_trainer == trainer:
                print(f"  - Class: {class_obj.name}, Subject: {subject.name}, Venue: {class_obj.venue}, Duration: {class_obj.duration}")
