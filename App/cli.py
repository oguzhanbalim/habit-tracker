# cli.py
import sys
from habit_tracker import HabitTracker
from utils import get_user_input, load_predefined_habits

def main():
    habit_tracker = HabitTracker()

    # Load predefined habits
    load_predefined_habits(habit_tracker)

    while True:
        print("\nHabit Tracker")
        print("1. Add a new habit")
        print("2. Delete a habit")
        print("3. Check off a habit")
        print("4. View all habits")
        print("5. View habits by periodicity")
        print("6. View longest streak for a habit")
        print("7. View the habit you struggled with last month")
        print("8. Save habits to file")
        print("9. Load habits from file")
        print("10. Exit")
        
        choice = get_user_input("Choose an option: ", [str(i) for i in range(1, 11)])
        
        if choice == "1":
            name = input("Enter habit name: ")
            periodicity = int(input("Enter periodicity (in days): "))
            habit_tracker.add_habit(name, periodicity)
            print(f"Habit '{name}' added.")
        
        elif choice == "2":
            name = input("Enter habit name to delete: ")
            habit_tracker.delete_habit(name)
            print(f"Habit '{name}' deleted.")
        
        elif choice == "3":
            name = input("Enter habit name to check off: ")
            habit_tracker.checkoff_habit(name)
            print(f"Habit '{name}' checked off.")
        
        elif choice == "4":
            habits = habit_tracker.get_all_habits()
            for habit in habits:
                print(f"Habit: {habit.name}, Periodicity: {habit.periodicity} days, Current Streak: {habit.current_streak()}")

        elif choice == "5":
            periodicity = int(input("Enter periodicity (in days): "))
            habits = habit_tracker.get_habits_by_periodicity(periodicity)
            for habit in habits:
                print(f"Habit: {habit.name}, Current Streak: {habit.current_streak()}")

        elif choice == "6":
            name = input("Enter habit name: ")
            streak = habit_tracker.longest_streak_for_habit(name)
            print(f"Longest streak for '{name}' is {streak} days.")
        
        elif choice == "7":
            struggled_habits = habit_tracker.habits_struggled_last_month()
            print("Habits struggled with last month:")
            for habit_name in struggled_habits:
                print(f"- {habit_name}")
        
        elif choice == "8":
            filename = input("Enter filename to save (default is 'habits.json'): ") or "habits.json"
            habit_tracker.save_to_file(filename)
            print(f"Habits saved to {filename}.")
        
        elif choice == "9":
            filename = input("Enter filename to load (default is 'habits.json'): ") or "habits.json"
            habit_tracker.load_from_file(filename)
            print(f"Habits loaded from {filename}.")
        
        elif choice == "10":
            print("Goodbye!")
            sys.exit()

if __name__ == "__main__":
    main()

