from PIL import Image
import cv2

i = 0
j = 1
diffsP = 0
diffsN = 0
threshold = 2500
counts = 0
while True:
    i = i + 1
    file1 = 'dataset/997/frame%04d.jpg' % i
    file2 = 'dataset/997/frame%04d.jpg' % (i + 1)
    try:
        i1 = Image.open(file1)
        i2 = Image.open(file2)
    except:
        break
    assert i1.mode == i2.mode, "Different kinds of images."
    # assert i1.size == i2.size, "Different sizes."

    pairs = zip(i1.getdata(), i2.getdata())
    if len(i1.getbands()) == 1:
        # for gray-scale jpegs
        dif = sum(abs(p1 - p2) for p1, p2 in pairs)
    else:
        dif = sum(abs(c1 - c2) for p1, p2 in pairs for c1, c2 in zip(p1, p2))

    ncomponents = i1.size[0] * i1.size[1] * 3

    diffsN = (dif / 255.0 * 10000000) / ncomponents
    img = cv2.imread(file2)
    img = cv2.resize(img, (int(img.shape[1] / 2), int(img.shape[0] / 2)))
    cv2.imshow('frames', img)
    cv2.waitKey(1)

    if abs(diffsN - diffsP) > threshold:
        counts = counts + 1
        print("Difference (", j, i, "):", diffsN, "difference",counts)
        diffsP = diffsN
        cv2.imshow('keyframes', img)
        cv2.waitKey(1)
        j = i
    else:
        print("Difference (", i, i + 1, "):", diffsN)
    # print("Difference (", i, i + 1, "):", dif/255.0, ncomponents)

cv2.destroyAllWindows()
