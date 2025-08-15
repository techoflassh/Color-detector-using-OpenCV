import math
import numpy as np

import cv2
import matplotlib.pyplot as plt

from tkinter import filedialog as fd

######
Optionimage = False
Optionvideo = True
######
mouseX, mouseY = 0, 0

rgbColorNameDict = {}
rgbToNameFile = open("./rgbToName.txt", "r")
for line in rgbToNameFile.readlines():
    line = line.replace("\n", "").split(":")
    rgbColorNameDict[line[0]] = line[1]


def rgbToName(rgbTuple):
    try:
        r, g, b = rgbTuple
        diffs = []
        for color in rgbColorNameDict:
            cr, cg, cb = (int(x) for x in color.split(","))
            diff = math.sqrt((abs(r - cr) ** 2 + abs(g - cg) ** 2 + abs(b - cb) ** 2))
            diffs.append((diff, color))
        name = rgbColorNameDict[min(diffs)[1]]
        return name
    except:
        return "Unable to get name"


def mousePos(event, x, y, flags, param):
    # print(x, y)
    global mouseX, mouseY
    mouseX, mouseY = x, y


def graphy(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    ploty = [0]*255

    hueList = image[:, :, 0].flatten()
    for i in range(255):
        # ploty[i] == np.count_nonzero(x == i)
        ploty[i] = np.count_nonzero(hueList == i)
    plotx = list(range(0, 255))
    print(len(hueList))
    print(hueList)
    # print(image)
    print(ploty)
    plt.plot(plotx, ploty)
    plt.show()


def hist(image):
    assert img is not None, "file could not be read, check with os.path.exists()"
    color = ('b', 'g', 'r')
    for i, col in enumerate(color):
        histr = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(histr, color=col)
        plt.xlim([0, 256])
    plt.show()


def hist2(image):
    plt.hist(img.ravel(), 256, [0, 256])
    plt.show()


inp = cv2.VideoCapture(0)
inp.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
inp.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)


# bug fix
img = cv2.imread('red.jpg', 1)
cv2.imshow("IMAGE COLOR ANALYZER", img)


while True:
    if Optionimage == True:
        frame = np.copy(img)

    # elif Optionvideo == True:
    if Optionvideo == True:
        _, frame = inp.read()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    height, width, _ = frame.shape

    cv2.setMouseCallback("IMAGE COLOR ANALYZER", mousePos)
    x = mouseX
    y = mouseY

    try:
        pixel = rgb_frame[y, x]
    except:
        pixel = (0, 0, 0)

    color = rgbToName(pixel)
    r, g, b = int(pixel[0]), int(pixel[1]), int(pixel[2])
    #######################################
    # show color name UI here
    if x + 10 + 185 >= width:
        x = x - 185 - 15
    if y + 10 + 115 >= height:
        y = y - 115 - 15
    # rectangle for color
    frame = cv2.rectangle(frame, (x+15, y+5), (x+185, y+115), (99, 99, 99), -1)
    frame = cv2.rectangle(frame, (x+15, y+5), (x+185, y+115), (9, 9, 9), 1)
    frame = cv2.rectangle(frame, (x+20, y+10), (x+180, y+50), (b, g, r), -1)
    frame = cv2.rectangle(frame, (x+20, y+10), (x+180, y+50), (9, 9, 9), 1)
    # rectangle for rgb value output
    frame = cv2.rectangle(frame, (x+20, y+60), (x+180, y+82), (30, 30, 30), -1)
    frame = cv2.rectangle(frame, (x+20, y+60), (x+180, y+82), (9, 9, 9), 1)
    # rectangle for name output
    frame = cv2.rectangle(frame, (x+20, y+87), (x+180, y+110), (30, 30, 30), -1)
    frame = cv2.rectangle(frame, (x+20, y+87), (x+180, y+110), (9, 9, 9), 1)

    rbginText = (f"RGB : ({r}, {g}, {b})")
    cv2.putText(frame, rbginText, (x+21, y+76), 1, 0.8, (255, 255, 255), 1)
    cv2.putText(frame, color, (x+15, y+103), 1, 0.8, (255, 255, 255), 1)

    cv2.imshow("IMAGE COLOR ANALYZER", frame)
    key = cv2.waitKey(30)
    if key == ord('G') or key == ord('g'):
        graphy(frame)
        hist(frame)
        # hist2(frame)

    if key == ord('I') or key == ord('i'):
        Optionimage = True
        Optionvideo = False

        filename = fd.askopenfilename()
        img = cv2.imread(filename)

    if key == ord('V') or key == ord('v'):
        Optionimage = False
        Optionvideo = True
    if key == ord(' ') or key == 27:
        break
inp.release()
cv2.destroyAllWindows()
