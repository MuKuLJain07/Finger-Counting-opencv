andDetector(min_detection_confidence=0.75)


# while True:
#         ret, frame = cap.read()

#         # overlay images
#         h, w, c = overlayList[1].shape
#         frame[0:h, 0:w] = overlayList[1]
        
#         cv2.imshow("frame" , frame)

#         if cv2.waitKey(1) & 0xFF == ord('q'): 
#             break