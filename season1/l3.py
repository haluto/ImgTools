
#coding=utf-8    
import cv2    
import numpy as np    
         
img = cv2.imread('lena.jpg')    
h = np.zeros((256,256,3)) #创建用于绘制直方图的全0图像    
         
bins = np.arange(256).reshape(256,1) #直方图中各bin的顶点位置    
color = [ (255,0,0),(0,255,0),(0,0,255) ] #BGR三种颜色    
for ch, col in enumerate(color):    
    originHist = cv2.calcHist([img],[ch],None,[256],[0,256])    
    cv2.normalize(originHist, originHist,0,255*0.9,cv2.NORM_MINMAX)    
    hist=np.int32(np.around(originHist))    
    pts = np.column_stack((bins,hist))    
    cv2.polylines(h,[pts],False,col)    
         
h=np.flipud(h)    
         
cv2.imshow('colorhist',h)    
cv2.waitKey(0)    

'''
import cv2
import numpy as np

def calcAndDrawHist(image, color):
    hist = cv2.calcHist([image], [0], None, [256], [0.0,255.0])
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(hist)
    histImg = np.zeros([256,256,3], np.uint8)
    hpt = int(0.9*256);
    
    for h in range(256):
        intensity = int(hist[h]*hpt/maxVal)
        cv2.line(histImg, (h,256), (h,256-intensity), color)
        
    return histImg


if __name__ == '__main__':
    img = cv2.imread("lena.jpg")
    b,g,r = cv2.split(img)

    histImgB = calcAndDrawHist(b, [255, 0, 0])
    histImgG = calcAndDrawHist(g, [0, 255, 0])
    histImgR = calcAndDrawHist(r, [0, 0, 255])
    
    cv2.imshow("histImgB", histImgB)
    cv2.imshow("histImgG", histImgG)
    cv2.imshow("histImgR", histImgR)
    cv2.imshow("Img", img)    
    cv2.waitKey(0)    
    cv2.destroyAllWindows()   
    
'''