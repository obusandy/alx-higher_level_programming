#!/usr/bin/python3
    """
    a script that lists all states from
    the database hbtn_0e_0_usa
    script should connect to a MySQL
    server running on localhost at port 3306
    """

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Arguments:
    username: string username
    password: string password
    database: string database
    """
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
            passwd=argv[2], db=argv[3])

    curs = db.cursor()
    curs.execute("SELECT * FROM states")
    lines = curs.fetchall()

for lines in lines:
    print(lines)
