#!/usr/bin/python3
"""
a script that lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa:
script should take 3 arguments:
mysql username, mysql password and database name
no argument validation needed
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
   Arguments:
            username(string): username
            password(string): password
            dtbs(string): database
    """
    dtbs = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    cursr = dtbs.cursor()
    cursr.execute("SELECT * FROM states \
                 WHERE name LIKE BINARY 'N%' \
                 ORDER BY states.id ASC")
    lines = cursr.fetchall()

    for line in lines:
        print(line)