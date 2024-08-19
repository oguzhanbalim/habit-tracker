# habit.py
import datetime

class Habit:
    def __init__(self, name, periodicity, created_at=None):
        self.name = name
        self.periodicity = periodicity
        self.created_at = created_at if created_at else datetime.datetime.now()
        self.checkoffs = []
        self.streak = 0
        self.last_checkoff_date = None

    def checkoff(self):
        today = datetime.date.today()
        if self.last_checkoff_date:
            delta = (today - self.last_checkoff_date).days
            if delta > self.periodicity:
                self.streak = 0
        self.checkoffs.append(datetime.datetime.now())
        self.last_checkoff_date = today
        self.streak += 1

    def current_streak(self):
        today = datetime.date.today()
        if self.last_checkoff_date:
            delta = (today - self.last_checkoff_date).days
            if delta <= self.periodicity:
                return self.streak
        return 0

    def longest_streak(self):
        if not self.checkoffs:
            return 0

        streaks = []
        current_streak = 1

        for i in range(1, len(self.checkoffs)):
            if (self.checkoffs[i].date() - self.checkoffs[i - 1].date()).days <= self.periodicity:
                current_streak += 1
            else:
                streaks.append(current_streak)
                current_streak = 1

        streaks.append(current_streak)
        return max(streaks)

    def to_dict(self):
        return {
            "name": self.name,
            "periodicity": self.periodicity,
            "created_at": self.created_at.isoformat(),
            "checkoffs": [dt.isoformat() for dt in self.checkoffs]
        }

    @classmethod
    def from_dict(cls, data):
        habit = cls(data["name"], data["periodicity"], datetime.datetime.fromisoformat(data["created_at"]))
        habit.checkoffs = [datetime.datetime.fromisoformat(dt) for dt in data["checkoffs"]]
        if habit.checkoffs:
            habit.last_checkoff_date = habit.checkoffs[-1].date()
        return habit

