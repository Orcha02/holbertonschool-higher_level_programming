#!/usr/bin/python3
""" Script that lists all cities from the database hbtn_0e_4_usa """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """ Open database connection """
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                         passwd=mysql_password, db=database_name)
    cursor = db.cursor()

    query = "SELECT cities.id, cities.name, states.name\
    FROM cities, states\
    WHERE cities.state_id = states.id\
    ORDER BY cities.id ASC"
    cursor.execute(query)

    all_rows = cursor.fetchall()
    for row in all_rows:
        print(row)
    cursor.close()
    db.close()
