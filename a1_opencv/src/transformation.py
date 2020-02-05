# USAGE
# python transformation.py --image images/trex.png
# docker run --rm -v $(pwd)/src:/root opencv python transformation.py --image images/trex.png

# Import the necessary packages
import numpy as np
import argparse
import imutils
import cv2

# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# Load the image and show it
image = cv2.imread(args["image"])
cv2.imwrite("images/transformation/Original.png", image)

'''The first method we are going to explore is translation.
Translation is the shifting of an image along the x and y
axis. Using translation, we can shift an image up, down,
left, or right, along with any combination of the above!'''

# NOTE: Translating (shifting) an image is given by a
# NumPy matrix in the form:
# [[1, 0, shiftX], [0, 1, shiftY]]
# You simply need to specify how many pixels you want
# to shift the image in the X and Y direction.
# Let's translate the image 25 pixels to the right and
# 50 pixels down
M = np.float32([[1, 0, 25], [0, 1, 50]])
'''Now that we have our translation matrix defined, the
actual translation takes place on Line 15 using the cv2.
warpAffine function. The first argument is the image we
wish to shift and the second argument is our translation ma-
trix M. Finally, we manually supply the dimensions (width
and height) of our image as the third argument.'''
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imwrite("images/transformation/ShiftedDR.png", shifted)

# Now, let's shift the image 50 pixels to the left and
# 90 pixels up. We accomplish this using negative values
M = np.float32([[1, 0, -50], [0, 1, -90]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imwrite("images/transformation/ShiftedUL.png", shifted)

# Finally, let's use our helper function in imutils.py to
# shift the image down 100 pixels
'''imutils.py. This file will store basic
image processing methods, allowing us to conveniently
call them without writing a lot of code.'''
shifted = imutils.translate(image, 0, 100)
cv2.imwrite("images/transformation/ShiftedD.png", shifted)

# cv2.imshow("ShiftedD", shifted)
# cv2.waitKey(0)

# cv2.destroyAllWindows()

'''Rotation: rotating an image by some angle x.
 angle x to represent by how many degrees
we are rotating the image. '''

# Let's use our helper function in imutils.py to
# rotate the image by 180 degrees (flipping it upside down)
rotated = imutils.rotate(image, 180)
cv2.imwrite("images/transformation/Rotated.png", rotated)

'''Perhaps, not surprisingly, we will be using the cv2.resize
function to resize our images. But we need to keep in mind
the aspect ratio of the image when we are using this func-
tion.'''
# Of course, calculating the ratio each and every time we
# want to resize an image is a real pain. Let's create a
# function where we can specify our target width or height,
# and have it take care of the rest for us.
resized = imutils.resize(image, width=100)
cv2.imwrite("images/transformation/Resized.png", resized)

'''We can flip an image around either the x or
y axis, or even both.
The cv2.flip method requires two arguments: 1) the image we want to flip and
2) a flip code that is used to determine how we are going to flip
the image. Using a flip code value of 1 indicates that we are going
to flip the image horizontally, around the y-axis.
Specifying a flip code of 0 indicates that we want to flip the
image vertically, around the x-axis. Finally, using
a negative flip code flips the image around both axes.'''
# Flip the image horizontally
flipped = cv2.flip(image, 1)
cv2.imwrite("images/transformation/FlippedH.png", flipped)

# Flip the image vertically
flipped = cv2.flip(image, 0)
cv2.imwrite("images/transformation/FlippedV.png", flipped)

# Flip the image along both axes
flipped = cv2.flip(image, -1)
cv2.imwrite("images/transformation/FlippedHV.png", flipped)

'''When we crop an image, we want to remove the outer parts
of the image that we are not interested in. We can accom-
plish image cropping by using NumPy array slicing.'''
# Cropping an image is as simple as using array slices
# in NumPy! Let's crop out the face of the T-Rex. The
# order in which we specify the coordinates is:
# startY:endY, startX:endX
# In this case, we are starting at Y=30 and ending at
# Y=120. Similarly, we start at X=240 and X=335.
cropped = image[30:120, 240:335]
cv2.imwrite("images/transformation/Face.png", cropped)
