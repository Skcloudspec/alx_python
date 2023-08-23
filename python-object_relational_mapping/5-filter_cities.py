import MySQLdb
import sys


def filter_cities_by_state(username, password, database, state_name):
    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute the SQL query to fetch cities of the given state
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))

    # Fetch and print the results
    results = cursor.fetchall()
    cities = [row[0] for row in results]
    print(", ".join(cities))

    # Close the cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    # Retrieve MySQL connection credentials and state name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Call the filter_cities_by_state function
    filter_cities_by_state(username, password, database, state_name)
