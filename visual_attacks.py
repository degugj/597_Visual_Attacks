import time
import picamera
import numpy as np
import cv2

with picamera.PiCamera() as camera:
    camera.resolution = (320, 240)
    resolution = (320, 240)
    camera.resolution = resolution
    camera.framerate = 24
    video_feed = []
    counter = 0
    while 1:
        time.sleep(1)
        #time.sleep(1/30)
        output = np.empty((240, 320, 3), dtype=np.uint8)  # 3D matrix of rgb values
        camera.capture(output, 'rgb')  # Find argument to make capture faster (at framerate)
        camera.capture(output, 'rgb', True)  # Find argument to make capture faster (at framerate)
        counter+=1
        # Here is where we'd modify and inject the frame
        video_feed.append(output)
        print("Got new frame")
        if counter == 20:
        if counter == 1000:
            break
    print("Number of Frames Captured: ", len(video_feed))
    # Build video from numpy array

    out = cv2.VideoWriter('output_video.avi', cv2.VideoWriter_fourcc(*'DIVX'), 60, resolution)
    for i in range(counter):
         out.write(video_feed[i])
    out.release()
