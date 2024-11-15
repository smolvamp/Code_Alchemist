import numpy as np
import cv2 as cv
import time

haar_cascade = cv.CascadeClassifier("C:\\Users\\produ\\Desktop\\CIJ\\Code_py\\haar_face.xml")

people = ['frames']
confi=[]
boolean=False

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read(r'C:\Users\produ\Desktop\CIJ\python_only\face_trained.yml')

capture = cv.VideoCapture(0)

frame_count = 0
start_time = time.time()
while True:
    ret, frame = capture.read()
    if not ret:
        break
    
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces_rect:
        faces_roi = gray[y:y+h, x:x+w]

        label, confidence = face_recognizer.predict(faces_roi)
        print(f'Label = {people[label]} with a confidence of {confidence:02f}')
        confi.append(confidence)

        #cv.putText(frame, str(people[label]), (x, y - 10), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness=2)
        #cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

    #cv.imshow('Detected Face', frame)

    frame_count += 1
    if frame_count >= 20:# Stop after 60 frames with detected faces
        avg=sum(confi)/len(confi)
        print(avg)
        break

    if time.time()-start_time>5:
        print('time limit reached')
        break

    #time.sleep(0.08)  # Wait for 0.2 seconds before capturing the next frame
if avg>30:
    boolean=True
capture.release()
cv.destroyAllWindows()


