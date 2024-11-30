# models/trainers.py
import json

DATA_FILE = "data/trainers.json"

def get_trainers():
    """Retrieve all trainers"""
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def add_trainer(name, availability):
    """Add a trainer"""
    trainers = get_trainers()
    trainers.append({"name": name, "availability": availability})
    with open(DATA_FILE, "w") as file:
        json.dump(trainers, file)

def get_trainer_by_name(name):
    """Retrieve trainer by name"""
    return next((trainer for trainer in get_trainers() if trainer["name"] == name), None)
