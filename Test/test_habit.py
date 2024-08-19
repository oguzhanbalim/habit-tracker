# test_habit.py
import unittest
from habit import Habit
import datetime

class TestHabit(unittest.TestCase):
    def test_creation(self):
        habit = Habit("Test Habit", 1)
        self.assertEqual(habit.name, "Test Habit")
        self.assertEqual(habit.periodicity, 1)
        self.assertEqual(len(habit.checkoffs), 0)
    
    def test_checkoff(self):
        habit = Habit("Test Habit", 1)
        habit.checkoff()
        self.assertEqual(len(habit.checkoffs), 1)
        self.assertEqual(habit.streak, 1)
    
    def test_current_streak(self):
        habit = Habit("Test Habit", 1)
        habit.checkoff()
        self.assertEqual(habit.current_streak(), 1)
    
    def test_longest_streak(self):
        habit = Habit("Test Habit", 1)
        habit.checkoff()
        self.assertEqual(habit.longest_streak(), 1)

if __name__ == '__main__':
    unittest.main()

