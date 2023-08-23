import MySQLdb
import sys


def filter_states(username, password, database):
    # Connect to MySQL server
    db = MySQLdb.connect(host='localhost', port=3306, user=username,
                         passwd=password, db=database)

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute the query to select states with names starting with 'N' (case-insensitive)
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

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

    # Call the function to filter and list states
    filter_states(username, password, database)
