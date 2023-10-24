#!/usr/bin/python3
""" Task 0 """

import sys
import MySQLdb


def all_states():
    """ Lists all states from the database """

    """ Connect to MySQL """
    DB = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], DB=sys.argv[3])

    """ Set a cursor """
    cursor = DB.cursor()

    """ Inject SQL Query """
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    """ Grab the results of the Query """
    states = cursor.fetchall()

    for state in states:
        print(state)

    """ Close the connection """
    cursor.close()
    DB.close()


if __name__ == "__main__":
    all_states()
