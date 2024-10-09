# Module 5 - Lesson 3 - Applying SQL in Python
Author: Elizabeth Yates

In this repository, I completed the following assignment: 

## 1. Gym Database Management with Python and SQL

*Objective:* The aim of this assignment is to reinforce your understanding of Python's interaction with SQL databases, focusing on CRUD (Create, Read, Update, Delete) operations in the context of a gym's membership and workout session management system. You will work with two tables: 'Members' and 'WorkoutSessions'.

*Problem Statement:* You are tasked with developing a Python application to manage a gym's database. The database consists of 'Members' and 'WorkoutSessions' tables. Your role is to implement various functions to add, retrieve, update, and delete records in these tables, ensuring data integrity and efficient data handling.

### Task 1: Add a Member

- Write a Python function to add a new member to the 'Members' table in the gym's database.

    # Example code structure
    def add_member(id, name, age):
        # SQL query to add a new member
        # Error handling for duplicate IDs or other constraints

*Expected Outcome:* A Python function that successfully adds a new member to the 'Members' table in the gym's database. The function should handle errors gracefully, such as duplicate member IDs or violations of other constraints.

### Task 2: Add a Workout Session

- Develop a Python function to add a new workout session to the 'WorkoutSessions' table for a specific member.

    # Example code structure
    def add_workout_session(member_id, date, duration_minutes, calories_burned):
        # SQL query to add a new workout session
        # Error handling for invalid member ID or other constraints

*Expected Outcome:* A Python function that adds a new workout session to the 'WorkoutSessions' table in the gym's database for a specific member. The function should handle errors gracefully, such as invalid member IDs or violations of other constraints.

### Task 3: Updating Member Information

- Implement a function to update the age of a member. Ensure that your function checks if the member exists before attempting the update.

    # Example code structure
    def update_member_age(member_id, new_age):
        # SQL query to update age
        # Check if member exists
        # Error handling

*Expected Outcome:* A Python function that updates the age of a member and handles cases where the member does not exist.
Task 4: Delete a Workout Session

### Task 4: Deleting a Member

- Create a Python function to delete a workout session based on its session ID. Include error handling for cases where the session ID does not exist.

    # Example code structure
    def delete_workout_session(session_id):
        # SQL query to delete a session
        # Error handling for non-existent session ID

*Expected Outcome:* A Python function that can delete a workout session using its session ID, with proper error handling for invalid IDs.

#### Submission Guidelines:

- Submit a Python script (.py file) containing all the functions for the tasks.
- Include comments in your code to explain your logic and SQL queries.
- Ensure your script handles errors gracefully and provides meaningful output.
