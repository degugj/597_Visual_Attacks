import time
import picamera
import numpy as np
import cv2
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def blink_verification(numBlinks):
     # if color not in bottom left of frame, return -1 else return 0
	# Raspberry Pi pin configuration:
	RST = 24
	# 128x32 display with hardware I2C:
	disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)
	disp.begin()
	for i in range(numBlinks):

		# Create blank image for drawing.
		# Make sure to create image with mode '1' for 1-bit color.
		width = disp.width
		height = disp.height
		image = Image.new('1', (width, height))

		# Get drawing object to draw on image.
		draw = ImageDraw.Draw(image)

		# Draw a black filled box to clear the image.
		draw.rectangle((0,0,width,height), outline=0, fill=0)

		# Draw some shapes.
		# First define some constants to allow easy resizing of shapes.
		padding = 2
		shape_width = 20
		top = padding
		bottom = height-padding
		# Move left to right keeping track of the current x position for drawing shapes.
		x = padding
		# Draw a rectangle.
		draw.rectangle((0, 0, 124, 124), outline=255, fill=255)
		x += shape_width+padding
		draw.polygon([(x, bottom), (x+shape_width/2, top), (x+shape_width, bottom)], outline=255, fill=255)

		# Display image.
		disp.image(image)
		disp.display()
		time.sleep(.5)
		disp.clear()
		disp.display()
		time.sleep(.5)
	return 0

def interframe_correlation(prevFrame, currFrame):
	array_a = np.ndarray.flatten(currFrame)
	array_b = np.ndarray.flatten(prevFrame)
	correlation = np.correlate(array_a, array_b)[0]
	
	return correlation
