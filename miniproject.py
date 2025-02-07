class Workout:
    def __init__(self, date, type, duration, calories):
        self.date = date
        self.type = type
        self.duration = duration
        self.calories = calories

    def to_string(self):
        return f"{self.date},{self.type},{self.duration},{self.calories}"

    @staticmethod
    def from_string(workout_str):
        date, type, duration, calories = workout_str.strip().split(',')
        return Workout(date, type, duration, calories)

class FitnessTracker:
    def __init__(self):
        self.workouts = []

    def add_workout(self, workout):
        self.workouts.append(workout)

    def view_progress(self):
        for workout in self.workouts:
            print(f"Date: {workout.date}, Type: {workout.type}, Duration: {workout.duration} mins, Calories: {workout.calories}")

    def save_data(self, filename):
        with open(filename, 'w') as file:
            for workout in self.workouts:
                file.write(workout.to_string() + '\n')

    def load_data(self, filename):
        with open(filename, 'r') as file:
            self.workouts = [Workout.from_string(line) for line in file]

def main():
    tracker = FitnessTracker()
    
    while True:
        print("\n1. Add Workout")
        print("2. View Progress")
        print("3. Save Data")
        print("4. Load Data")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            type = input("Enter workout type: ")
            duration = input("Enter duration (in minutes): ")
            calories = input("Enter calories burned: ")
            workout = Workout(date, type, duration, calories)
            tracker.add_workout(workout)
        elif choice == '2':
            tracker.view_progress()
        elif choice == '3':
            filename = input("Enter filename to save data: ")
            tracker.save_data(filename)
        elif choice == '4':
            filename = input("Enter filename to load data: ")
            tracker.load_data(filename)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
