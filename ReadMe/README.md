Welcome to the Habit Tracker project! This application is a command-line tool that helps you manage and track your habits, monitor your progress, and stay motivated. Whether you're trying to build new habits or maintain existing ones, this tool is designed to support your journey.

Project Details
GitHub Profile: oguzhanbalim
Date: 19 August 2024
Course: Object Oriented and Functional Programming with Python
Institution: IU International University of Applied Science
Developer: Oğuzhan Balım

Features
Track Habits: Easily add, delete, and check off habits.
Monitor Streaks: Keep track of how many days in a row you've successfully maintained a habit.
Analyze Progress: View the longest streaks for each habit and identify habits you struggled with.
Save and Load: Save your progress to a file and load it anytime to continue where you left off.
Getting Started
Prerequisites
To use this Habit Tracker, you'll need to have Python 3 installed on your computer. Python is a popular programming language, and you can download it here. https://www.python.org/

Download the Project
Clone the Repository:

If you are familiar with Git, you can clone this repository directly using the following command in your terminal:

sh
git clone https://github.com/oguzhanbalim/habit-tracker.git

If you're not familiar with Git, you can also:

Go to the GitHub repository page for this project.
Click on the green "Code" button.
Choose "Download ZIP" and save the file to your computer.
Extract the ZIP file to a folder on your computer.
Navigate to the Project Folder:

Open a terminal (Command Prompt or PowerShell on Windows, Terminal on macOS/Linux).
Use the cd command to navigate to the folder where you extracted the files.
Example:

sh
cd path_to_your_project_folder/habit-tracker

How to Run the Habit Tracker
Open the Terminal:

On Windows: Search for "cmd" or "Command Prompt" in the Start menu.
On macOS: Search for "Terminal" in Spotlight.
On Linux: Look for "Terminal" in your applications menu.
Run the Application:

In the terminal, type the following command and press Enter:

sh
python cli.py

This will start the Habit Tracker application. You will see a menu with options to add, delete, and check off habits, among other features.

Follow the On-Screen Instructions:

The application will guide you through various options. Simply follow the prompts to interact with the Habit Tracker.
Saving and Loading Your Habits
Save Your Progress: You can save your habits and streaks to a file by selecting the appropriate option in the application. The default file name is habits.json, but you can choose a different name if you like.

Load Your Progress: To load your habits from a saved file, the application will automatically load the habits.json file when it starts. If the file doesn't exist, it will start fresh. You can also specify a different file if needed.

Running Tests
If you're interested in making sure everything works correctly, the project includes some automated tests. Here's how you can run them:

Run All Tests:

In the terminal, run the following command:

sh
python -m unittest discover

This will execute all the tests included in the project to verify that everything is working as expected.

Project Structure
Here's a breakdown of the project's structure:

habit.py: Contains the Habit class, which defines what a habit is and how it works.
habit_tracker.py: Manages multiple habits, allowing you to add, delete, and check off habits.
utils.py: Provides utility functions to help with input validation and loading predefined habits.
cli.py: The command-line interface that you interact with to use the Habit Tracker.
test_habit.py and test_habit_tracker.py: Automated tests to ensure that the Habit Tracker works correctly.
Contribution

If you'd like to contribute to this project, feel free to fork the repository, make your changes, and submit a pull request. Contributions are always welcome!

Acknowledgements
This project was created as part of the Object Oriented and Functional Programming with Python course at IU International University of Applied Science by Oğuzhan Balım on 19 August 2024.

