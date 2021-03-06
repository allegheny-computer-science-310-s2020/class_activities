# USAGE
# ** Locally Installed OpenCV: from `src` directory:
# python recognize.py --training images/training --testing images/testing
# ** Docker Container: from a5_LBP:
# docker run --rm -v $(pwd)/src:/root opencv python recognize.py --training images/training --testing images/testing

# ref: https://www.pyimagesearch.com/2015/12/07/local-binary-patterns-with-python-opencv/


# import the necessary packages
from pyimagesearch.localbinarypatterns import LocalBinaryPatterns
from sklearn.svm import LinearSVC
from imutils import paths
import argparse
import cv2
import os

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-t", "--training", required=True,
                help="path to the training images")
ap.add_argument("-e", "--testing", required=True,
                help="path to the tesitng images")
args = vars(ap.parse_args())

# initialize the local binary patterns descriptor along with
# the data and label lists
desc = LocalBinaryPatterns(24, 8)
data = []
labels = []

# loop over the training images
for imagePath in paths.list_images(args["training"]):
    # load the image, convert it to grayscale, and describe it
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist = desc.describe(gray)

    # extract the label from the image path, then update label and data lists
    labels.append(imagePath.split(os.path.sep)[-2])
    data.append(hist)

# train a Linear SVM on the data
# https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html
model = LinearSVC(C=100.0, random_state=42, dual=False)
model.fit(data, labels)

# loop over the testing images
for imagePath in paths.list_images(args["testing"]):
    # load the image, convert it to grayscale, describe it, and classify it
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist = desc.describe(gray)
    prediction = model.predict(hist.reshape(1, -1))

    # display the image and the prediction
    cv2.putText(image, prediction[0], (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                1.0, (0, 0, 255), 3)
    cv2.imwrite("Image.png", image)
    cv2.waitKey(0)
