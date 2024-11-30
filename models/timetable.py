class Timetable:
    def __init__(self):
        self.classes = []  # List of all classes
        self.trainings = {}  # Dictionary mapping class -> list of (trainer, subject)
    
    def add_class(self, class_obj):
        self.classes.append(class_obj)
    
    def assign_trainer(self, class_obj, trainer, subject, time_slot):
        # Conflict check logic for trainers
        for assigned_class, assignments in self.trainings.items():
            for assigned_trainer, _ in assignments:
                if assigned_trainer == trainer:
                    if assigned_class == class_obj:  # Check if already assigned
                        raise ValueError(f"Trainer {trainer.name} is already assigned to {class_obj.name}")
        
        # Add trainer to class's timetable
        if class_obj not in self.trainings:
            self.trainings[class_obj] = []
        self.trainings[class_obj].append((trainer, subject))

    def print_timetable(self):
        print("Institution Timetable:")
        for class_obj in self.classes:
            print(f"\nClass: {class_obj.name}, Code: {class_obj.code}, Duration: {class_obj.duration}, Venue: {class_obj.venue}")
            if class_obj in self.trainings:
                for trainer, subject in self.trainings[class_obj]:
                    print(f"  - Trainer: {trainer.name}, Subject: {subject.name}")

    def print_trainer_timetable(self, trainer):
        print(f"\nTimetable for Trainer: {trainer.name}")
        for class_obj, assignments in self.trainings.items():
            for assigned_trainer, subject in assignments:
                if assigned_trainer == trainer:
                    print(f"  - Class: {class_obj.name}, Subject: {subject.name}, Venue: {class_obj.venue}, Duration: {class_obj.duration}")
