# Testing DCTs

import Image, cv
import os, sys
import numpy
from opencv.cv import *

def PIL2array(img):
	return numpy.array(img.getdata(),numpy.uint8).reshape(img.size[1],img.size[0], 1)

def array2PIL(arr, size):
	#mode = 'RGBA'
	mode = 'L'
	arr = arr.reshape(arr.shape[0]*arr.shape[1], arr.shape[2])
	if len(arr[0]) == 3:
		arr = numpy.c_[arr, 255*numpy.ones((len(arr),1), numpy.uint8)]
	return Image.frombuffer(mode, size, arr.tostring(), 'raw', mode, 0, 1)

def main():
	img = Image.open(sys.argv[1])
	img = img.resize((32,32))
	img = img.convert("L")
	arr = PIL2array(img)
	src = cv.CreateMat(32, 32, CV_32FC1)
	dst = cv.CreateMat(32, 32, CV_32FC1)
	cv.DCT(src, dst, CV_DXT_FORWARD)
	img2 = array2PIL(dst.tostring(), img.size)
	#img2 = array2PIL(arr, img.size)
	img2.save('out.jpg')

if __name__ == '__main__':
	main()


#cv_im = cv.CreateImageHeader(im.size, cv.IPL_DEPTH_8U, 1)
#cv_im_dst = cv.CreateImageHeader(im.size, cv.IPL_DEPTH_8U, 1)
#cv.SetData(cv_im, im.tostring())
#cv.DCT(cv_im, cv_im_dst, CV_DXT_FORWARD)
#print im.size, cv.GetSize(cv_im)
#print im.tostring() == cv_im.tostring()
