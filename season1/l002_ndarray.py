#!/usr/bin/python
#coding=utf-8

'''
OpenCV的  Python API是基于Numpy的，其核心数据结构是ndarray。
'''

import cv2
import numpy as np


def main():
    '''
    2.1 认识numpy中的ndarray
    '''
    
    '''
    2.1.1 构造ndarray对象
    '''
    
    '''
    1. 构造二维的ndarray
    
    构造一个二维数组（矩阵），需要知道的最基本信息是它的行数（高）和列数（宽）及其数据类型，
    如  uint8，  int32，  float32，  float64等。
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
    
    # 初始化一个2*2*4的  32位浮点型数组（即可以把这个三维数组理解为两个2*4的二维数组）
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
    #例如获取m中的第1个二维数组，即第1个数组的所有行和列
    #m[1,:,:]
    print "\nGet the index1 2d array of the 3d array\n", m, "\nis\n", m[1,:,:]
    
    
    
    '''
    2.3 矩阵的运算
    一般用到的关于矩阵的运算包括：加法、减法、点乘、点除、乘法等。
    '''
    
    '''
    2.3.1 加法运算
    矩阵的加法就是两个矩阵对应位置的数值相加。
    '''
    #(1) Use "+" of Numpy
    src1 = np.array([[23,123,90],[100,250,0]],np.uint8)
    src2 = np.array([[125,150,60],[100,10,40]],np.uint8)
    dest = src1 + src2
    print "\nArray + Array demo:\n", src1, "\n+\n", src2, "\nis\n", dest
    #array对大于255的  uchar 类型的处理方式是将该数对255取模运算后减1，即   273%255-1 = 7
    
    #(2) Use OpenCV python API "add"
    src1 = np.array([[23,123,90],[100,250,0]],np.uint8)
    src2 = np.array([[125,150,60],[100,10,40]],np.float32)
    dest = src1 + src2
    print "\nArray + Array demo:\n", src1, "\n+\n", src2, "\nis\n", dest
    dst = cv2.add(src1, src2, dtype=cv2.CV_32F)
    print "\nArray + Array demo:\n", src1, "\n+\n", src2, "\nis\n", dst
    
    '''
    2.3.2 减法运算
    矩阵的减法与加法类似，但有几点注意事项。
    '''
    #减法通过“-”运算符实现
    src1 = np.array([[23,123,90],[100,250,0]],np.uint8)
    src2 = np.array([[125,150,60],[100,10,40]],np.uint8)
    dest = src1 - src2
    print "\nArray - Array demo:\n", src1, "\n-\n", src2, "\nis\n", dest
    #Numpy处理23-125，是将该数对255取模运算后加1，即  ：  -102%255+1 = 154
    
    '''
    2.3.3 点乘运算
    矩阵的点乘即两个矩阵对应位置的数值相乘。
    '''
    #点乘通过“*”运算符；或multiply函数
    src1 = np.array([[23,123,90],[100,250,0]],np.uint8)
    src2 = np.array([[125,150,60],[100,10,40]],np.float32)
    dest = src1*src2
    print "\nArray * Array demo:\n", src1, "\n*\n", src2, "\nis\n", dest
    dst = np.multiply(src1, src2)
    print "\nArray * Array demo:\n", src1, "\n*\n", src2, "\nis\n", dst
    
    '''
    2.3.4 点除运算
    点除运算是两个矩阵对应位置的数值相除。
    '''
    #点除通过“/”运算符
    src1 = np.array([[23,123,90],[100,250,0]],np.uint8)
    src2 = np.array([[125,150,60],[100,10,40]],np.uint8)
    dest = src2 / src1
    print "\nArray / Array demo:\n", src2, "\n/\n", src1, "\nis\n", dest
    # 40/0 处理为等于0
    
    src1 = src1.astype(np.float32) #改变src1的数据类型
    dest = src2 / src1
    print "\nArray / Array demo:\n", src2, "\n/\n", src1, "\nis\n", dest
    #从打印结果可以看出，此时40/0=inf
    #所以Numpy处理分母为0的情况时，如果两个ndarray都是uint8类型的，则返回值为0；其他情况返回inf。
    
    '''
    2.3.5 乘法运算
    '''
    #使用Numpy中的“*”运算符或者multiply函数可以完成两个array的点乘，而对于矩阵的乘法则使用dot函数
    src3 = np.array([[1,2,3],[4,5,6]],np.uint8)
    src4 = np.array([[6,5],[4,3],[2,1]],np.uint8)
    dest = np.dot(src3, src4)
    print "\nArray dot Array demo:\n", src3, "\ndot\n", src4, "\nis\n", dest
    #  | 1,2,3 |       | 6,5 |      | 1*6+2*4+3*2, 1*5+2*3+3*1 |      | 20, 14 |
    #  | 4,5,6 |    *  | 4,3 |   =  | 4*6+5*4+6*2, 4*5+5*3+6*1 |   =  | 56, 41 |
    #                  | 2,1 |      
    
    '''
    2.3.6 其他运算
    '''
    '''
    1. 指数和对数运算
    这里讨论的对数和指数运算是对矩阵中的每一个数值进行相应的运算。当然我们可以使用for循环对矩阵中每一个值进行相应的运算，
    但  OpenCV提供了exp和  log函数（这里log是以e为底的）封装了该操作。这两个函数输入矩阵的数据类型只能是CV_32F或  CV_64F。
      Numpy同样提供了exp和  log函数，但输入的ndarray可以是任意数据类型，返回的ndarray为  float或者double类型。
    '''
    src5 = np.array([[6,5],[4,3]],np.uint8)
    dest1 = np.exp(src5)
    dest2 = np.log(src5)
    print "\nArray exp demo:\n", src5, "\nexp is\n ", dest1, "\ndtype is: ", dest1.dtype
    print "\nArray log demo:\n", src5, "\nlog is\n ", dest2, "\ndtype is: ", dest2.dtype
    
    '''
    2. 幂指数和开平方运算
    这里讨论的幂指数和开平方运算是对矩阵中的每一个数值进行相应的运算。
    OpenCV提供了pow和  sqrt函数。
    Numpy提供了针对ndarray的幂指数运算power函数
    '''
    src = np.array([[25,40],[10,100]],np.uint8)
    dest1 = np.power(src,2)
    dest2 = np.power(src,2.0)
    print "\n", dest1, "\n", dest2
    
if __name__ == "__main__":
    main()
    
    