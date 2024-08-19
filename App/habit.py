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
        else:
            delta = self.periodicity
        
        if delta <= self.periodicity:
            self.streak += 1
        
        self.checkoffs.append(datetime.datetime.now())
        self.last_checkoff_date = today

    def current_streak(self):
        today = datetime.date.today()
        if self.last_checkoff_date:
            delta = (today - self.last_checkoff_date).days
            if delta <= self.periodicity:
                return self.streak
        return 0

    def calculate_longest_streak(self):  # Renamed method to avoid conflict
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
            "checkoffs": [dt.isoformat() for dt in self.checkoffs],
            "streak": self.streak,
            "last_checkoff_date": self.last_checkoff_date.isoformat() if self.last_checkoff_date else None
        }

    @classmethod
    def from_dict(cls, data):
        habit = cls(data["name"], data["periodicity"], datetime.datetime.fromisoformat(data["created_at"]))
        habit.checkoffs = [datetime.datetime.fromisoformat(dt) for dt in data["checkoffs"]]
        habit.streak = data.get("streak", 0)
        habit.last_checkoff_date = datetime.date.fromisoformat(data["last_checkoff_date"]) if data["last_checkoff_date"] else None
        return habit
