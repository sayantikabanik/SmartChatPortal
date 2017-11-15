import sys
import os
import socket, select
import MySQLdb
import pymysql



db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="science",  # your password
                     db="chat")        # name of the data base
cursor = db.cursor()

def putdata():
	cursor.execute("SELECT * from chating")
	row = cursor.fetchone()
	print("printing the conversation")
	while row is not None:
            print(row)
            row = cursor.fetchone()
 
    


if __name__=="__main__":
	putdata()
