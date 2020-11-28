import time
import picamera
import numpy as np
import cv2

def color_verification(frame, color):
     # if color not in bottom left of frame, return -1 else return 0
     return 0

def interframe_correlation(prevFrame, currFrame):
	array_a = np.ndarray.flatten(currFrame)
	array_b = np.ndarray.flatten(prevFrame)
	correlation = np.correlate(array_a, array_b)[0]
	
	return correlation
