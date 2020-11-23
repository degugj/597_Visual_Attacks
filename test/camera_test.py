from picamera import PiCamera
from time import sleep

# TODOs:
# (1) Configure Pi Camera with Pi
# (2) Still image attack - change/spoof aspects of an image
# (3) Replay video attack - replay some duration of buffered frames
# (4) "Active" video attack - change/spoof aspects of the video live

# Notes:
# If we're using the idea of colors as a verification technique, we should have some sort of range to identify them.
# As Wei said, the NoIR camera is not going to be accurrate enough to detect the exact hexcode of a color

camera = PiCamera()

camera.start_preview()
sleep(15)
camera.stop_preview()
