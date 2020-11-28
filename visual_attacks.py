import time
import sys
import picamera
import numpy as np
import cv2
from datetime import datetime
import replay_attack


isReplayAttack = False
isSelectiveReplayAttack = False
isForgedAttack = False
isIFC_Verification = False
isBlinkVerification = False

if len(sys.argv)>1:
    if sys.argv[1] == "replay":
        isReplayAttack = True

with picamera.PiCamera() as camera:
    resolution = (320, 240)
    camera.resolution = resolution
    camera.framerate = 24
    video_feed = []
    video_true = []
    c = 0
    
    for c in range(1000):
        #output = np.empty((240, 320, 3), dtype=np.uint8)  # 3D matrix of rgb values
        output = picamera.array.PiRGBArray(camera)
        camera.capture(output, 'bgr')  # Find argument to make capture faster (at framerate)
        video_true.append(output)
        # Here is where we'd modify and inject the frame
        if isReplayAttack:
            output = replay_attack.replay_attack(100, output)
            video_feed.append(output)
        c+=1
    
    
    # Build video from numpy array
    now = datetime.now()
    if isReplayAttack or isForgedAttack:
        out = cv2.VideoWriter('outputs/output_video'+str(now)+'.avi', cv2.VideoWriter_fourcc(*'DIVX'), 24, resolution)
    
    out_true = cv2.VideoWriter('outputs/output_true'+str(now)+'.avi', cv2.VideoWriter_fourcc(*'DIVX'), 24, resolution)
    for i in range(c):
        if isReplayAttack or isForgedAttack:
            out.write(video_feed[i])
        out_true.write(video_true[i])
    if isReplayAttack or isForgedAttack:
        out.release()
    out_true.release()
