# USAGE
# python imageDisplay.py --image images/trex.png
# docker run --rm -v $(pwd)/src:/root opencv python imageDisplay.py --image images/trex.png

# Import the necessary packages
from __future__ import print_function
import argparse
import cv2

# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# Load the image and show some basic information on it
image = cv2.imread(args["image"])
print("height: {} pixels".format(image.shape[0]))
print("width: {} pixels".format(image.shape[1]))
print("channels: {}".format(image.shape[2]))

# Show the image and wait for a keypress
# cv2.imshow("Original Image", image)
# cv2.waitKey(0)

# Save the image -- OpenCV handles converting filetypes
# automatically
cv2.imwrite("images/display/newimage.jpg", image)

(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

image[0, 0] = (0, 0, 255)
(b, g, r) = image[0, 0]
cv2.imwrite("images/display/next_image.png", image)
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

corner = image[0:100, 0:100]
cv2.imwrite("images/display/Corner.png", corner)

image[0:100, 0:100] = (0, 255, 0)
cv2.imwrite("images/display/Updated.png", image)
