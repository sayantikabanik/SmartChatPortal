import client
import server
from pymongo import MongoClient
client = MongoClient('localhost:27017')

client = MongoClient('localhost:27017')
db = client.chatdata

def insert():
    try:
 	   chatport = PORT
           clientdata= data
   	   clientmsg=msg
    #if((clientdata &&clientmsg )!= None ):
	   db.chatdata.insert_one(
        	{
		 	"port": chatport,
		 	"data":clientdata,
			 "msg":clientmsg}) 
           print '\nInserted data successfully\n'
    
	   except Exception, e:
	    	 print str(e)
def read():
    try:
	    chatCol = db.chatdata.find()
    	    print '\n All data from EmployeeData Database \n'
            for chat in chatCol:
	            print chat

    except Exception, e:
        print str(e)


