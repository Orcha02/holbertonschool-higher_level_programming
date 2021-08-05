#!/usr/bin/python3
""" Script that lists all states from the database hbtn_0e_0_usa """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """  Open database connection """
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
# Prepare a cursor object using cursor() method
cursor = db.cursor()
# Query the database - must be sorted in ascending order by states.id
cursor.execute("SELECT * FROM states ORDER BY id ASC")
# Fetch all rows
all_rows = cursor.fetchall()
for row in all_rows:
    print(row)
# Disconnect from server
cursor.close()
db.close()
