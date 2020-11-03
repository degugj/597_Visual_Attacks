import time
import picamera
import numpy as np

with picamera.PiCamera() as camera:
    camera.resolution = (320, 240)
    camera.framerate = 24
    video_feed = []
    counter = 0
    while 1:
        time.sleep(1)
        output = np.empty((240, 320, 3), dtype=np.uint8)  # 3D matrix of rgb values
        camera.capture(output, 'rgb')  # Find argument to make capture faster (at framerate)
        counter+=1
        # Here is where we'd modify and inject the frame
        video_feed.append(output)
        print("Got new frame")
        if counter == 20:
            break
    print("Number of Frames Captured: ", len(video_feed))
    # Build video from numpy array
        
