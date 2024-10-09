from connect_mysql import connect_database

conn = connect_database()
cursor = conn.cursor()

def get_all():
    '''This function returns all workout sessions along with the member names and ages.'''
    # Define query
    query = '''
    SELECT s.session_id, s.session_date, s.session_time, s.activity, m.id, m.name, m.age
    FROM WorkoutSessions s, Members m
    WHERE s.member_id = m.id
    '''
    # Execute query
    cursor.execute(query)
    # Returns a list of all the workout sessions plus the names and ages of the members in the workout session
    return cursor.fetchall()

def get_member(id):
    '''This function will return the member information for the id provided.'''
    # Check if the member exists
    if check_member(id):
        # Define query
        query = "SELECT * FROM Members WHERE id = %s"
        # Execute query
        cursor.execute(query, (id, ))
        # Return member
        return cursor.fetchall()
    # Return None if member not found
    else:
        return None

def get_workout_session(session_id):
    '''This function will return the workout session information for the id provided.'''
    # Check if the workout session exists
    if check_workout_session(session_id):
        # Define query
        query = "SELECT * FROM WorkoutSessions WHERE session_id = %s"
        # Execute query
        cursor.execute(query, (session_id, ))
        # Return workout session
        return cursor.fetchall()
    # Return None if workout session not found.
    else:
        return None
    
def check_member(id):
    '''Returns True if the member with the provided id is found, and False if the member is not found.'''
    # Define query
    query = "SELECT id FROM Members WHERE id = %s"
    # Execute Query
    cursor.execute(query, (id, ))
    if cursor.fetchone():
        return True
    else:
        return False

def check_workout_session(session_id):
    '''Returns True if the member with the provided id is found, and False if the member is not found.'''
    # Define query
    query = "SELECT session_id FROM WorkoutSessions WHERE session_id=%s"
    # Execute query
    cursor.execute(query, (session_id, ))
    if cursor.fetchone():
        return True
    else:
        return False