# script for frame extraction from video
import cv2
import os



def extractFrames(path,dates):
    # dates = str(2)
    directoryF = 'dataset/frames/' + dates
    if not os.path.exists(directoryF):
        os.makedirs(directoryF)

    # keep a video file with name video.mp4
    # path = 'videos/videoshruti.mp4'
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
            # (h,w)=image.shape[:2]
            # center=(w/2,h/2)
            # rotated=cv2.getRotationMatrix2D(center,90,1.0)
            # rotated90=cv2.warpAffine(image,rotated,(w,h))
            cv2.imwrite(directoryF + "/frame%04d.jpg" % count, image)
            print(count)
            count += 1

    return dates
