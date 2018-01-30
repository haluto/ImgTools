#coding=utf-8
import cv2
import numpy

image = cv2.imread("building.jpg", 0)
#����һ��3x3�ĽṹԪ��
element = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
#����ͼ��
dilate = cv2.dilate(image, element)
#��ʴͼ��
erode = cv2.erode(image, element)

#������ͼ�������ñߣ���һ�����������ͺ��ͼ�񣬵ڶ��������Ǹ�ʴ���ͼ��
result1 = cv2.absdiff(dilate, erode)

#����õ��Ľ���ǻҶ�ͼ�������ֵ���Ա������Ĺ۲���
retval,result2 = cv2.threshold(result1,40,255,cv2.THRESH_BINARY)
#��ɫ�����Զ�ֵͼÿ������ȡ��
result3 = cv2.bitwise_not(result2)
#��ʾͼ��
cv2.imshow("image",image)
cv2.imshow("dilate",dilate)
cv2.imshow("erode",erode)
cv2.imshow("result1",result1)
cv2.imshow("result2",result2)
cv2.imshow("result3",result3)
cv2.waitKey(0)
cv2.destroyAllWindows()


