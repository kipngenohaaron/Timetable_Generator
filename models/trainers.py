class Trainer:
    def __init__(self, name, trainer_id):
        self.name = name
        self.trainer_id = trainer_id

    def __repr__(self):
        return f"Trainer(name={self.name}, trainer_id={self.trainer_id})"
