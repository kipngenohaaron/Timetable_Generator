# utils/printer.py

def print_timetable(timetable):
    """Print the generated timetable"""
    
    # Print for each class
    print("\n--- Timetable for Classes ---")
    classes = set([slot["class"] for slot in timetable])  # Unique classes
    for class_name in classes:
        print(f"\nClass: {class_name}")
        class_slots = [slot for slot in timetable if slot["class"] == class_name]
        for slot in class_slots:
            print(f"  Trainer: {slot['trainer']} | Time: {slot['time']} | Venue: {slot['venue']}")
    
    # Print for each trainer
    print("\n--- Timetable for Trainers ---")
    trainers = set([slot["trainer"] for slot in timetable])  # Unique trainers
    for trainer_name in trainers:
        print(f"\nTrainer: {trainer_name}")
        trainer_slots = [slot for slot in timetable if slot["trainer"] == trainer_name]
        for slot in trainer_slots:
            print(f"  Class: {slot['class']} | Time: {slot['time']} | Venue: {slot['venue']}")
