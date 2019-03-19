# script to extract ROI
import cv2
import os


def roi(folder):
    dates = folder
    # initializing image variable
    img = None
    # creating face cascade opbject
    face_cascade = cv2.CascadeClassifier("haarcascad/12.xml")
    # input directory name (temporary)
    # dirName = input("Enter Dataset directory name: ")
    i = 0

    directoryROI = 'dataset/ROI/' + dates
    if not os.path.exists(directoryROI):
        os.makedirs(directoryROI)

    while True:
        i = i + 1
        # creating path for images
        # file = 'dataset/' + dirName + '/frame%04d.jpg' % i
        filein = 'dataset/keyFrames/' + dates + '/frame%04d.jpg' % i
        fileout = 'dataset/ROI/' + dates + '/frame%04d.jpg' % i
        print(filein)
        # reading the image file
        img = cv2.imread(filein, 0)
        # to handel bad imageshruti
        if img is None:
            break
        # getting ROI/face coordinates in image
        face = face_cascade.detectMultiScale(img, scaleFactor=1.05, minNeighbors=5)
        print(face)
        # cropping and storing the image
        for x, y, w, h in face:
            if w > 60 and h > 60:
                # img = cv2.rectangle(img, (x - 10, y - 20), (x + w + 5, y + h + 10), (0, 0, 255), 2)
                img = img[y - 20:y + h + 10, x - 10:x + w + 5]
                cv2.imwrite(fileout, img)

    cv2.destroyAllWindows()
