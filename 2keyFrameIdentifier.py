from PIL import Image
import cv2

i = 0
j = 1
img = None
diffsP = 0
diffsN = 0
# threshold values: static-2500 mobile-4000
threshold = 2500
counts = 0
i = i + 1
file = 'dataset/5/frame%04d.jpg' % i
try:
    i2 = Image.open(file)
except:
    pass

while True:
    try:
        i1 = i2
        i = i + 1
        file = 'dataset/5/frame%04d.jpg' % i
        i2 = Image.open(file)
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
    imgp = img
    img = cv2.imread(file)
    img = cv2.resize(img, (int(img.shape[1] / 2), int(img.shape[0] / 2)))
    cv2.imshow('frames', img)
    cv2.waitKey(1)
    if abs(diffsN - diffsP) > threshold:
        counts = counts + 1
        print("Difference (", j, i, "):", diffsN, "difference", counts)
        diffsP = diffsN
        cv2.imshow('keyframes', img)
        cv2.waitKey(1)
        j = i
    else:
        print("Difference (", j, i, "):", diffsN)

cv2.destroyAllWindows()
