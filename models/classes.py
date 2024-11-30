# models/classes.py
import json

DATA_FILE = "data/classes.json"

def get_classes():
    """Retrieve all classes"""
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def add_class(name, size):
    """Add a class"""
    classes = get_classes()
    classes.append({"name": name, "size": size})
    with open(DATA_FILE, "w") as file:
        json.dump(classes, file)

def get_class_by_name(name):
    """Retrieve class by name"""
    return next((cls for cls in get_classes() if cls["name"] == name), None)
