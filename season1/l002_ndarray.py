#!/usr/bin/python
#coding=utf-8

'''
OpenCV的Python API是基于Numpy的，其核心数据结构是ndarray。
'''

import cv2
import numpy as np


def main():
    '''
    2.1.1 构造ndarray对象
    '''
    
    '''
    1. 构造二维的ndarray
    
    构造一个二维数组（矩阵），需要知道的最基本信息是它的行数（高）和列数（宽）及其数据类型，
    如uint8，int32，float32，float64等。
    '''
    
    # 构造一个2行4列全是0的uchar类型的二维数组：
    z = np.zeros((2,4),np.uint8) # 构造2行4列的矩阵
    print type(z) # 输出numpy.ndarray
    print "\nThe 2d zero array: ";print z
    
    # 构造一个2行4列全是1的整形矩阵：
    o = np.ones((2,4),np.int32)
    print "\nThe 2d one array:";print o
    
    # 初始化一个浮点型矩阵：
    m = np.array([[4,12,3,1],
                  [10,12,14,29]], np.float32)
    print "\nThe 2d float array:";print m

    
    '''
    2. 构造三维的ndarray
    
    三维数组可以理解成每一个元素都是一个二维数组。
    '''
    
    # 初始化一个2*2*4的32位浮点型数组（即可以把这个三维数组理解为两个2*4的二维数组）
    m = np.array(
                [
                  [[1,2,3,4],[5,6,7,8]],
                  [[10,11,12,14],[15,16,17,18]]
                  ],np.float32)
    print "\nThe 3d float array:";print m
    
    
    '''
    3. ndarray的成员变量
    -- shape
    -- dtype
    '''
    m = np.array([[4,12,3,1],[10,12,14,49]],np.float32)
    print "\nThe shape is:", m.shape
    print "\nThe dtype is:", m.dtype
    
    
    '''
    2.1.2 访问ndarray中的值
    '''
    
    '''
    1. 访问二维ndarray中的值
    '''
    m = np.array([[14,12,3,1],[10,12,114,29],[67,23,534,2]],np.float32)
    
    #第一种情况：如何获取第r行，第c列的值
    #例如获得第1行第3列的值：
    #m[1,3]
    print "\nGet row1 column3 item of\n", m, "\nis\n", m[1,3] # 结果是29.0
    
    #第二种情况：如何获取m中第2行的值
    #m[2,:]
    print "\nGet row2 items of\n", m, "\nis\n", m[2,:] # 结果是[  67.   23.  534.    2.]
    
    #第三种情况：如何获取m中第3列的值
    #m[:,3]
    print "\nGet column3 items of\n", m, "\nis\n", m[:,3] # 结果是[  1.  29.   2.]
    
    #第四种情况：如何获取连续矩形区域的值
    #例如获取m中从左上角第0行第1列至右下角第2行第3列矩形区域的所有值：
    #m[0:2,1:3]  <Me: 区间范围是左闭右开，所以针对题目需求，m[0:3,1:4]更恰当？>
    print "\nGet row0column1-row2column3 rect of\n", m, "\nis\n", m[0:2,1:3] # 结果是[[  12.    3.], [  12.  114.]]
    
    '''
    2. 访问三维ndarray中的值
    '''
    m = np.array([[[1,2,3,4],
                 [5,6,7,8]],
                [[10,11,12,14],
                 [15,16,17,18]],
                [[11,12,43,32],
                 [1,5,10,23]]],np.float32)
    
    #已经知道三维的ndarray可以看成是由二维的ndarray构成的
    
    #第一种情况：如何获取所有二维数组的第c列
    #例如获取m中所有二维数组的第0列
    #m[:,:,0]
    print "\nGet column0 of all 2d arrays in 3d array\n", m, "\nis\n", m[:,:,0]
    #从返回结果可以看出，将所有二维数组的第0列按每行进行排列得到了新的二维数组。
    
    #第二种情况：如何获取三维数组中的第n个二维数组
    #例如
    
if __name__ == "__main__":
    main()
    
    