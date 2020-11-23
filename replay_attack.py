import numpy

stored_frames = []
counter = 0

""" replay_attack """
def replay_attack(numFrames, frame):

	if len(stored_frames) != numFrames:
		# store current frame
		stored_frames.append(frame)
		return frame

	else:
		return_frame = stored_frames[counter]
		if counter == numFrames:
			counter = 0
		counter += 1
		return return_frame

