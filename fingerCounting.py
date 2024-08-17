import cv2
import time
import os
import HandTrackingModule as htm

# cv screen setup
Wcam, Hcam = 1280, 720
cap = cv2.VideoCapture(0)
cap.set(3, Wcam)
cap.set(4, Hcam)


# fingers image display setup
folderPath = "Fingers"
myList = os.listdir(folderPath)

overlayList = []
for imagePath in myList:
    image = cv2.imread(f'{folderPath}/{imagePath}')
    overlayList.append(image)


# hand detection
detector = htm.handDetector(min_detection_confidence=0.75)

TipIds = [8, 12, 16, 20]                                      # index, middle, ring, pinky            thumb -> 4

while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)

        frame = detector.findHands(frame)
        lmList = detector.findPosition(frame, draw=False)

        
        if len(lmList) != 0:                                           # hand detected
            fingers = []

            # for thumb
            if lmList[4][1] > lmList[4-1][1]:
                fingers.append(1)                                      # checking for index finger
            else:
                fingers.append(0)
  
            for tipId in TipIds:
                if lmList[tipId][2] < lmList[tipId-2][2]:
                    fingers.append(1)                                  # checking for index finger
                else:
                    fingers.append(0)

            # evaluate finger array for displaying the correct image
            fingercount = fingers.count(1)
            print(fingercount)

            # overlay images
            h, w, c = overlayList[fingercount].shape
            frame[0:h, 0:w] = overlayList[fingercount]
        
        cv2.imshow("frame" , frame)

        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break