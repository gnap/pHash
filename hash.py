import Image
import os, sys

im = Image.open("portal.jpg")
print im.format, im.size, im.mode
