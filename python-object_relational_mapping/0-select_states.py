#!/usr/bin/python3
"""A script that lists all states from the database hbtn_0e_0_usa"""

import sys
print(sys.path)

import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user="root",
                         passwd="root", db="hbtn_0e_0_usa")
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id")
    cur.close()
    db.close()
