import cv2 as cv
import os
import time
import numpy as np
import tkinter as tk
from tkinter import Button, Label, Toplevel
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Face Register")
root.geometry("800x600")


img = None
frame_count = 0
start_time = 0
last_saved_time = 0
output_folder = r'C:\Users\produ\Desktop\CIJ\python_only\OCVVP\frames'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


capture = cv.VideoCapture(0)
haar_cascade = cv.CascadeClassifier("C:\\Users\\produ\\Desktop\\CIJ\\Code_py\\haar_face.xml")

def retry_capture():
    global img, frame_count, start_time, last_saved_time
    capture.open(0)
    frame_count = 0
    start_time = time.time()
    last_saved_time = time.time()
    capture_video()


def start_capture():
    global img, frame_count, start_time, last_saved_time
    frame_count = 0
    start_time = time.time()
    last_saved_time = time.time()
    capture_video()


def capture_video():
    global img, frame_count, start_time, last_saved_time
    ret, frame = capture.read()
    if not ret:
        return

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10)

    if len(faces_rect) > 0 and (time.time() - last_saved_time) > 0.1:
        frame_filename = os.path.join(output_folder, f'Photoo{frame_count:03d}.jpg')
        cv.imwrite(frame_filename, frame)
        frame_count += 1
        last_saved_time = time.time()

    for (x, y, w, h) in faces_rect:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

    
    img = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    img = ImageTk.PhotoImage(image=img)

    
    canvas.create_image(0, 0, anchor=tk.NW, image=img)

    
    if (time.time() - start_time) < 20 and frame_count < 60:
        root.after(10, capture_video)
    else:
        if frame_count < 60:
            show_failure_message()
        else:
            end_capture()

def end_capture():
    capture.release()
    cv.destroyAllWindows()
    root.quit()
    print('Capture complete')
    print(f"Frames saved in folder: {output_folder}")

def show_failure_message():
    failure_popup = Toplevel(root)
    failure_popup.title("Registration Failed")
    failure_popup.geometry("300x150")
    Label(failure_popup, text="Face registration failed.\nPlease try again.", pady=20).pack()

    retry_button = Button(failure_popup, text="Retry", command=lambda: [failure_popup.destroy(), retry_capture()])
    retry_button.pack(pady=20)

canvas = tk.Canvas(root, width=640, height=480)
canvas.pack()

start_button = Button(root, text="Start Capture", command=start_capture)
start_button.pack(side=tk.LEFT, padx=10, pady=10)

root.mainloop()
