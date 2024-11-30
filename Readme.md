
# Timetable Generator

## Author: **Kipngenoh Aaron Rotich**  
📱 **Contact**: 0724828197 | 0724279400  
📧 **Email**: [kipngenoahaaron@gmail.com](mailto:kipngenoahaaron@gmail.com)  
🔗 **GitHub**: [https://github.com/kipngenohaaron](https://github.com/kipngenohaaron)

---

## Project Description

This **Timetable Generator** is a Python-based application designed to automate the creation of class schedules for an educational institution. It allows for the management of trainers, classes, and subjects, and can generate conflict-free timetables for both trainers and classes.

### Key Features:
- **Add Classes**: Add new classes with their size.
- **Add Trainers**: Add trainers along with their availability.
- **Generate Timetable**: Automatically generates timetables for classes and trainers while avoiding conflicts.
- **Print Timetable**: Outputs the generated timetable in a clear format.

## Requirements

- Python 3.x
- Flask (for web functionality, optional)
- Pandas (for data manipulation, optional)
- OpenPyXL (for Excel export, optional)
- pytest (for unit testing, optional)

## Installation

### 1. Clone the repository:
```bash
git clone https://github.com/kipngenohaaron/Timetable_Generator.git
cd Timetable_Generator
```

### 2. Install dependencies:
#### Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # For Linux/macOS
```

#### Install required packages:
```bash
pip install -r requirements.txt
```

### 3. Run the program:
```bash
python3 main.py
```

The program will prompt you to add classes, trainers, and then generate timetables. It will output the results in the console.

## File Structure

```
timetable_generator/
├── main.py                 # Entry point for the application
├── models/                 # Contains the core logic for handling data
│   ├── classes.py          # Class data management
│   ├── trainers.py         # Trainer data management
│   ├── subjects.py         # Subject data management
│   └── timetable.py        # Timetable generation logic
├── utils/                  # Utility files for timetable printing and conflict checking
│   ├── conflict_checker.py # Conflict resolution logic
│   └── printer.py          # Printing timetable in a readable format
├── data/                   # Stores data for classes, trainers, and subjects
│   ├── classes.json        # Class data (initially empty)
│   ├── trainers.json       # Trainer data (initially empty)
│   ├── subjects.json       # Subject data (initially empty)
│   └── timetable.json      # Generated timetable (initially empty)
├── tests/                  # Unit tests for timetable generation
│   ├── test_timetable.py   # Unit tests for timetable generation
└── requirements.txt        # List of required packages
```

## Usage

After running the program, follow the interactive prompts to:

1. **Add a Class**: Enter the class name and size.
2. **Add a Trainer**: Enter the trainer's name and availability.
3. **Generate a Timetable**: The system will generate a conflict-free timetable for all classes and trainers.
4. **Exit**: End the program.

## Example Output

When the timetable is generated, you will see output like this:

```
Generated Timetable:
Class: Math 101 | Trainer: John Doe | Time: 9:00 AM - 10:00 AM | Venue: Room 101
Class: Science 201 | Trainer: Jane Smith | Time: 10:00 AM - 11:00 AM | Venue: Room 102
...
```

## Testing

To run unit tests for the timetable generation logic:

```bash
pytest tests/test_timetable.py
```

---

## Contributing

Feel free to fork the project, submit issues, and create pull requests.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- Special thanks to my mentors and peers for their feedback and support throughout the project.
```
