from connect_mysql import connect_database

conn = connect_database()
cursor = conn.cursor()

def add_member(name, age):
    '''This function will add a new member with the name and age parameters to the Members table.'''
    try:
        # Define member
        member = (name,age)
        # Define query
        query = "INSERT INTO Members (name, age) VALUES(%s, %s)"
        # Execute the query
        cursor.execute(query, member)
        conn.commit()
        # If successful, it will return True
        return True
        # If unsuccessful, it will return False
    except Exception:
        return False

def add_workout_session(member_id, date, time, activity):
    '''This function will add a new workout session with the member id, date, time, and activity parameters to the 
    Workout Sessions table.'''
    try:
        # Define session
        session = (member_id, date, time, activity)
        # Define query
        query = "INSERT INTO WorkoutSessions (member_id, session_date, session_time, activity) VALUES(%s, %s, %s, %s)"
        # Execute Query
        cursor.execute(query, session)
        conn.commit()
        # If successful, it will return True
        return True
        # If unsuccessful, it will return False
    except Exception:
        return False