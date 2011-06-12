#!/usr/bin/python

# face_detect.py

# Face Detection using OpenCV. Based on sample code from:
# http://python.pastebin.com/m76db1d6b

# Usage: python face_detect.py <image_file>

# REQUIREMENTS:
# python-opencv
# opencv-docs
# libc-dev
# imagemagick

import sys, os
from opencv.cv import *
from opencv.highgui import *
import Image
import re

def detectObjects(image):
  """Converts an image to grayscale and prints the locations of any 
     faces found"""
  grayscale = cvCreateImage(cvSize(image.width, image.height), 8, 1)
  cvCvtColor(image, grayscale, CV_BGR2GRAY)

  storage = cvCreateMemStorage(0)
  cvClearMemStorage(storage)
  cvEqualizeHist(grayscale, grayscale)
  cascade = cvLoadHaarClassifierCascade(
    'haarcascade_frontalface_default.xml',
    #'/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml',
    cvSize(1,1))
  faces = cvHaarDetectObjects(grayscale, cascade, storage, 1.2, 2,
                             CV_HAAR_DO_CANNY_PRUNING, cvSize(50,50))

  if faces.total > 0:
    for f in faces:
      return ("[(%d,%d) -> (%d,%d)]" % (f.x, f.y, f.x+f.width, f.y+f.height))
      #print("[(%d,%d) -> (%d,%d)]" % (f.x, f.y, f.x+f.width, f.y+f.height))

def main():
  im = cvLoadImage(sys.argv[1]);
  coords = detectObjects(im)
  co = re.split('\D+', coords)
  #image.crop(tuple(co))
  toCrop = Image.open(sys.argv[1])
  im2 = toCrop.crop((int(co[1]),int(co[2]),int(co[3]),int(co[4])))
  im2.save(sys.argv[2])
  #for i in range(1,5):
#	print co[i]


if __name__ == "__main__":
  main()
