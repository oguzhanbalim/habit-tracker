# test_habit_tracker.py
import unittest
from habit_tracker import HabitTracker
from habit import Habit

class TestHabitTracker(unittest.TestCase):
    def setUp(self):
        self.habit_tracker = HabitTracker()
    
    def test_add_habit(self):
        self.habit_tracker.add_habit("Test Habit", 1)
        self.assertIn("Test Habit", self.habit_tracker.habits)
    
    def test_delete_habit(self):
        self.habit_tracker.add_habit("Test Habit", 1)
        self.habit_tracker.delete_habit("Test Habit")
        self.assertNotIn("Test Habit", self.habit_tracker.habits)
    
    def test_checkoff_habit(self):
        self.habit_tracker
