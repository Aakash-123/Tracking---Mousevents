import cv2 as cv
import numpy as np
drawing = False
WindowName = 'Drawing'
img = np.zeros((512,512,3),np.uint8)
cv.namedWindow(WindowName)
def draw_circle(event,x,y,flags,param):
    if drawing == True:
        event == cv.EVENT_MOUSEMOVE
        cv.circle(img,(x,y),5,(0,255,0),-1)
cv.setMouseCallback(WindowName,draw_circle)
def main():
    while(True):
        cv.imshow(WindowName,img)
        k = cv.waitKey(1)
        if k == ord('0'):
            drawing == True
        elif k == 27:
            break
    cv.destroyAllWindows()
if __name__ == '__main__':
    main()
