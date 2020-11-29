import time
import sys
import picamera
import numpy as np
import cv2
from datetime import datetime
import threading

import replay_attack
import verification
terminated = False
def input_thread():
    while not terminated:
            numBlinks = input("Enter number of blinks for display: ")
            if numBlinks == '':
                return
            verification.blink_verification(numBlinks)
isReplayAttack = False
isBlinkDemo = False
isSelectiveReplayAttack = False
isBlinkAttack = False
isForgedAttack = False
isIFC_Verification = False
isBlinkVerification = False
thread = None;
if len(sys.argv)>1:
    if sys.argv[1] == "replay":
        isReplayAttack = True
    if sys.argv[1] == "blinkDemo":
        isBlinkDemo = True
if isBlinkDemo or isSelectiveReplayAttack or isBlinkAttack:
    thread = threading.Thread(target=input_thread, args=())
    thread.daemon = True
    thread.start()
with picamera.PiCamera() as camera:
    resolution = (320, 240)
    camera.resolution = resolution
    camera.framerate = 24
    video_feed = []
    video_true = []
    c = 0
    prevFrame = None
    for c in range(1000):
        output = np.empty((240, 320, 3), dtype=np.uint8)  # 3D matrix of rgb values
        
        camera.capture(output, 'rgb', True)  # Find argument to make capture faster (at framerate)
        video_true.append(output)
        
        """if prevFrame != None:
            correlation = verification.interframe_correlation(prevFrame, output)
            print("correlation: ", correlation)
        prevFrame = output
        """
        
        # Here is where we'd modify and inject the frame
        if isReplayAttack:
            output = replay_attack.replay_attack(100, output)
            video_feed.append(output)
        
        c+=1
    if isBlinkDemo or isSelectiveReplayAttack or isBlinkAttack:
        terminate = True
        print("\nPress Enter to Exit")
        thread.join()
    # Build video from numpy array
    now = datetime.now()
    if isReplayAttack or isForgedAttack:
        out = cv2.VideoWriter('outputs/output_spoof'+str(now)+'.avi', cv2.VideoWriter_fourcc(*'DIVX'), 24, resolution)
    
    out_true = cv2.VideoWriter('outputs/output_true'+str(now)+'.avi', cv2.VideoWriter_fourcc(*'DIVX'), 24, resolution)
    for i in range(c):
        if isReplayAttack or isForgedAttack:
            out.write(video_feed[i])
        out_true.write(video_true[i])
    if isReplayAttack or isForgedAttack:
        out.release()
    out_true.release()
