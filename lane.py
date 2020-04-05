import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
def cal_lines(img,lines):
    img = np.copy(img)
    blank_image = np.zeros((img.shape[0],img.shape[1],3),dtype = np.uint8)
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv.line(blank_image,(x1,y1),(x2,y2),(0,0,255),5)
        img = cv.addWeighted(img,0.8,blank_image,0.9,0.0)
        return img
cap = cv.VideoCapture('lane_vgt.mp4')
while(1):
    ret ,frame  = cap.read()
    #gray_image = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(frame,(3,3),0)
    mask = cv.inRange(blur,(110,110,110),(130,255,255))
    res = cv.bitwise_and(blur,blur,
    mask = mask )
    res = cv.cvtColor(res,cv.COLOR_BGR2GRAY)
    ret,thresh = cv.threshold(res,110,255,cv.THRESH_BINARY)
    ret,thresh2 = cv.threshold(thresh,110,255,cv.THRESH_BINARY)
    canny_image = cv.Canny(thresh2,100,200)
    cropped_image = cv.rectangle(canny_image,(0,0),(640,200),(0,0,0),-1)
    cv.imshow('fgh',cropped_image)
    lines = cv.HoughLinesP(cropped_image,10,np.pi/60,100,150,
    minLineLength = 50,maxLineGap  = 25)
    blank_image = cal_lines(frame,lines)
    cv.imshow('img',blank_image)
    k = cv.waitKey(1)
    if k == ord('q'):
        break
cv.destroyAllWindows()
