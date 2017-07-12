import MySQLdb
import datetime
import random
import threading

conn = MySQLdb.connect(host="localhost",
                  user="czo",
                  passwd="czo",
                  db="czo")
db = conn.cursor()

select_query = "SELECT * FROM app_nodedata"
insert_query = "INSERT INTO app_nodedata(battery_str) VALUES(%s) "

def printit():
	insert_query_args = (random.randint(80,101),)
	if db.execute(insert_query,insert_query_args):
		print('inserted successfully')
		conn.commit()
	else:
		print('error occured')	
		conn.rollback()
	
	threading.Timer(1.0, printit).start()

printit()
# data = db.fetchone()

# db.close()
