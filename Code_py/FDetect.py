import cv2 as cv
import numpy as np
import time
import os

img = cv.VideoCapture(0)
if not img.isOpened():
    print("Error: Could not open video.")
    exit()
haar_cascade = cv.CascadeClassifier("C:\\Users\\produ\\Desktop\\CIJ\\Code_py\\haar_face.xml")
start_time = time.time()
frame_count = 0
#cv.imshow('Abhyansh', img)

output_folder = r'C:\Users\produ\Desktop\CIJ\python_only\OCVVP\frames'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    
while True:
    isTrue, frame = img.read()
    
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #cv.imshow('Gray_Scale', gray)
    
    faces_rect = haar_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=10)
    print(f'Number of faces found = {len(faces_rect)}')
    if len(faces_rect)>0:
        frame_filename = os.path.join(output_folder, f'Photoo{frame_count:03d}.jpg')
        cv.imwrite(frame_filename, frame)
        frame_count += 1

    for (x,y,w,h) in faces_rect:
        cv.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), thickness=2)
    cv.imshow('VID',frame)

    if frame_count==30:
        print('Frames reached')
        print(f"Frames saved in folder: {output_folder}")
        break

    elif time.time() - start_time > 10:
        print('Time limit reached')
        break
    
    elif cv.waitKey(1) & 0xFF==ord('q'):
        break
    
img.release()
cv.destroyAllWindows()

#cv.imshow('Detected Faces', img)
#cv.waitKey(0)'''
