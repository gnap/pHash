import Image
import os, sys
import binhex, binascii

im = Image.open("portal2.jpg")
print im.format, im.size, im.mode
imlarger = im.copy();
im = im.resize((8, 8))
imlarger = imlarger.resize((32,32))
im = im.convert("L")
imlarger = imlarger.convert("L")
print im.format, im.size, im.mode
im.save("foo.jpg")
imlarger.save("foo2.jpg")

# find the average value
def average(image):
	count = 0
	pix = image.load()
	for i in range(0,8):
		for j in range(0,8):
			count += pix[i, j]
	count /= 64
	print count

# computes the hamming distance
def hamming_distance(s1, s2):
	assert len(s1) == len(s2)
	return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

# compute the bits from the average
def compute(image, av):
	testString = ""
	for i in range(0,8):
		for j in range(0,8):
			pix = image.load()
			if(pix[i, j] >= av):
				pix[i, j] = 1
			else:
				pix[i, j] = 0
			testString += `pix[i, j]`
	print "This is the test string: " + testString
#	print binascii.b2a_hex(testString)


# printing things out
print compute(im, average(im))
print hamming_distance("toned", "roses")
print hamming_distance("1011101", "1001001")
print hamming_distance("2173896", "2233796")
