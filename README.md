# Patient-Fall-Detection-System
Patient Monitoring System to detect fall using OpenCV

### Version 0 
## Person Fall Detection using OpenCV

### Version 0

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
