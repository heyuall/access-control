import socket
import sys
import _thread

HOST = ''
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket created')

try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

print( 'Socket bind complete')

s.listen(10)
print( 'Socket now listening')

def clientthread(conn):
    #Sending message to connected client
    conn.send(bytes(10))

    #infinite loop so that function do not terminate and thread do not end.
    while True:

        #Receiving from client
        data = conn.recv(1024)
        reply = bytes(100)
        print (data)
        if not data:
            break

        conn.sendall(reply)

    conn.close()

#now keep talking with the client
while 1:
    #wait to accept a connection
    conn, addr = s.accept()
    print ('Connected with ' + addr[0] + ':' + str(addr[1]))

    #start new thread
    _thread.start_new_thread(clientthread ,(conn,))

s.close()