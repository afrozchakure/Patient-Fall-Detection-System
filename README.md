## Person Fall Detection using OpenCV

[![GitHub stars](https://img.shields.io/github/stars/afrozchakure/Patient-Fall-Detection-System?color=green&style=for-the-badge)](https://github.com/afrozchakure/Python-Games/stargazers)
[![GitHub license](https://img.shields.io/github/license/afrozchakure/Patient-Fall-Detection-System?color=blue&style=for-the-badge)](https://github.com/afrozchakure/Patient-Fall-Detection-System/blob/master/LICENSE)
[![GitHub forks](https://img.shields.io/github/forks/afrozchakure/Patient-Fall-Detection-System?color=orange&style=for-the-badge)](https://github.com/afrozchakure/Patient-Fall-Detection-System/network)
[![Visits Badge](https://badges.pufler.dev/visits/afrozchakure/Patient-Fall-Detection-System?color=blueviolet&style=for-the-badge)](https://badges.pufler.dev)
[![Created Badge](https://badges.pufler.dev/created/afrozchakure/Patient-Fall-Detection-System?color=yellowgreen&style=for-the-badge)](https://badges.pufler.dev)
[![Updated Badge](https://badges.pufler.dev/updated/afrozchakure/Patient-Fall-Detection-System?color=red&style=for-the-badge)](https://badges.pufler.dev)

## 1. Version 0

#### Getting the video:
* The program gets the video from the source or path which is passed to it.
* Then we create a background subtractor ``fgbg``.

#### Within the while(1) loop: 
* It **converts each of the frames to grayscale** and **applies Background Subtractor on the image**.
* The ``cv2.findContours()`` takes in the **source image, the contour retrieval mode and contour approximation method to give image, contours and hierarchy**. 
* ``contours`` is a Python list of all the contours in the image.
* We then try to find area of contours from a frame. To do that we have used ``cv2.contourArea(contour)`` function to find the area within the contours and we later append the area to ``areas`` list.
* We take the maximum value from the ``areas`` list and find the ``contour`` with the maximum area.
* Then we find the moment ``M`` for the contour.
* The values of ``x, y, w, h`` are obtained for contour using ``cv2.boundingRect()``

#### Loop Checking if h < w :
* Each time when the value of ``h`` is less than ``w``, we increment the value of j by 1.
* When the value of j is greater than 10, we classify that as a **"Fall"** and draw bounding boxes with **Red** color, otherwise if value of ``h`` is more than ``w`` its **not a Fall**, the value of j is again set to 0 and we draw the rectangle with **Green**.

#### Breaking out of the loop:

* It checks if waitKey(33) is equal to 27 (ASCII) and if it is then it breaks the loop.
![](extras/waitkey.png)

#### Results:

#### 1) Fall
![](version0/doc/extras/pic1.png)
![](version0/doc/extras/pic4.png)

#### 2) Not a Fall
![](version0/doc/extras/pic2.png)
![](version0/doc/extras/pic3.png)

#### Limitations:

* Fails to work everytime, needs improvements in terms of detection and recognising a fall.
* Far too simple model for recognition and doesn't work for all test cases (especially when there are objects in the background).


## 2. Version 1



### Fall Detection v1 (Specifics to v1)

* The first version of the fall detector **utilizes sort of a dynamic approach**. It will **detect if a person is not moving or is moving too little in a specific time period.**
* Detections **could be configured** so that there are different detection times for e.g. sitting on the sofa or lying in the bed and if the person is lying on the floor not moving the detection could be triggered in a few minutes. 
* When the detection is made it will **send an alarm to a RESTful web service**. This web service can trigger different functions from a centralized alarm center. 
* These functions include information to professional care takers and family.

#### Use of Simple Adaptive Backgrounding Method:
* The first version of the fall detector uses a **simple adaptive backgrounding method**. 
* As preprocessing the background method does make the frame gray scale and resizes it smaller so that the foreground can be detected faster. 
* This backgrounding method is **not able to handle illumination changes quickly**. It can identify and track movement of multiple objects at the same time.

### Description of v1

* The minimum allowed size of bounding boxes can be set in the settings so that minimal objects won't count as persons in the scene. 
* If a person suffers from a fall, this does not yet trigger the alarm but by lying on the floor not moving enough will start an alarm counter. 
* The system will raise an alarm if the person doesn't move or hasn't moved enough till the set threshold.
* The various settings can be controlled using Keys like 0-9, 'o', '+' and 'p'.
* If it detects a fall, it will form a cross over the frame to make it easier to detect where the person fell from the bed.

#### Version-1 files

1. **main.py** - is the main loop. This main loop starts the software and keeps it running while calling different functions in the video class.

2. **video.py** - Video class - utilizes the video feed. It is able to capture frames from the feed, call different background subtraction features, take keyboard inputs for changing settings (these can be found in testSettings()), raise an alarm, downscale frames for rapid future use, show frames for debugging reasons and release the camera and cleanup if quitting.

3. **bs.py** - __Bs class__ - is handling the background subtraction and supports MOG2 and the dynamic approach.

4. **person.py** - __Person and Persons class__ - is called by Video class. It includes two classes Person and Persons. Each time a frame is analyzed and a person is found it will try to analyze if the person has been in the previous frames and is it the same person as earlier.
  Other features are data of how much the person moved during last frames, has the person raised an alarm and has it been sent to the webservice, where was the person in the last frame and should the person be removed (exited the scene). Person class also contains the alarm counter.

5. **webservice.py** - __Webservice class__ - is able to send alarms to a webservice via http-requests.

6. **settings.py** - __Settings class__ - includes all the settings that can be modified in the system. Some of these settings can be changed on the fly but some are static when the program runs. This file includes settings for the following things:

#### Set of options in Settings:
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

#### Additional steps:
* Appropriate thresholds must be set for the bed. 

## 3. Version 2

#### Fall Detection v2

* The minimum allowed size of bounding boxes can be set in the settings so that minimal objects won't count as persons in the scene. 
* If a person suffers from a fall, this does not yet trigger the alarm but by lying on the floor not moving enough will start an alarm counter. 
* The system will raise an alarm if the person doesn't move or hasn't moved enough till the set threshold.
* The various settings can be controlled using Keys like 0-9, 'o', '+' and 'p'.
* If it detects a fall, it will form a cross over the frame to make it easier to detect where the person fell from the bed.

#### Features of v2 program

* Person not moving alert
* Multiple person detection
* Ability to adjust detecting settings live
* Basic automatic handler for light condition change
* Ability to push information to a webservice
* Current detection time period is 50 frames (~10 seconds)

#### Version-2 files

1. **main.py** - is the main loop. This main loop starts the software and keeps it running while calling different functions in the video class.

2. **video.py** - Video class - utilizes the video feed. It is able to capture frames from the feed, call different background subtraction features, take keyboard inputs for changing settings (these can be found in testSettings()), raise an alarm, downscale frames for rapid future use, show frames for debugging reasons and release the camera and cleanup if quitting.

3. **bs.py** - __Bs class__ - is handling the background subtraction and supports MOG2 and the dynamic approach.

4. **person.py** - __Person and Persons class__ - is called by Video class. It includes two classes Person and Persons. Each time a frame is analyzed and a person is found it will try to analyze if the person has been in the previous frames and is it the same person as earlier.
  Other features are data of how much the person moved during last frames, has the person raised an alarm and has it been sent to the webservice, where was the person in the last frame and should the person be removed (exited the scene). Person class also contains the alarm counter.

5. **webservice.py** - __Webservice class__ - is able to send alarms to a webservice via http-requests.

6. **settings.py** - __Settings class__ - includes all the settings that can be modified in the system. Some of these settings can be changed on the fly but some are static when the program runs. This file includes settings for the following things:

#### Set of options in Settings:
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

#### Additional steps:
* Appropriate thresholds must be set for the bed.

#### Setting of Appropriate thresholds
* The program detects if the person is not moving for a time period. 
* This is probably a better way to detect if a person needs help than detecting when the person fall. 
* In a real situation the time period would be set around 2 minutes if the person is on the floor. 
* For the bed there could be a limit of 12 hours.

### References
Thanks to the amazing Repositories by:
1. @EikeSans (version - 0) - https://github.com/EikeSan/video-fall-detection
2. @infr (version - 1, version - 2)-  https://github.com/infr/falldetector-public
