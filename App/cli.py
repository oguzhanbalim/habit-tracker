# cli.py
import sys
from habit_tracker import HabitTracker
from utils import get_user_input, load_predefined_habits

def main():
    habit_tracker = HabitTracker()

    # Greet the user and ask for their name
    user_name = input("Welcome to Habit Tracker! What's your name? ").strip().title()
    print(f"Hello, {user_name}! Let's get started with tracking your habits.")

    # Load predefined habits
    load_predefined_habits(habit_tracker)

    while True:
        print(f"\n{user_name}, here are your options:")
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
            name = input(f"{user_name}, enter the habit name: ")
            periodicity = int(input("Enter the periodicity (in days): "))
            habit_tracker.add_habit(name, periodicity)
            print(f"Habit '{name}' added.")
        
        elif choice == "2":
            name = input(f"{user_name}, enter the habit name to delete: ")
            habit_tracker.delete_habit(name)
            print(f"Habit '{name}' deleted.")
        
        elif choice == "3":
            name = input(f"{user_name}, enter the habit name to check off: ")
            habit_tracker.checkoff_habit(name)
            print(f"Habit '{name}' checked off.")
        
        elif choice == "4":
            habits = habit_tracker.get_all_habits()
            if habits:
                print(f"{user_name}, here are your habits:")
                for habit in habits:
                    print(f"Habit: {habit.name}, Periodicity: {habit.periodicity} days, Current Streak: {habit.current_streak()}")
            else:
                print("You have no habits tracked yet.")
        
        elif choice == "5":
            periodicity = int(input(f"{user_name}, enter the periodicity (in days): "))
            habits = habit_tracker.get_habits_by_periodicity(periodicity)
            if habits:
                for habit in habits:
                    print(f"Habit: {habit.name}, Current Streak: {habit.current_streak()}")
            else:
                print(f"No habits found with a periodicity of {periodicity} days.")
        
        elif choice == "6":
            name = input(f"{user_name}, enter the habit name: ")
            streak = habit_tracker.longest_streak_for_habit(name)
            if streak is not None:
                print(f"The longest streak for '{name}' is {streak} days.")
            else:
                print(f"No streak information found for habit '{name}'.")
        
        elif choice == "7":
            struggled_habits = habit_tracker.habits_struggled_last_month()
            if struggled_habits:
                print(f"{user_name}, here are the habits you struggled with last month:")
                for habit_name in struggled_habits:
                    print(f"- {habit_name}")
            else:
                print("You did not struggle with any habits last month.")
        
        elif choice == "8":
            filename = input("Enter the filename to save (default is 'habits.json'): ") or "habits.json"
            habit_tracker.save_to_file(filename)
            print(f"Habits saved to {filename}.")
        
        elif choice == "9":
            filename = input("Enter the filename to load (default is 'habits.json'): ") or "habits.json"
            habit_tracker.load_from_file(filename)
            print(f"Habits loaded from {filename}.")
        
        elif choice == "10":
            print(f"Goodbye, {user_name}! Have a great day!")
            sys.exit()

if __name__ == "__main__":
    main()

