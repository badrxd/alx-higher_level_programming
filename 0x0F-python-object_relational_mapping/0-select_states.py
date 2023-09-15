#!/usr/bin/python3
''' script that lists all states from the database hbtn_0e_0_usa '''

import sys
import MySQLdb

if __name__ == '__main__':

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT id,name  FROM states ORDER BY id ASC")
    data = cur.fetchall()
    for DATA in data:
        print(DATA)
    cur.close()
    db.close()
