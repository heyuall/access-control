import socket
import RPi.GPIO as GPIO
import time

HOST=""
PORT=8888

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setwarnings(False)
ajoutAngle = 5

print("\n+----------/ ServoMoteur  Controlleur /----------+")
print("|                                                |")
print("| Le Servo doit etre branche au pin 11 / GPIO 17 |")
print("|                                                |")
print("+------------------------------------------------+\n")

mySocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind( (HOST, PORT) )
mySocket.listen(1)
print("Waiting for connection")

connection, address=mySocket.accept()
print("Connection recieved from:", address[0])

connection.send(bytearray("SERVER>>> Connection successful", "utf-8"))
clientMessage=connection.recv(1024)


