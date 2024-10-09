from connect_mysql import connect_database
import retrieve_data as r

conn = connect_database()
cursor = conn.cursor()

def delete_member(id):
    '''This function will remove a member and all their workout sessions from the database.'''
    # Check if the member exists
    if r.check_member(id):
        # Query 1: To remove the workout sessions for the member
        query1 = "DELETE FROM WorkoutSessions WHERE member_id = %s"
        cursor.execute(query1, (id, ))
        # Query 2: To remove the member 
        query2 = "DELETE FROM Members WHERE id = %s"
        cursor.execute(query2, (id, ))
        conn.commit()
        # If successful, return True
        return True
        # If unsuccessful, return False
    else:
        return False

def delete_workout_session(session_id):
    '''This function will remove a workout session from the Workout Sessions table.'''
    # Check if the workout session exists
    if r.check_workout_session(session_id):
        # Define the session
        session = (session_id, )
        # Define the query
        query = "DELETE FROM WorkoutSessions WHERE session_id = %s"
        # Execute Query
        cursor.execute(query, session)
        conn.commit()
        # If successful, return True
        return True
        # If unsuccessful, return False
    else:
        return False