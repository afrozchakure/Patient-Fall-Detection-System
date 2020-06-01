# Fall detector main
# Kim Salmi, kim.salmi(at)iki(dot)fi
# http://tunn.us/arduino/falldetector.php
# License: GPLv3

import video
import time
import sys

video = video.Video("Video/frontfacing/vid8.mp4")

time.sleep(1.0) # let camera autofocus + autosaturation settle
video.nextFrame()
video.testBackgroundFrame()

while 1:
	try:
		video.nextFrame()
		video.testBackgroundFrame()
		video.updateBackground()
		video.compare()
		video.showFrame()
		video.testSettings()
		if video.testDestroy():
			sys.exit()
	except Exception as e:
		break
