#!/usr/bin/python3
""" Get all states """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
<<<<<<< HEAD
                        passwd=sys.argv[2], db=sys.argv[3], port=3306)
=======
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
>>>>>>> 28ff9e3458867786bc178ef5a318f4d43c246fac
    c = db.cursor()
    c.execute("SELECT * FROM STATES")
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
