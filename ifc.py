import cv2
import numpy as np
import statistics

prev_frame = np.zeros((1080,1920,3), dtype = np.uint8)

round0 = 1

#put path to video below. might need to  reset datype based on video. check frame.dtype()
cap = cv2.VideoCapture('Backend-Demo.mp4') 
# ctr = 0
maximumFrame = 0
sumArray = []
correlationArray = []
while(cap.isOpened()):
	print(".")
	if round0 == 0:
		prev_frame = frame
	ret, frame = cap.read()
	if frame is None:
		break
	array_a = np.ndarray.flatten(frame)
	array_b = np.ndarray.flatten(prev_frame)
	corr = np.correlate(array_a, array_b)[0]
	# print("Correlation: ",corr)
	diff = cv2.absdiff(frame, prev_frame)
	sumPixelArray = cv2.sumElems(diff)
	# print("Prev Frame:",prev_frame)
	# print("New Frame", frame)
	# print("Diff",diff)
	frameSum = cv2.sumElems(sumPixelArray)[0]
	sumArray.append(frameSum)
	if frameSum > maximumFrame:
		maximumFrame = frameSum 
	correlationArray.append(corr)
	color = cv2.cvtColor(frame, 0)
	# cv2.imshow('frame diff ',diff)    
	# cv2.imshow('frame',color)
	round0 = 0
	# ctr+=1
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
print("Minimum correlation = ", min(correlationArray))
print("Maximum correlation = ", max(correlationArray))
print("Correlation average = ", statistics.mean(correlationArray))
print("Mean of sum arrays: = ", statistics.mean(sumArray))

#put check condition based on the specific video that we will run for a certain amount of time


cap.release()
cv2.destroyAllWindows()