#coding=utf-8
import cv2

img =cv2.imread("lena.jpg", 0)
result = cv2.blur(img, (5,5))
result1 = cv2.boxFilter(img, -1, (5,5))
gaussianResult = cv2.GaussianBlur(img, (5,5), 1.5)

cv2.imshow("Origin", img)
cv2.imshow("Blur", result)
cv2.imshow("boxFilter", result1)
cv2.imshow("gaussianResult", gaussianResult)

cv2.waitKey(0)
cv2.destroyAllWindows()