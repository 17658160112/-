import cv2
import sys
from PIL import Image

def CatchUsbVideo(window_name, camera_idx):
    cv2.namedWindow(window_name)

capture=cv2.VideoCapture(0)


while capture.isOpened():

    ret,frame=capture.read()

    cv2.imshow('camera',frame)
    if cv2.waitKey(5)&0xFF==27:
        break

capture.release()

cv2.destroyAllWindows()


if __name__=='__main__':
 CatchUsbVideo(0)
