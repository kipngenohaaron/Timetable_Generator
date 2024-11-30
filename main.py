from models.timetable import Timetable  
from utils.printer import print_timetable  
from utils.conflict_checker import check_conflicts  

def main():  
    # Create a Timetable instance  
    timetable = Timetable()  
    
    # Load data (this can be done from data JSON files)  
    timetable.load_data()  

    # Check for conflicts before generating  
    if check_conflicts(timetable):  
        print("Conflicts detected! Please resolve them.")  
    else:  
        # Generate the timetable  
        timetable.generate()  
        print_timetable(timetable)  

if __name__ == "__main__":  
    main()