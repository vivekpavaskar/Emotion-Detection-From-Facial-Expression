import cv2
import numpy as np

i = 1
img1 = cv2.imread('dataset/shruti/frame%04d.jpg' % i)

while True:
    try:
        i = i + 1
        img2 = cv2.imread('dataset/shruti/frame%04d.jpg' % i)
        diff = cv2.absdiff(img1, img2)
        res = diff.astype(np.uint8)
        percentage = (np.count_nonzero(res) * 100) / res.size
        # if percentage > 82:
        cv2.imshow('diff', diff)
        cv2.waitKey(1)
        print(i, percentage)
        img1 = img2
    except:
        break

cv2.destroyAllWindows()
