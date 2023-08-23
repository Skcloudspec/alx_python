import MySQLdb
import sys


def filter_states(username, password, database, state_name):
    # Connect to MySQL server
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Prepare the SQL query with user input
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    # Execute the query
    cursor.execute(query, (state_name,))

    # Fetch all rows from the result set
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()


if __name__ == '__main__':
    # Get command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Call the function to filter and list states
    filter_states(username, password, database, state_name)
