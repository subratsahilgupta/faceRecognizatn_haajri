import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime
import os

video_capture = cv2.VideoCapture(0)

face_encodingsDatabase =[]
face_namesDatabase = []

with open("imgPath.txt", "r") as f:
    for line in f:

        add = line.strip()
        capData = face_recognition.load_image_file(fr"{add}")
        capData_encoding = face_recognition.face_encodings(capData)[0]
        
        # filename = os.path.basename(add)
        filename, file_extension = os.path.splitext(os.path.basename(add))
        
        face_encodingsDatabase.append(capData_encoding)
        face_namesDatabase.append(filename)

#list of expected students
studExpected = face_namesDatabase.copy()

face_locations = []
face_encodings = []

# get current date 
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

f = open(f"{current_date}.csv", "w", newline = "")
lnwriter = csv.writer(f)

while True:
    _, frame = video_capture.read()
    small_frame = cv2.resize(frame,(0,0),fx = 0.25, fy = 0.25)
    rgb_small_frame = cv2.cvtColor(small_frame,cv2.COLOR_BGR2RGB)
    
    # Recognize face
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
    
    for face_encoding in face_encodings:

        #checking if a single face_encoding is present in the known face encoding and returns True/False
        matches = face_recognition.compare_faces(face_encodingsDatabase,face_encoding)

        #Given a list of face encodings, compare them to a known face encoding and get a euclidean distance for each comparison face. 
        face_distance = face_recognition.face_distance(face_encodingsDatabase,face_encoding)

        #Get the best matched face
        best_match_index = np.argmin(face_distance)

        #Checking if the matched face actually exists in the database or not
        if(matches[best_match_index]):
            name = face_namesDatabase[best_match_index]

        #Return  confirmation if person is present
        if name in face_namesDatabase:
            font = cv2.FONT_HERSHEY_SIMPLEX
            bottomLeftCornerOfText =(10,100)
            fontScale = 1.5
            fontColor = (255,0,0)
            thickness = 3
            lineType = 2
            cv2.putText(frame, name + " Present", bottomLeftCornerOfText, font, fontScale, fontColor,thickness, lineType)
            
            #To prevent data redundancy
            if name in studExpected:
                studExpected.remove(name)
                # get current time
                current_time = now.strftime("%H-%M-%S")
                lnwriter.writerow([name, current_time])


    cv2.imshow("Attendence", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


video_capture.release()
cv2.destroyAllWindows()
f.close()

