# USAGE
# python classify.py --images dataset/images --masks dataset/masks

# import the necessary packages
from __future__ import print_function
from pyimagesearch.rgbhistogram import RGBHistogram
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import numpy as np
import argparse
import glob
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required=True,
                help="path to the image dataset")
ap.add_argument("-m", "--masks", required=True,
                help="path to the image masks")
args = vars(ap.parse_args())

# grab the image and mask paths
imagePaths = sorted(glob.glob(args["images"] + "/*.png"))
maskPaths = sorted(glob.glob(args["masks"] + "/*.png"))

# initialize the list of data and class label targets
data = []
target = []

# initialize the image descriptor
desc = RGBHistogram([8, 8, 8])

# loop over the image and mask paths
for (imagePath, maskPath) in zip(imagePaths, maskPaths):
    # load the image and mask
    image = cv2.imread(imagePath)
    mask = cv2.imread(maskPath)
    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

    # describe the image
    features = desc.describe(image, mask)

    # update the list of data and targets
    data.append(features)
    target.append(imagePath.split("_")[-2])

# grab the unique target names and encode the labels
targetNames = np.unique(target)
le = LabelEncoder()
target = le.fit_transform(target)

# TODO: construct the training and testing splits

# TODO: train the classifier

# TODO: evaluate the classifier

# TODO: testing loop
