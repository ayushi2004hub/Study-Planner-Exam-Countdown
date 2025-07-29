# study_planner_project/main.py
from countdown import countdown_days
from tracker import add_exam, add_study_topic, mark_topic_complete, view_progress
import json

DATA_FILE = 'planner_data.json'

def load_data():
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("Error: planner_data.json is not properly formatted.")
        return {}

def save_data(data):
    try:
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print("Error saving data:", e)

def main():
    while True:
        print("\n------ Study Planner ------")
        print("1. Add new exam")
        print("2. Add study topic")
        print("3. Mark topic as complete")
        print("4. View exam countdown")
        print("5. View progress report")
        print("6. Exit")

        try:
            choice = input("Enter your choice: ").strip()
            data = load_data()

            if choice == '1':
                add_exam(data)
            elif choice == '2':
                add_study_topic(data)
            elif choice == '3':
                mark_topic_complete(data)
            elif choice == '4':
                subject = input("Enter subject name: ").strip()
                if subject:
                    countdown_days(data, subject)
                else:
                    print("Subject name cannot be empty.")
            elif choice == '5':
                view_progress(data)
            elif choice == '6':
                print("Exiting... Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 6.")

            save_data(data)

        except Exception as e:
            print("An error occurred:", e)

if __name__ == "__main__":
    main()
