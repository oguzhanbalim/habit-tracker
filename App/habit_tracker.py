import json
import datetime
from collections import defaultdict
from habit import Habit

class HabitTracker:
    def __init__(self):
        self.habits = {}
        self.habits_by_periodicity = defaultdict(list)

    def add_habit(self, name, periodicity):
        habit = Habit(name, periodicity)
        self.habits[name] = habit
        self.habits_by_periodicity[periodicity].append(habit)

    def delete_habit(self, name):
        if name in self.habits:
            habit = self.habits.pop(name)
            self.habits_by_periodicity[habit.periodicity].remove(habit)

    def checkoff_habit(self, name):
        if name in self.habits:
            self.habits[name].checkoff()
        else:
            print(f"Habit '{name}' does not exist.")

    def get_all_habits(self):
        return list(self.habits.values())

    def get_habits_by_periodicity(self, periodicity):
        return self.habits_by_periodicity[periodicity]

    def longest_streak_all(self):
        return max((habit.calculate_longest_streak() for habit in self.habits.values()), default=0)

    def longest_streak_for_habit(self, name):
        if name in self.habits:
            return self.habits[name].calculate_longest_streak()
        return 0

    def habits_struggled_last_month(self):
        one_month_ago = datetime.date.today() - datetime.timedelta(days=30)
        struggled_habits = []
        for habit in self.habits.values():
            if not habit.checkoffs or habit.checkoffs[-1].date() < one_month_ago:
                struggled_habits.append(habit.name)
        return struggled_habits

    def save_to_file(self, filename="habits.json"):
        with open(filename, "w") as f:
            json.dump({name: habit.to_dict() for name, habit in self.habits.items()}, f)

    def load_from_file(self, filename="habits.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                self.habits = {name: Habit.from_dict(h) for name, h in data.items()}
                self.habits_by_periodicity = defaultdict(list)
                for habit in self.habits.values():
                    self.habits_by_periodicity[habit.periodicity].append(habit)
        except FileNotFoundError:
            print(f"File '{filename}' not found. Starting with an empty habit tracker.")

