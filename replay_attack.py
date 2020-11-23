import numpy

stored_frames = []

""" replay_attack """
def replay_attack(numFrames, frame):

	# 1. store current frame
	stored_frames.append(frame)

	# 2. run stored frames in a while loop
	if len(stored_frames) == numFrames:
		# return old frame
		return_frame = stored_frames[0]
		stored_frames.pop(0)
		return return_frame

	return frame

