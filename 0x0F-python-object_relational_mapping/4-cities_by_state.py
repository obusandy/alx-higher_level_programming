#!/usr/bin/python3
"""
 a script that lists all cities from
 the database hbtn_0e_4_usa
  script should take 3 arguments:
  mysql username, mysql password and database name
"""

import sys
import MySQLdb

if __name__ == "__main__":
   # main execution block
    # Get MySQL credentials
    dtbs = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    # Connect to MySQL server
    crs = dtbs.cursor()

    # Execute the SQL query to retrieve all states
    crs.execute("SELECT `c`.`id`, `c`.`name`, `s`.`name` \
                 FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                   ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")

    # Fetch all rows and print the result state
    [print(rslts) for rslts in crs.fetchall()]
