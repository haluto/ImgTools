#coding=utf-8  
import cv2  
import numpy as np    
  
img = cv2.imread("lion.jpg", 0)  

gray_lap = cv2.Laplacian(img,cv2.CV_16S,ksize = 3)  
dst = cv2.convertScaleAbs(gray_lap)  

gaussianResult = cv2.GaussianBlur(img, (5,5), 1.5)
gray_lap1 = cv2.Laplacian(gaussianResult,cv2.CV_16S,ksize = 3)  
dst1 = cv2.convertScaleAbs(gray_lap1)  

cv2.imshow('laplacian',dst)
cv2.imshow('gaussian-laplacian', dst1)
cv2.waitKey(0)  
cv2.destroyAllWindows()  