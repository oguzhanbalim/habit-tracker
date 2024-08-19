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
        {
            "name": "Read 10 Pages",
            "periodicity": 1,
            "checkoffs": [
                "2024-08-01", "2024-08-02", "2024-08-03", "2024-08-04", "2024-08-05", "2024-08-06", "2024-08-07",
                "2024-08-08", "2024-08-09", "2024-08-10", "2024-08-11", "2024-08-12", "2024-08-13", "2024-08-14",
                "2024-08-15", "2024-08-16", "2024-08-17", "2024-08-18", "2024-08-19", "2024-08-20", "2024-08-21",
                "2024-08-22", "2024-08-23", "2024-08-24", "2024-08-25", "2024-08-26", "2024-08-27", "2024-08-28"
            ]
        },
        {
            "name": "Exercise",
            "periodicity": 1,
            "checkoffs": [
                "2024-08-01", "2024-08-02", "2024-08-03", "2024-08-05", "2024-08-06", "2024-08-07",
                "2024-08-08", "2024-08-09", "2024-08-10", "2024-08-12", "2024-08-13", "2024-08-14",
                "2024-08-15", "2024-08-16", "2024-08-17", "2024-08-19", "2024-08-20", "2024-08-21",
                "2024-08-22", "2024-08-23", "2024-08-24", "2024-08-26", "2024-08-27", "2024-08-28"
            ]
        },
        {
            "name": "Drink 2.5 Liters of Water",
            "periodicity": 1,
            "checkoffs": [
                "2024-08-01", "2024-08-02", "2024-08-04", "2024-08-05", "2024-08-06", "2024-08-07",
                "2024-08-08", "2024-08-09", "2024-08-11", "2024-08-12", "2024-08-13", "2024-08-14",
                "2024-08-15", "2024-08-16", "2024-08-18", "2024-08-19", "2024-08-20", "2024-08-21",
                "2024-08-22", "2024-08-23", "2024-08-25", "2024-08-26", "2024-08-27", "2024-08-28"
            ]
        },
        {
            "name": "Meditate for 10 Minutes",
            "periodicity": 1,
            "checkoffs": [
                "2024-08-01", "2024-08-03", "2024-08-04", "2024-08-06", "2024-08-07", "2024-08-08",
                "2024-08-10", "2024-08-11", "2024-08-13", "2024-08-14", "2024-08-15", "2024-08-17",
                "2024-08-18", "2024-08-20", "2024-08-21", "2024-08-22", "2024-08-24", "2024-08-25",
                "2024-08-27", "2024-08-28"
            ]
        },
        {
            "name": "Weekly Review",
            "periodicity": 7,
            "checkoffs": [
                "2024-08-01", "2024-08-08", "2024-08-15", "2024-08-22"
            ]
        }
    ]

    for habit_data in predefined_habits:
        habit = Habit(habit_data["name"], habit_data["periodicity"])
        habit.checkoffs = [datetime.datetime.strptime(date, "%Y-%m-%d") for date in habit_data["checkoffs"]]
        if habit.checkoffs:
            habit.last_checkoff_date = habit.checkoffs[-1].date()
        habit_tracker.habits[habit.name] = habit
        habit_tracker.habits_by_periodicity[habit.periodicity].append(habit)

