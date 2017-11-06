import socket, select, string, sys
import MySQLdb
import pymysql


db = MySQLdb.connect(host='127.0.0.1',    # your host, usually localhost
                     user="root",         # your username
                     passwd="science",  # your password
                     db="chat",
		     	)        # name of the data base
#from pymongo import MongoClient
#client = MongoClient()
#db = client.test 
cursor = db.cursor()
def prompt() :
    sys.stdout.write('<You> ')
    sys.stdout.flush()
 
#main function
if __name__ == "__main__":
     
    if(len(sys.argv) < 3) :
        print 'Usage : python telnet.py hostname port'
        sys.exit()
     
    host = sys.argv[1]
    port = int(sys.argv[2])
     
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
     
    # connect to remote host
    try :
        s.connect((host, port))
    except :
        print 'Unable to connect'
        sys.exit()
     
    print 'Connected to remote host. Start sending messages'
    prompt()
     
    while 1:
        socket_list = [sys.stdin, s]
         
        # Get the list sockets which are readable
        read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])
         
        for sock in read_sockets:
            #incoming message from remote server
            if sock == s:
                data = sock.recv(4096)
		cursor.execute("INSERT INTO clientchat (text) VALUES (data)")
                if not data :
                    print '\nDisconnected from chat server'
                    sys.exit()
                else :
                    #print data
                    sys.stdout.write(data)
		    #cursor.execute("INSERT INTO clientchat (text) VALUES (data)")
                    prompt()
             
            #user entered a message
            else :
                msg = sys.stdin.readline()
		cursor.execute("INSERT INTO clientchat (textuser) VALUES(msg)")
                s.send(msg)
                prompt()
	
db.commit()
db.close()
