```python
#!/usr/bin/python3
"""
Script that lists all states with a name starting with n(lowercase n)
from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys


if __name__ == "__main__":
    # Connect to the database using the arguments
    username, password, db_name = sys.argv[1:]
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name,
        charset="utf8")

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Execute the query
    cursor.execute("""SELECT * FROM states
                   WHERE name LIKE BINARY 'n%'
                   ORDER BY id ASC""")

    # Display the results
    results = cursor.fetchall()

    for row in results:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
