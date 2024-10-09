from connect_mysql import connect_database
import add_records as a
import delete_records as d
import retrieve_data as r
import update_records as u
import mysql.connector

def main():
    '''This main menu will allow the user to perform the following actions on the fitness center database: add a new member, 
    delete a member, update a member, view a member's details, add a new workout session, remove a workout session, 
    update a workout session, view a workout session's details, and view all workout sessions. When the user chooses 
    to quit, it will exit the program.'''
    conn = connect_database()
    if conn is not None:
        while True:
            cursor = conn.cursor()
            action = input('''
\033[1mMain Menu:\033[0m\n
1. Add a new member
2. Delete a member
3. Update a member
4. View member details
5. Add a new workout session
6. Remove a workout session
7. Update a workout session
8. View workout session details
9. View all workout sessions
10. Quit
    
Enter menu item (1-10): ''')
            try:
                # 6 = Quit
                if action == "10":
                    cursor.close()
                    conn.close()
                    break
                # 1 = Add a New Member
                elif action == "1":
                    # Prompt the user for necessary information
                    name, age = input("\nName: "), input("Age: ")
                    if a.add_member(name, age):
                        print(f"\nThe new member {name} was added successfully.")
                    else:
                        print(f"\nThe new member {name} could not be added successfully.")
                # 2 = Remove a Member
                elif action == "2": 
                    # Prompt the user for the member id to be removed
                    member_id = input("\nMember ID: ")
                    if d.delete_member(member_id):
                        print(f'\nMember {member_id} was successfully removed.')
                    else: 
                        print(f"\nMember {member_id} could not be removed.")
                # 3 = Update a Member
                elif action == "3":
                    # Prompt user for and member id to be updated along with new name and age
                    id, name, age = input("\nMember ID: "), input("New Name: "), input("New Age: ")
                    if u.update_member(id, name, age):
                        print(f"\nMember {id} was updated with {name} and {age}.")
                    else:
                        print(f"\nMember {id} could not be updated.")
                # 4 = View Member Details
                elif action == "4":
                    # Prompt the user for the member id to be viewed
                    member_id = int(input("\nMember ID: "))
                    member = r.get_member(member_id)
                    if member is not None:
                        print(f"\nMember ID: {member[0][0]}, Name: {member[0][1]}, Age: {member[0][2]}")
                    else: 
                        print(f"\nMember {member_id} not found.")
                # 5 = Add a New Workout Session
                elif action == "5":
                    # Prompt the user for necessary information
                    member_id, date, time, activity = input("\nMember ID: "), input("Date: "), input("Time: "), input("Activity: ")
                    if a.add_workout_session(member_id, date, time, activity):
                        print("\nThe new workout session was added successfully.")
                    else:
                        print("\nThe new workout session could not be added successfully.")
                # 6 = Remove a Workout Session
                elif action == "6": 
                    # Prompt the user for the member id to be removed
                    session_id = input("\nSession ID: ")
                    if d.delete_workout_session(session_id):
                        print(f'\nWorkout session {session_id} was successfully removed.')
                    else: 
                        print(f"\nWorkout session {session_id} could not be removed.")
                # 7 = Update a Workout Session
                elif action == "7":
                    # Prompt user for and member id to be updated along with new name and age
                    session_id, member_id, date, time, activity = input("\nSession ID: "), input("Member ID: "), input("New Date: "), input("New Time: "), input("New Activity: ")
                    if u.update_workout_session(session_id, member_id, date, time, activity):
                        print(f"\nWorkout session {session_id} was updated with new Member ID '{member_id}', date '{date}', time '{time}', activity '{activity}'.")
                    else:
                        print(f"\nWorkout session {session_id} could not be updated.")
                # 8 = View Workout Session Details
                elif action == "8":
                    # Prompt the user for the member id to be viewed
                    session_id = input("\nSession ID: ")
                    workout_session = r.get_workout_session(session_id)
                    if workout_session is not None:
                        print(f"\nSession ID: {workout_session[0][0]}, Member ID: {workout_session[0][1]}, Date: {workout_session[0][2]}, Time: {workout_session[0][3]}, Activity: {workout_session[0][4]}")
                    else: 
                        print(f"\nWorkout session {session_id} not found.")
                # 9 = View All Workout Sessions
                elif action == "9":
                    all_sessions = r.get_all()
                    if all_sessions is not None:
                        for session in all_sessions:
                            print(f"\nSession ID: {session[0]}, Date: {session[1]}, {session[2]}, Name: {session[5]} ({session[6]}yo), Activity: {session[3]}")
                    else: 
                        print("\nThere are currently no workout sessions in the system.")
                else:
                    # Raise value error for invalid inputs
                    raise ValueError()
                # Handling Database Errors
            except mysql.connector.Error as db_e: 
                print(f"\nDatabase error: {db_e}")
                # Handling Value Errors
            except ValueError:
                print(f"\nInvalid input: {action}. Please enter a number between 1 and 10.")          
                # Handling any other errors
            except Exception as e:
                print(f"\nAn error occurred: {e}")
                
if __name__ == "__main__":
    main()