#coding=utf-8
import cv2
import numpy

image = cv2.imread("building.jpg", 0)
#构造一个3x3的结构元素
element = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
#膨胀图像
dilate = cv2.dilate(image, element)
#腐蚀图像
erode = cv2.erode(image, element)

#将两幅图像相减获得边，第一个参数是膨胀后的图像，第二个参数是腐蚀后的图像
result1 = cv2.absdiff(dilate, erode)

#上面得到的结果是灰度图，将其二值化以便更清楚的观察结果
retval,result2 = cv2.threshold(result1,40,255,cv2.THRESH_BINARY)
#反色，即对二值图每个像素取反
result3 = cv2.bitwise_not(result2)
#显示图像
cv2.imshow("image",image)
cv2.imshow("dilate",dilate)
cv2.imshow("erode",erode)
cv2.imshow("result1",result1)
cv2.imshow("result2",result2)
cv2.imshow("result3",result3)
cv2.waitKey(0)
cv2.destroyAllWindows()


