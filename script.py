import MySQLdb
import datetime
import random
import threading

conn = MySQLdb.connect(host="localhost",
                  user="czo",
                  passwd="czo",
                  db="czo")
db = conn.cursor()

#details for node

# node_id = 2   #avaialable town1 town2 town3
# signal_str = random.randint(80,101)
# battery_str =random.randint(80,101)
# ctimestamp =datetime.datetime.now()
# data =random.randint(150,240)
#close data


# node = db.execute("SELECT node_id from app_nodestats WHERE node_id=3")
# print(node)

insert_query = "INSERT INTO app_nodedata (node_id,signal_str,battery_str,ctimestamp,data) VALUES(%s,%s,%s,%s,%s) "


def printit():
	node_id = 1   #avaialable town1 town2 town3
	signal_str = random.randint(80,101)
	battery_str =random.randint(80,101)
	ctimestamp =datetime.datetime.now()
	data =random.randint(150,240)
	insert_query_args = (node_id,signal_str,battery_str,ctimestamp,data,)

	try:
		db.execute(insert_query,insert_query_args)
		print('inserted successfully')
		conn.commit()
	except Exception,e: print str(e)
	
	threading.Timer(2.0, printit).start()

printit()
# data = db.fetchone()

# db.close()
