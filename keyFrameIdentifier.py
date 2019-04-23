from PIL import Image
import os
import cv2


def filterKeyFrame(folder):
    dates = folder
    directoryKF = 'dataset/keyFrames/' + dates
    if not os.path.exists(directoryKF):
        os.makedirs(directoryKF)
    i = 1
    j = 1
    k = 1
    img = None
    diffsP = 0
    diffsN = 0
    # threshold values: static-2500 mobile-4000
    threshold = 4000
    counts = 0

    frames = 'dataset/frames/' + dates + '/frame%04d.jpg' % i
    keyFrames = 'dataset/keyFrames/' + dates + '/frame%04d.jpg' % k

    try:
        i2 = Image.open(frames)
        i1 = i2
        imgp = cv2.imread(frames)
        cv2.imwrite(keyFrames, imgp)
    except:
        pass

    while True:
        try:
            i = i + 1
            frames = 'dataset/frames/' + dates + '/frame%04d.jpg' % i
            i2 = Image.open(frames)
        except:
            break
        assert i1.mode == i2.mode, "Different kinds of images."
        assert i1.size == i2.size, "Different sizes."
        pairs = zip(i1.getdata(), i2.getdata())

        if len(i1.getbands()) == 1:
            # for gray-scale jpegs
            dif = sum(abs(p1 - p2) for p1, p2 in pairs)
        else:
            dif = sum(abs(c1 - c2) for p1, p2 in pairs for c1, c2 in zip(p1, p2))

        ncomponents = i1.size[0] * i1.size[1] * 3

        diffsN = (dif / 255.0 * 10000000) / ncomponents
        img = cv2.imread(frames)
        imgResize = cv2.resize(img, (int(img.shape[1] / 2), int(img.shape[0] / 2)))
        # imgResize = cv2.resize(img, (100,100))
        # imgResize = cv2.resize(img, (600,600))
        # cv2.imshow('frames', imgResize)
        # cv2.waitKey(1)
        diffValue = abs(diffsN - diffsP)
        if diffValue > threshold:
            counts = counts + 1
            # print("Difference (", j, i, "):", diffValue, "difference", counts)
            diffsP = diffsN
            # cv2.imshow('keyframes', imgResize)
            # cv2.waitKey(1)
            j = i
            i1 = i2
            k = k + 1
            imgp = img
            keyFrames = 'dataset/keyFrames/' + dates + '/frame%04d.jpg' % k
            cv2.imwrite(keyFrames, imgp)
        # else:
            # print("Difference (", j, i, "):", diffValue)

    # cv2.destroyAllWindows()
