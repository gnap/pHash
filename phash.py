#!/usr/bin/python
#
# Image Average Hashing + Hamming Distance
# Author: Justin Wong
#
# Usage:
# python hash.py <image1> <image2>

import Image, cv, os, sys, numpy
from opencv.cv import *

def PIL2array(img):
    return numpy.array(img.getdata(),numpy.uint8).reshape(img.size[1],img.size[0], 1)

def array2PIL(arr, size):
    mode = 'L'
    arr = arr.reshape(arr.shape[0]*arr.shape[1], arr.shape[2])
    if len(arr[0]) == 3:
        arr = numpy.c_[arr, 255*numpy.ones((len(arr),1), numpy.uint8)]
    return Image.frombuffer(mode, size, arr.tostring(), 'raw', mode, 0, 1)

# find the average value from the reduced DCT (low-freq vals)
def average(image):
	count = 0
	pix = image.load()
	for i in range(0,7):
		for j in range(0,7):
			count += pix[i, j]
	count -= pix[0, 0] #exclude first position since it varies greatly from rest of vals
	val = count / (8*8) 
	print "Total:\t\t%d" % count
	print "Average:\t%d" % val
	return val

# find the DCT value
def hashDct(img):
	arr = PIL2array(img)
	src = cv.CreateMat(32, 32, CV_32FC1)
	dst = cv.CreateMat(32, 32, CV_32FC1)
	cv.DCT(src, dst, CV_DXT_FORWARD)
	imgarray = numpy.asarray(dst)
	img2 = Image.fromarray(numpy.uint8(imgarray))
	return img2
	print "Average:\t%d"

# compute the hash
def compute(image, av, size):
	testString = ""
	for i in range(0,size):
		for j in range(0,size):
			pix = image.load()
			if(pix[i, j] >= av):
				val = 1
				#pix[i, j] = 1
			else:
				val = 0
				#pix[i, j] = 0
			testString += `val`
			#testString += `pix[i, j]`
	print "testString:\t" + testString
	encoded = "%x" % int(testString,2)
	print "Hash:\t\t" + encoded + "\n"
	return encoded
	
# computes the hamming distance
def hamming_distance(s1, s2):
	if len(s1) > len(s2):
		s2 = s2.zfill(len(s1))
	elif len(s2) > len(s1):
		s1 = s1.zfill(len(s2))
	assert len(s1) == len(s2)
	return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

# printing things out
def main():
	if len(sys.argv) <= 1 or len(sys.argv) > 3:
		print "Usage %s: <image1> <image2>" % sys.argv[0]
	# Image 1 hash
	im = Image.open(sys.argv[1])
	im = im.resize((32, 32))
	im = im.convert("L")
	hash1DCT = hashDct(im)
	hash1 = compute(hash1DCT, average(hash1DCT), 31)
	# Image 2 hash
	im2 = Image.open(sys.argv[2])
	im2 = im2.resize((32, 32))
	im2 = im2.convert("L")
	hash2DCT = hashDct(im2)
	hash2 = compute(hash2DCT, average(hash2DCT), 31)
	# Hamming Distance calculation
	print "-------------Hamming Distance-------------"
	print "Threshold = 26"
	result = hamming_distance(hash1, hash2)	
	if result < 26:
	  print "Hamming distance = %d. Images are similar." % result
	else:
	  print "Hamming distance = %d. Images are not similar" % result

if __name__ == "__main__":
	main()
