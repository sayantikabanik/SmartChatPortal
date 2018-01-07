import sys
import os
import socket, select
import MySQLdb
import pymysql
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer



db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="science",  # your password
                     db="chat")        # name of the data base
cursor = db.cursor()

def putdata():
	cursor.execute("SELECT * from chating")
	#row = str([cell.encode('utf-8') for cell in row])
	row = cursor.fetchone()

	print("printing the conversation on the console")
	while row is not None:
            print(row)
            row= cursor.fetchone()
            opinion=TextBlob(str(row),analyzer=NaiveBayesAnalyzer());
            print(opinion.sentiment);
            row = cursor.fetchone()


 
    


if __name__=="__main__":
	putdata()
