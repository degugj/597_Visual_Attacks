import cv2
import numpy as np
import statistics
#put path to video below. might need to  reset datype based on video. check frame.dtype()

maxlength = 500
maxbreadth = 500
boxPixel = [34,139,34]
framectr = 0
correlationArray = []

round0 = 1

prev_frame = np.zeros((1080,1920,3), dtype = np.uint8)

cap = cv2.VideoCapture('Backend-Demo.mp4') 


while(cap.isOpened()):
	ret, frame = cap.read()
	if frame is None:
		break
	if round0 == 0:
		prev_frame = frame
	array_a = np.ndarray.flatten(frame)
	array_b = np.ndarray.flatten(prev_frame)
	corr = np.correlate(array_a, array_b)[0]
	correlationArray.append(corr)	
	ctr = 0
	framectr += 1
	if framectr > maxbreadth:
		framectr = maxbreadth
	while ctr <= framectr:
		for i in range(maxlength):
			frame[i][ctr] = boxPixel
		ctr+=1

	color = cv2.cvtColor(frame, 0)
	# cv2.imshow('frame diff ',diff)    
	cv2.imshow('frame',color)
	round0 = 0
	# ctr+=1
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

print("Minimum correlation = ", min(correlationArray))
print("Maximum correlation = ", max(correlationArray))
print("Correlation average = ", statistics.mean(correlationArray))

cap.release()
cv2.destroyAllWindows()