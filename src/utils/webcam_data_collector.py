import time
import os
import sys
import cv2

mod_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(mod_path)

from src.config.gaze_config import data_dir

'''
This python file collects unlabeled real gaze images using the webcamera.
'''

# Dataset parameters
DATASET_NAME = '070118_real'
NUM_IMAGES = 10

# Create local data dir
dataset_dir = os.path.join(data_dir, DATASET_NAME)
if not os.path.exists(dataset_dir):
    os.mkdir(dataset_dir)

for i in range(NUM_IMAGES):
    print('Taking image %s out of %s' % (i, NUM_IMAGES))
    # Set up video capture device on webcam
    webcam = cv2.VideoCapture(0)
    # Countdown on target gaze location
    time.sleep(1)
    # Snap image from webcamera
    snap = webcam.grab()
    ret, frame = webcam.retrieve()
    # # Show image
    # cv2.imshow('Video', frame)
    # cv2.waitKey()
    # Save image
    filename = '%s.jpg' % i
    cv2.imwrite(os.path.join(dataset_dir, filename), frame)
    # Delete camera object to reset buffer
    del webcam