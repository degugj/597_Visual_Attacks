import time
import picamera
import numpy as np
import cv2

import replay_attack

with picamera.PiCamera() as camera:
    resolution = (320, 240)
    camera.resolution = resolution
    camera.framerate = 24
    video_feed = []
    video_true = []
    c = 0
    while 1:
        output = np.empty((240, 320, 3), dtype=np.uint8)  # 3D matrix of rgb values
        camera.capture(output, 'rgb', True)  # Find argument to make capture faster (at framerate)
        video_true.append(output)
        c+=1
        # Here is where we'd modify and inject the frame
        output = replay_attack.replay_attack(100, output)
        video_feed.append(output)
        print(c)
        if c == 1000:
            break
    print("Number of Frames Captured: ", len(video_feed))
    # Build video from numpy array

    out = cv2.VideoWriter('output_video.avi', cv2.VideoWriter_fourcc(*'DIVX'), 24, resolution)
    out_true = cv2.VideoWriter('output_true.avi', cv2.VideoWriter_fourcc(*'DIVX'), 24, resolution)
    for i in range(c):
         out.write(video_feed[i])
         out_true.write(video_true[i])
    out.release()
    out_true.release()
