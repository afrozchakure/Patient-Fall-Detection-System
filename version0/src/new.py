#Based on Zed code - Person Fall detection using raspberry pi camera and opencv lib. Link: https://www.youtube.com/watch?v=eXMYZedp0Uo

import cv2
import time

fitToEllipse = False
cap = cv2.VideoCapture('queda.mp4')
time.sleep(2)

fgbg = cv2.createBackgroundSubtractorMOG2()
j = 0

while(1):
    ret, frame = cap.read()
    
    #Convert each frame to gray scale and subtract the background
    try:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        fgmask = fgbg.apply(gray)
        
        #Find contours
        contours, _ = cv2.findContours(fgmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
        
            # List to hold all areas
            areas = []

            for contour in contours:
                ar = cv2.contourArea(contour)
                areas.append(ar)
            
            max_area = max(areas, default = 0)  # Take contour with maximum area

            max_area_index = areas.index(max_area)  # Index of contour with maximum area

            cnt = contours[max_area_index]  # Contour with max_area_index

            M = cv2.moments(cnt)
            
            x, y, w, h = cv2.boundingRect(cnt)

            cv2.drawContours(fgmask, [cnt], 0, (255,255,255), 3, maxLevel = 0)
            
            if h < w:  # If height is less than width
                j += 1
                
            if j > 10:  # If count is greater than 10 frames
                # print("FALL")
                cv2.putText(fgmask, 'FALL', (x, y), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (255,255,255), 2) # Put the text Fall 
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)

            if h > w:   # If height is greater than width
                j = 0 
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)   # Creating a rectangle


            cv2.imshow('video', frame)  # Showing the video frame
        
            if cv2.waitKey(33) == 27: # Exit the video ()
                break
    except Exception as e:
        break
cv2.destroyAllWindows()  # Destroy all windows
