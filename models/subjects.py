class Subject:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def __repr__(self):
        return f"Subject(name={self.name}, code={self.code})"
