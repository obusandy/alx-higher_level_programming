#!/usr/bin/python3

"""
 a script that takes in the name of a state as an argument and
 lists all cities of that state, using the database hbtn_0e_4_usa
 script should take 4 arguments:
 mysql username, mysql password, database name and
 state name (SQL injection free!)


   Arguments:
            username: String(username)
            password:String(password)
            database: string (database)
            state name: string(state's name)
"""

import sys
import MySQLdb

if __name__ == "__main__":
 
    # Get MySQL credentials
    dtbs = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    crs = dtbs.cursor()

    # Execute the SQL queries
    queries = ("SELECT * FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                   ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")
    crs.execute(queries)

    # Print the cities separated by commas
    print(", ".join([cities[2] for cities in crs.fetchall() if cities[4] == sys.argv[4]]))
