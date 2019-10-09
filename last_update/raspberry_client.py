import socket
HOST='192.168.8.200'
PORT=8888

print ("Attempting connection")
mySocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.connect(( HOST, PORT))
print ("Connected to server")

serverMessage=mySocket.recv(1024)


  #print (serverMessage)
clientMessage=input("Client: ")
mySocket.send(bytearray(clientMessage, "utf-8"))


print ("Connection ended.")
mySocket.close()