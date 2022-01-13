from datetime import datetime
from PIL import ImageGrab  # PIL shortform of Pillow
import numpy as np
import cv2                 # cv2 shotform of opencv
from tkinter import *      # to get screen width and height
import datetime

width = Tk().winfo_screenwidth()
height = Tk().winfo_screenheight()

time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %I-%M-%S')  #I=1-12 H=0-24  dynamic file name
# print(time_stamp)

file_name = f'{time_stamp}.mp4' 

fourcc = cv2.VideoWriter_fourcc('m','p','4','v')    # Encoding, specify the video codec
captured_video = cv2.VideoWriter(file_name,fourcc,20.0,(width,height)) 

# print(width,height)

while True:
    img = ImageGrab.grab(bbox=(0,0,width,height))           # which part of screen u need to capture
    img_np = np.array(img)                              # stores the array for the captured image
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB) 
    cv2.imshow('capture window', img_final)             # pop up window which shows whats recording
    captured_video.write(img_final)                     # create a video from images

    if cv2.waitKey(10) == ord('q'):                                     # wait
        break