import cv2
import face_recognition
import os
import glob
import numpy as np
import time

# load sample and convert to encodiings
haar_cascade = cv2.CascadeClassifier(r"C:\Users\produ\Desktop\Face_Recog\FRmodules\haar_face.xml")
boolean = False

class SimpleFacerec:
    def __init__(self):
        self.known_face_encodings = []
        self.known_face_names = []

        # Resize frame for a faster speed
        self.frame_resizing = 0.25

    def load_encoding_images(self, images_path):
        # Load Images
        images_path = glob.glob(os.path.join(images_path, "*.*"))

        print("{} encoding images found.".format(len(images_path)))

        # Store image encoding and names
        for img_path in images_path:
            img = cv2.imread(img_path)
            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # Get the filename only from the initial file path.
            basename = os.path.basename(img_path)
            (filename, ext) = os.path.splitext(basename)
            # Get encoding
            img_encoding = face_recognition.face_encodings(rgb_img)[0]

            # Store file name and file encoding
            self.known_face_encodings.append(img_encoding)
            self.known_face_names.append(filename)
        print("Encoding images loaded")

    def detect_known_faces(self, frame):
        small_frame = cv2.resize(frame, (0, 0), fx=self.frame_resizing, fy=self.frame_resizing)
        # Find all the faces and face encodings in the current frame of video
        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
            name = "Unknown"

            

            # use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = self.known_face_names[best_match_index]
            face_names.append(name)

        # Convert to numpy array to adjust coordinates with frame resizing quickly
        face_locations = np.array(face_locations)
        face_locations = face_locations / self.frame_resizing
        return face_locations.astype(int), face_names


tryy=SimpleFacerec()
tryy.load_encoding_images('C:\\Users\\produ\\Desktop\\Face_Recog\\SampleCapture')
cptured=[]
result=[]
start_time=time.time()
capture=cv2.VideoCapture(0)

while True:
    cv2.waitKey(100)
    istrue, frame=capture.read()
    if not istrue:
        break
    faces_rect = haar_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=9)
    cptured.append(faces_rect)

    result.append([tryy.detect_known_faces(frame)])
    if len(cptured)>5 or time.time()-start_time>6:
        print(len(result))
        break

if len(result)>3:
    boolean=True
    #print(boolean)
