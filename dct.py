# Testing DCTs

import Image, cv
import os, sys
from opencv.cv import *

im = Image.open(sys.argv[1])
im = im.resize((32,32))
im = im.convert("L")



cv_im = cv.CreateImageHeader(im.size, cv.IPL_DEPTH_8U, 1)
cv.SetData(cv_im, im.tostring())
print im.size, cv.GetSize(cv_im)
print im.tostring() == cv_im.tostring()
