# main.py
from models.classes import add_class
from models.trainors import add_trainer
from models.timetable import generate_timetable
from utils.printer import print_timetable

def main():
    """Main program to manage timetable generation"""
    print("Welcome to the Timetable Generator!")
    while True:
        print("\nMenu:")
        print("1. Add Class")
        print("2. Add Trainer")
        print("3. Generate Timetable")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter class name: ")
            size = int(input("Enter class size: "))
            add_class(name, size)
        elif choice == "2":
            name = input("Enter trainer name: ")
            availability = input("Enter availability (e.g., Mon-Fri 9AM-5PM): ")
            add_trainer(name, availability)
        elif choice == "3":
            timetable = generate_timetable()
            print_timetable(timetable)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
