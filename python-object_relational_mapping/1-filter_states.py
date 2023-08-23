```python
#!/usr/bin/python3
"""
Script that lists all states with a name starting with N(upper N or lower n)
"""
import MySQLdb
import sys

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: {} USERNAME PASSWORD DATABASE".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1:]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database)

    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
