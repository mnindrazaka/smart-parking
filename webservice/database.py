import MySQLdb
import MySQLdb.cursors

db = MySQLdb.connect(
    host="localhost", user="root", passwd="", db="smart-parking")

cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
