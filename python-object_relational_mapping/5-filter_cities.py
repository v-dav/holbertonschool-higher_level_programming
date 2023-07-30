#!/usr/bin/python3
"""a script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    """Connexion to the database"""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    """Defining the cursor"""
    cursor = db.cursor()

    """Execute the query"""
    cursor.execute(
        """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name LIKE BINARY %s
        ORDER BY cities.id
        """, (sys.argv[4],)
    )

    """Get results of the query"""
    rows = cursor.fetchall()

    """Format the output into a string"""
    city_names = []
    for row in rows:
        city_names.append(row[0])
    string = ", ".join(city_names)
    print(string)

    """Close cursor session and connexion"""
    cursor.close()
    db.close()
