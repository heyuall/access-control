import face_recognition
import cv2
import os
import pickle


database={}
print("trainning...")
for root, dirs, files in os.walk("data"):
    for file in files:
        if file.endswith("png") or file.endswith("jpg") or file.endswith("pgm"):
            path = os.path.join(root, file)
            label = os.path.basename(root)
            print("decoding "+label+" image")
            image=face_recognition.load_image_file(path)
            image_encoding = face_recognition.face_encodings(image)[0]
            print(image_encoding)
            database[label]=image_encoding


print("finshed trainning")        
with open("pickles/data.pickle", 'ab') as f:
    pickle.dump(database, f)
