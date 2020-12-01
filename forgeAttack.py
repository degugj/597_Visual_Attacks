import cv2
import numpy as np
import statistics
#put path to video below. might need to  reset datype based on video. check frame.dtype()

maxlength = 100
maxbreadth = 100
boxPixel = [50,50,50]
framectr = 0
correlationArray = []

round0 = 1

prev_frame = np.zeros((320,240,3), dtype = np.uint8)

cap = cv2.VideoCapture('RWBoutput_true2020-11-30 03 52 02.163626.avi') 


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
#to get rid of the first correlation value as it is meaningless
correlationArray.pop(0)

results = list(map(int, correlationArray))
stdev = statistics.stdev(results)
mean = statistics.mean(correlationArray)

print("Minimum correlation = ", min(correlationArray))
print("Maximum correlation = ", max(correlationArray))
print("Correlation average = ", mean)
print("Standard Deviation = ", stdev)
print("Approximate IFC value: = ", mean - stdev)


cap.release()
cv2.destroyAllWindows()