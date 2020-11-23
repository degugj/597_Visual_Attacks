import numpy

stored_frames = []
replayIt = 0

""" replay_attack """
def replay_attack(numFrames, frame):
        if len(stored_frames) != numFrames:
                # store current frame
                stored_frames.append(frame)
                return frame
        else:
                global replayIt
                return_frame = stored_frames[replayIt]
                replayIt += 1
                if replayIt == numFrames:
                     replayIt = 0
                return return_frame

