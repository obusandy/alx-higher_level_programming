#!/usr/bin/python3

"""
a script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
must use the module MySQLdb (import MySQLdb)
Results must be sorted in ascending order by states.id
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Establish a connection to the MySQL database.
    dtbs = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    # Create a cursor object to execute SQL statements
    crs = dtbs.cursor()

    # Execute the SQL query to retrieve matching current state
    crs.execute("SELECT * \
                 FROM `states` \
                WHERE BINARY `name` = '{}'".format(sys.argv[4]))

    # print the results
    [print(currentrslt) for currentrslt in crs.fetchall()]
