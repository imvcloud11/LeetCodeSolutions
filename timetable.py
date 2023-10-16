# Define a daily timetable using a dictionary
timetable = {
    "Monday": ["Math", "Science", "History", "Lunch", "English"],
    "Tuesday": ["Science", "Math", "Physical Education", "Lunch", "Art"],
    "Wednesday": ["History", "Math", "Science", "Lunch", "Music"],
    "Thursday": ["English", "Math", "Geography", "Lunch", "Science"],
    "Friday": ["Science", "Math", "Art", "Lunch", "Physical Education"]
}

# Function to display the timetable
def display_timetable():
    for day, subjects in timetable.items():
        print(f"{day}:")
        for period, subject in enumerate(subjects, start=1):
            print(f"  Period {period}: {subject}")
        print()

# Display the timetable
display_timetable()
