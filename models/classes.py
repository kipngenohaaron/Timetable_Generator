# class Class:
#     def __init__(self, name, code, duration=None, venue=None):
#         self.name = name
#         self.code = code
#         self.duration = duration  # Duration of the class
#         self.venue = venue        # Venue of the class

#     def __repr__(self):
#         return f"Class(name={self.name}, code={self.code}, duration={self.duration}, venue={self.venue})"
class Class:
    def __init__(self, name, subjects, trainer, venue, duration):
        self.name = name
        self.subjects = subjects
        self.trainer = trainer
        self.venue = venue
        self.duration = duration
