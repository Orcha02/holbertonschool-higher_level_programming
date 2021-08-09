#!/usr/bin/python3
""" Script that lists all states from the database hbtn_0e_0_usa """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """  Open database connection """
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cursor = db.cursor()  # Prepare a cursor object using cursor() method
    cursor.execute("SELECT * FROM states ORDER BY id ASC")  # Query the dbase

    all_rows = cursor.fetchall()  # Fetch all rows
    for row in all_rows:
        print(row)
    cursor.close()  # Disconnect from server
    db.close()
