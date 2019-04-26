# script for frame extraction from video
import cv2
import os


def extractFrames(path, dates):
    # initializing directory path
    directoryF = 'dataset/frames/' + dates
    if not os.path.exists(directoryF):
        os.makedirs(directoryF)

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
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(directoryF + "/frame%04d.jpg" % count, image)
            # start development
            # print(count)
            # end development
            count += 1

    return dates
