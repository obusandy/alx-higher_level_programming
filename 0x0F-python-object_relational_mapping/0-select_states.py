#!/usr/bin/python3

"""
     a script that lists all states from the database hbtn_0e_0_usa
     script should connect to a MySQL server running on localhost at port 3306
"""


import sys
import MySQLdb


if __name__ == '__main__':
"""
    Arguments:
        username: string username
        password: string password
        database: string database
"""
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    data = cursor.fetchall()

    for row in data:
        print(row)

    cursor.close()
    db.close()
