# models/subjects.py
import json

DATA_FILE = "data/subjects.json"

def get_subjects():
    """Retrieve all subjects"""
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def add_subject(name, code):
    """Add a subject"""
    subjects = get_subjects()
    subjects.append({"name": name, "code": code})
    with open(DATA_FILE, "w") as file:
        json.dump(subjects, file)

def get_subject_by_code(code):
    """Retrieve subject by code"""
    return next((subj for subj in get_subjects() if subj["code"] == code), None)
