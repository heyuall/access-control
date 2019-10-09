import face_recognition
import cv2
import os
import pickle
from pymongo import MongoClient
import datetime

import socket
HOST='192.168.25.250'
PORT=8888

print("connecting to the data base...")
with open('pickles/data.pickle','rb') as f:
    database = pickle.load(f)

known_face_names=[i for i in database]
print("names of people in the data base")
print(known_face_names)
known_face_encodings=[database[i] for i in database]
video_capture = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 4.0, (640,480))
while True:
    ret, frame = video_capture.read()
    frame=cv2.flip(frame,1,0)
    rgb_frame = frame[:, :, ::-1] #gray scale

    face_locations = face_recognition.face_locations(rgb_frame) #searching for faces in video
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations) #decoding the faces

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings): #parcourir tous les faces
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding) #tester si un visage est semblabe dans la base

        
        print(matches)
        # If a match was found y7ot carreiy a5dherrrrr
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
            color = (0,255,0)
            stroke = 2
            cv2.rectangle(frame, (left, top), (right, bottom),color, stroke)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left+6 , top-6 ), font, 1.0, (255, 255, 255), 1) #+6-6

            #enregistrement dans la base de données
            try:
                conn = MongoClient()
                print("Connected successfully!!!")
            except:
                print("Could not connect to MongoDB")

            # database
            db = conn.proget_db

            # Created or Switched to collection names: my_gfg_collection
            collection = db.historiques
            date = datetime.datetime.now()

            emp_rec1 = {
                "username": name,
                "date": str(date)
            }

            # Insert Data
            rec_id1 = collection.insert_one(emp_rec1)

            print("Data inserted with record ids", rec_id1)

            # Printing the data inserted
            cursor = collection.find()
            for record in cursor:
                print(record)

            #envoi socket
            print("Attempting connection")
            mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            mySocket.connect((HOST, PORT))
            print("Connected to server")

            serverMessage = mySocket.recv(1024)

            # print (serverMessage)
            clientMessage = name
            mySocket.send(bytearray(clientMessage, "utf-8"))

            print("Connection ended.")
            mySocket.close()


        else: #carreau a7mer
        	name = "Unknown"
        	color = (0, 0, 255)
        	cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
        	font = cv2.FONT_HERSHEY_DUPLEX
        	cv2.putText(frame, name, (left+6 , top-6 ), font, 1.0, (255, 255, 255), 1)

    out.write(frame)
    cv2.imshow('Video', frame)

    #quit = q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
out.release()
cv2.destroyAllWindows()

