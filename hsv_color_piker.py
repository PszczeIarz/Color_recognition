import cv2
import numpy as np


def colorme(x):
    pass

#Trackbar

cv2.namedWindow("frame")
cv2.createTrackbar("H", "frame", 0, 179, colorme)
cv2.createTrackbar("S", "frame", 255, 255, colorme)
cv2.createTrackbar("V", "frame", 255, 255, colorme)