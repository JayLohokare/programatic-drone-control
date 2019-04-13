import CoDrone
import cv2

cap = cv2.VideoCapture("rtsp://192.168.100.1/cam1/mpeg4")

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('Frame',frame)
 
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
        
    else: 
        break
 
    

cap.release() 