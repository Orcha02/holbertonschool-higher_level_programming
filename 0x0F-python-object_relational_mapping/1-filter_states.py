#!/usr/bin/python3
"""
Script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """ Open database connection """
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states\
    WHERE name LIKE BINARY 'N%' ORDER BY id ASC")

    all_rows = cursor.fetchall()
    for row in all_rows:
        print(row)
    cursor.close()
    db.close()

# LIKE-> Is used in a WHERE clause to search for specified pattern in a column
# BINARY-> Compares if its exactly the same
