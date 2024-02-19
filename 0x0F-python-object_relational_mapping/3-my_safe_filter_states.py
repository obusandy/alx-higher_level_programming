#!/usr/bin/python3

"""
do you remember the previous task?
its an SQL injection to delete all records of a table
 a script that takes in arguments and
 displays all values in the states table of hbtn_0e_0_usa
 where name matches the argument.
 But this time, write one that is safe from MySQL injections!
"""

import sys
import MySQLdb


def state_value(username, password, database, state_name):
    """
     Retrieves and prints values from the states table
    Arguments:
        username (string): MySQL username
        password (strng): MySQL password
        database (string): MySQL database.
        state_name (string): state to search for.

    Returns:
        None
    """
    # Establish a secure connection to the MySQL database
    connection = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database)
    curs = connection.cursor()
    # Create a cursor for executing SQL queries
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    curs.execute(query, (state_name,))
    # Retrieve the results
    rslts = curs.fetchall()
    # Retrieve the results
    curs.close()
    connection.close()
    # Print the retrieved state results
    for rslts in rslts:
        print(rslts)


if __name__ == "__main__":
    """
    Main execution block
    """
    if len(sys.argv) != 5:
        print("error")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
    # 
    state_value(username, password, database, state_name)
