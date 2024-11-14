import cv2
import os
import time

#capture = cv.VideoCapture(r'python_only\OCVVP\vid.mp4')
'''capture = cv.VideoCapture(0) # for camera usage
while True:
    isTrue, frame = capture.read(0)
    cv.imshow('Anime',frame)
    if cv.waitKey(0) & 0xff == ord('q'):
        break

capture.release()
cv.destroyAllWindows()'''

#import cv2
#import os
#import time


capture = cv2.VideoCapture(0)

if not capture.isOpened():
    print("Error: Could not open video.")
    exit()

output_folder = r'C:\Users\produ\Desktop\CIJ\python_only\OCVVP\frames'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

frame_count = 0
start_time = time.time()

while True:
    ret, frame = capture.read()
    cv2.imshow('Recording_Face',frame)

    if not ret:
        break
    
    frame_filename = os.path.join(output_folder, f'Photoo{frame_count:04d}.jpg')
    cv2.imwrite(frame_filename, frame)
    
    frame_count += 1
    
    if time.time() - start_time > 1.5:
        break

    elif cv2.waitKey(10) & 0xff == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()

print(f"Frames saved in folder: {output_folder}")
