# python ball_detection.py --video video/janyl.mov
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_template_matching/py_template_matching.html
# https://medium.com/analytics-vidhya/finding-waldo-feature-matching-for-opencv-9bded7f5ab10
import argparse
from collections import deque
import cv2
import imutils
import numpy as np

img_rgb = cv2.imread('image1.jpeg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('ball1.png', 0)
# saves the width and height of the template into 'w' and 'h'
w, h = template.shape[::-1]
res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
# finding the values where it exceeds the threshold
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):
    # draw rectangle on places where it exceeds threshold
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)
cv2.imshow('found ball', img_rgb)

cv2.waitKey(0)

'''
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=64, help="max buffer size")
args = vars(ap.parse_args())

video = cv2.VideoCapture(args["video"])

# white range
lower_white = np.array([0, 0, 0])
upper_white = np.array([0, 0, 255])
pts = deque(maxlen=args["buffer"])

template = cv2.imread('ball.jpeg')

# keep looping
while True:
    # grab the current frame
    (grabbed, frame) = video.read()

    # if we are viewing a video and we did not grab a
    # frame, then we have reached the end of the video
    if args.get("video") and not grabbed:
        break

    # resize the frame, blur it, and convert it to the HSV
    # color space
    # frame = imutils.resize(frame, width=600)
    # blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    # hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # result of template matching of object over an image
    result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF)
    sin_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    top_left = max_loc

    # increasing the size of bounding rectangle by 50 pixels
    bottom_right = (top_left[0]+50, top_left[1]+50)
    cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 5)

    cv2.imshow('object found', frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# release the camera
video.release()

# close all windows
cv2.destroyAllWindows()
'''
