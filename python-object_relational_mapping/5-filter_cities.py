#!/usr/bin/python3
""" Task 5 """

import sys
import MySQLdb


def all_cities():
    """ List all cities by argument """

    """ Connect to MySQL """
    DB = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    """ Set a cursor """
    cursor = DB.cursor()

    """ Inject SQL Query """
    cursor.execute("SELECT cities.name \
                    FROM cities \
                    INNER JOIN states ON cities.state_id = states.id \
                    WHERE states.name = %s \
                    ORDER BY cities.id ASC", (sys.argv[4],))

    """ Grab the results of the Query """
    cities = cursor.fetchall()

    for city in cities:
        print(city)

    """ Close the connection """
    cursor.close()
    DB.close()


if __name__ == "__main__":
    all_cities()
