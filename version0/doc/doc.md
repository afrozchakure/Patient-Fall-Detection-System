## Version-1 files

1. **main.py** - is the main loop. This main loop starts the software and keeps it running while calling different functions in the video class.

2. **video.py** - Video class - utilizes the video feed. It is able to capture frames from the feed, call different background subtraction features, take keyboard inputs for changing settings (these can be found in testSettings()), raise an alarm, downscale frames for rapid future use, show frames for debugging reasons and release the camera and cleanup if quitting.

3. **bs.py** - __Bs class__ - is handling the background subtraction and supports MOG2 and the dynamic approach.

4. **person.py** - __Person and Persons class__ - is called by Video class. It includes two classes Person and Persons. Each time a frame is analyzed and a person is found it will try to analyze if the person has been in the previous frames and is it the same person as earlier.
  Other features are data of how much the person moved during last frames, has the person raised an alarm and has it been sent to the webservice, where was the person in the last frame and should the person be removed (exited the scene). Person class also contains the alarm counter.

5. **webservice.py** - __Webservice class__ - is able to send alarms to a webservice via http-requests.

6. **settings.py** - __Settings class__ - includes all the settings that can be modified in the system. Some of these settings can be changed on the fly but some are static when the program runs. This file includes settings for the following things:
``
## Set of options in Settings:
1. **Debug** - Debuggin on or off
2. **Source** - Camera source
3. **BsMethod** - Backgrounding method listed in bs.py
4. **MOG2learningRate** - Learning rate (MOG2)
5. **MOG2shadow** - Shadow detection on or off (MOG2)
7. **MOG2history** - History (MOG2)
8. **MOG2thresh** - Threshold (MOG2)
9. **minArea** - Minimum area to be considered as a person
10. **thresholdLimit** - Threshold for considered as foreground
11. **dilationPixels** - Foreground is dilated this much
12. **useGaussian** - Using gaussian blur on or off
13. **useBw** - Using black and white on or off
14. **useResize** - Resizing frames on or off
15. **gaussianPixels** - Gaussian blur rate
16. **movementMaximum** - Maximum amount that a person can move and still be the same person
17. **movementMinimum** - Minimum amount that a person has to move to reset the alarm count
18. **movementTime** - Alarm count threshold
19. **location** - Location of the camera node, will be sent with the alarm
20. **phone** - Phone number of the resident
