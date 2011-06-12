import Image
import os, sys

# find the average value
def average(image):
	count = 0
	pix = image.load()
	for i in range(0,8):
		for j in range(0,8):
			count += pix[i, j]
	val = count / 64
	print "Total:\t\t%d" % count
	print "Average:\t%d" % val
	return val

# find the DCT value
def dct(image):
	mean = average(image)	
	compute(image, mean, 32)
	print "Average:\t%d" % mean

# compute the hash
def compute(image, av, size):
	testString = ""
	for i in range(0,size):
		for j in range(0,size):
			pix = image.load()
			if(pix[i, j] >= av):
				pix[i, j] = 1
			else:
				pix[i, j] = 0
			testString += `pix[i, j]`
	print "testString:\t" + testString
	encoded = "%x" % int(testString,2)
	print "Hash:\t\t" + encoded + "\n"
	
# computes the hamming distance
def hamming_distance(s1, s2):
	assert len(s1) == len(s2)
	return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

# printing things out
def main():
	im = Image.open(sys.argv[1])
	im = im.resize((32, 32))
	im = im.convert("L")
	print "\nResolution:\t%s" % (im.size,)
	print "Mode:\t\t" + im.mode
	im.save("output.jpg")
	avVal = average(im)
	compute(im, avVal, 8)
	#dct(im)

if __name__ == "__main__":
	main()
