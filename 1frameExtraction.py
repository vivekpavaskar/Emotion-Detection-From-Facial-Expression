# script for frame extraction from video
import cv2
import os
from datetime import datetime as dt

# creating timestamp based directory in dataset
dates = dt.now().strftime("%Y%m%d%H%M%S")
directory = 'dataset/' + str(dates)
if not os.path.exists(directory):
    os.makedirs(directory)

# keep a video file with name video.mp4
path = 'videos/video5.mp4'
# storing video data into variable
videoData = cv2.VideoCapture(path)
# used as counter variable
count = 1
# checks whether frames were extracted
success = 1

while success:
    # videoData object calls read
    success, image = videoData.read()
    # Saves the frames with frame-count
    if success:
        image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(directory + "/frame%04d.jpg" % count, image)
        print(count)
        count += 1
