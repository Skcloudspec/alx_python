import MySQLdb
import sys

def list_states(username, password, database):
    # Connect to MySQL server
    db = MySQLdb.connect(host='localhost', port=3306, user=username,
                         passwd=password, db=database)

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Create the test_1 database if it doesn't exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS test_1")

    # Switch to the test_1 database
    cursor.execute("USE test_1")

    # Create the states table if it doesn't exist
    cursor.execute("CREATE TABLE IF NOT EXISTS states ("
                   "id INT NOT NULL AUTO_INCREMENT,"
                   "name VARCHAR(256) NOT NULL,"
                   "PRIMARY KEY (id))")

    # Insert sample data into the states table
    cursor.execute("INSERT INTO states (name) VALUES ('California'), ('nevada'), ('New York')")

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

    # Call the function to list states
    list_states(username, password, database)
