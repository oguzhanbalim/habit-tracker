# utils.py
import datetime
from habit import Habit
from habit_tracker import HabitTracker

def get_user_input(prompt, valid_responses):
    while True:
        response = input(prompt).strip().lower()
        if response in valid_responses:
            return response
        print(f"Please enter one of the following: {', '.join(valid_responses)}")

def load_predefined_habits(habit_tracker):
    predefined_habits = [
        {"name": "Read 10 Pages", "periodicity": 1, "checkoffs": ["2023-07-01", "2023-07-02", "2023-07-03", "2023-07-04", "2023-07-05", "2023-07-06", "2023-07-07"]},
        {"name": "Exercise", "periodicity": 1, "checkoffs": ["2023-07-01", "2023-07-02", "2023-07-03", "2023-07-05", "2023-07-06", "2023-07-07"]},
        {"name": "Drink 2.5 Liters of Water", "periodicity": 1, "checkoffs": ["2023-07-01", "2023-07-02", "2023-07-04", "2023-07-05", "2023-07-06"]},
        {"name": "Meditate for 10 Minutes", "periodicity": 1, "checkoffs": ["2023-07-01", "2023-07-03", "2023-07-04", "2023-07-06"]},
        {"name": "Weekly Review", "periodicity": 7, "checkoffs": ["2023-06-30"]}
    ]

    for habit_data in predefined_habits:
        habit = Habit(habit_data["name"], habit_data["periodicity"])
        habit.checkoffs = [datetime.datetime.strptime(date, "%Y-%m-%d") for date in habit_data["checkoffs"]]
        if habit.checkoffs:
            habit.last_checkoff_date = habit.checkoffs[-1].date()
        habit_tracker.habits[habit.name] = habit
        habit_tracker.habits_by_periodicity[habit.periodicity].append(habit)

