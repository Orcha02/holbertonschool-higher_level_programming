#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa
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

    query = "SELECT cities.name\
    FROM cities, states\
    WHERE BINARY states.name = %s\
    AND cities.state_id = states.id\
    ORDER BY cities.id ASC"
    cursor.execute(query, (state_to_search,))

    all_rows = cursor.fetchall()
    print(", ".join(row[0] for row in all_rows))
    cursor.close()
    db.close()
