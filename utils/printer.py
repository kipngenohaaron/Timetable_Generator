# utils/printer.py
def print_timetable(timetable):
    """Print the generated timetable"""
    print("\nGenerated Timetable:")
    for slot in timetable:
        print(f"Class: {slot['class']} | Trainer: {slot['trainer']} | Time: {slot['time']} | Venue: {slot['venue']}")
