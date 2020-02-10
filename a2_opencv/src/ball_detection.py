# from /src: python ball_detection.py
# from a2_opencv: docker run --rm -v $(pwd)/src:/root opencv python motion_detection.py

# ref: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_template_matching/py_template_matching.html
# ref: https://docs.opencv.org/2.4/doc/tutorials/imgproc/histograms/template_matching/template_matching.html

import cv2
import numpy as np

img_rgb = cv2.imread('images/image.jpeg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('images/ball.png', 0)
# saves the width and height of the template into 'w' and 'h'
w, h = template.shape[::-1]
res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
# finding the values where it exceeds the threshold
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):
    # draw rectangle on places where it exceeds threshold
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)
cv2.imwrite('images/output/found_ball.png', img_rgb)

cv2.waitKey(0)
