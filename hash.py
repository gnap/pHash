import Image
import os, sys

im = Image.open("portal2.jpg")
imlarger = im.copy();
im = im.resize((8, 8))
imlarger = imlarger.resize((32,32))
im = im.convert("L")
imlarger = imlarger.convert("L")
print "\nResolution:\t%s" % (im.size,)
print "Mode:\t\t" + im.mode
im.save("foo.jpg")
imlarger.save("foo2.jpg")

# find the average value
def average(image):
	count = 0
	pix = image.load()
	for i in range(0,8):
		for j in range(0,8):
			count += pix[i, j]
	after = count / 64
	print "Total:\t\t%d" % count
	print "Average:\t%d" % after
	return after

# computes the hamming distance
def hamming_distance(s1, s2):
	assert len(s1) == len(s2)
	return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

# compute the hash
def compute(image, av):
	testString = ""
	for i in range(0,8):
		for j in range(0,8):
			pix = image.load()
			#print "--------------"
			#print "(%d,%d): %d" % (i,j, pix[i,j])
			if(pix[i, j] >= av):
				pix[i, j] = 1
			else:
				pix[i, j] = 0
			testString += `pix[i, j]`
	print "testString:\t" + testString
	encoded = "%x" % int(testString,2)
	print "Hash:\t\t" + encoded + "\n"
	
# printing things out
avVal = average(im)
compute(im, avVal)
