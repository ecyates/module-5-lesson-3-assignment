from connect_mysql import connect_database
import retrieve_data as r

conn = connect_database()
cursor = conn.cursor()

def update_member(id, name, age):
    if r.check_member(id):
        # Define member
        member = (name,age, id)
        # Define query
        query = "UPDATE Members SET name = %s, age = %s WHERE id = %s"
        # Execute Query
        cursor.execute(query, member)
        conn.commit()
        # If successful, return True
        return True
        # If unsuccessful, return False
    else: 
        return False

def update_workout_session(session_id, member_id, date, time, activity):
    if r.check_workout_session(session_id):
        # Define session
        session = (member_id, date, time, activity, session_id)
        # Define workout
        query = "UPDATE WorkoutSessions SET member_id = %s, session_date = %s, session_time = %s, activity = %s WHERE session_id = %s"
        # Execute Query
        cursor.execute(query, session)
        conn.commit()
        # If successful, return True
        return True
        # If unsuccessful, return False
    else: 
        return False