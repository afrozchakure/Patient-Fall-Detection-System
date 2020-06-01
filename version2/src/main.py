# Fall detector main
# Kim Salmi, kim.salmi(at)iki(dot)fi
# http://tunn.us/arduino/falldetector.php
# License: GPLv3

import video
import time
import sys
import numpy as np
import cv2
import time

video = video.Video('Video/Appo/vid1.mp4')
# video = video.Video('Video/queda.mp4')


time.sleep(0.5)
video.nextFrame()  # To grab the next frame, resize, make it grayscale and blur it
video.testBackgroundFrame()  #

while 1:
    try:
        video.nextFrame()
        video.testBackgroundFrame()
        video.updateBackground()  # To update the background
        video.compare()
        video.showFrame()
        video.testSettings()
        if video.testDestroy():
	        sys.exit()
    except Exception as e:
        break
