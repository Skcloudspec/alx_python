```python
#!/usr/bin/python3
"""Script that displays all values in the states table of hbtn_0e_0_usa
where name matches the argument"""

import sys
import MySQLdb

if __name__ == "__main__":
    # retrieve command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # connect to MySQL server
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=mysql_username,
                         passwd=mysql_password,
                         db=database_name)

    # execute SQL query to retrieve states with matching name
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name='{}' ORDER BY id"
                   .format(state_name))

    # fetch all matching rows and display results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # close cursor and database connections
    cursor.close()
    db.close() 
