#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """ Open database connection """
# Better visualize of args organization
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]
    name_to_search = argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                         passwd=mysql_password, db=database_name)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states\
    WHERE name LIKE BINARY '{}' ORDER BY id ASC".format(name_to_search))

    all_rows = cursor.fetchall()
    for row in all_rows:
        print(row)
    cursor.close()
    db.close()
