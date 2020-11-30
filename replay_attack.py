import numpy

stored_frames = []
replayIt = 0
numFrames = 0

indices = []
i = 0
for i in range(30*3,125*3,3):
    for j in range(120,180):
        indices.append(i+j*(320*3))
        indices.append(i+j*(320*3)+1)
        indices.append(i+j*(320*3)+2)

""" replay_attack """
def replay_attack(startFrame, endFrame, frame):
    global numFrames
    if numFrames != endFrame-1:
        # store current frame
        if numFrames >= startFrame-1:
            stored_frames.append(frame)
        numFrames+=1
        return frame
    else:
        global replayIt
        return_frame = stored_frames[replayIt]
        replayIt += 1
        if replayIt == endFrame-startFrame:
            replayIt = 0
        return return_frame

def selective_replay_attack(startFrame, endFrame, frame):
    global numFrames
    if numFrames != endFrame-1:
        # store current frame
        if numFrames >= startFrame-1:
            stored_frames.append(frame)
        numFrames+=1
        return frame
    else:
        global replayIt
        return_frame = numpy.empty((240, 320, 3), dtype=numpy.uint8)
        return_frame = stored_frames[replayIt].copy()
        #return_frame = numpy.zeros((240,320,3), dtype = numpy.uint8)
        replayIt += 1
        if replayIt == (endFrame-startFrame):
             replayIt = 0
        #for i in range(30,125):
        #    for j in range(120,180):
        #        return_frame[j][i] = frame[j][i].copy()
           
        displayPixels = numpy.take(frame, indices)
        numpy.put(return_frame, indices, displayPixels)
        
        # display_indices = []
        # numpy.take(return_frame, (display_indices)) = numpy.take(frame, (display_indices))
        
        return return_frame

