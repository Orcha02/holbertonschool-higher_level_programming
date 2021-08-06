#!/usr/bin/python3
"""
Script that takes in arguments and displays all values in the
states tableof hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """ Open database connection """
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]
    state_to_search = argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                         passwd=mysql_password, db=database_name)
    cursor = db.cursor()
# Prevention of MySQL injections
    query = "SELECT * FROM states\
    WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_to_search,))

    all_rows = cursor.fetchall()
    for row in all_rows:
        print(row)
    cursor.close()
    db.close()
