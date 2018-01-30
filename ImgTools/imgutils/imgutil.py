import cv2
import numpy as np
import traceback

# check supported COLOR type in cv2.
# flags = [i for i in dir(cv2) if i.startswith('COLOR_')]


class YUVWidthHeightError(Exception):
    pass

#------------------------------------------------------
# viewImage
#------------------------------------------------------
def viewImage(imgInFN):
    IMGWIN = "ImageWindow"
    
    img = cv2.imread(imgInFN)
    cv2.namedWindow(IMGWIN)
    cv2.imshow(IMGWIN, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
#------------------------------------------------------
# cvtImg2YUV
# convert image file to YUV
#------------------------------------------------------
def cvtImg2YUV(imgInFN, yuvOutFN):
    img = cv2.imread(imgInFN)
    emptyImage = cv2.cvtColor(img, cv2.COLOR_BGR2YUV_I420)
    
    newOutFN = yuvOutFN
    postfix = yuvOutFN[-4:]
    if postfix.lower() == '.yuv':
        # new name is: [filename]_[width]x[height].yuv
        newOutFN = yuvOutFN[:-4] + '_' + str(img.shape[1]) + 'x' + str(img.shape[0]) + postfix
    fOut = open(newOutFN, 'wb')
    fOut.write(emptyImage)
    fOut.close()

#------------------------------------------------------
# viewYUV
#------------------------------------------------------
def viewYUV(yuvInFN, w, h):
    IMGWIN = "ImageWindow"
    
    yuvData = np.fromfile(yuvInFN, dtype=np.uint8)
    # should assert here.
    #print int(yuvData.shape[0])
    #print int(h*1.5*w)
    if int(yuvData.shape[0]) != int(h*1.5*w):
        raise YUVWidthHeightError()
    yuvData = yuvData.reshape((h*1.5, w))
    
    #COLOR_YUV2BGRA_I420
    #COLOR_YUV2BGR_I420
    #COLOR_YUV2BGR_NV21
    
    emptyImage = cv2.cvtColor(yuvData, cv2.COLOR_YUV2BGR_I420)

    cv2.namedWindow(IMGWIN)
    cv2.imshow(IMGWIN, emptyImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def viewYUV2(yuvInFN, w, h):
    IMGWIN = "ImageWindow"
    
    yuvData = np.fromfile(yuvInFN, dtype=np.uint8)
    
    e = w*h
    Y = yuvData[0:e]
    Y = np.reshape(Y, (h, w))
    
    s = e
    V = yuvData[s::2]
    V = np.repeat(V, 2, 0)
    V = np.reshape(V, (h/2,w))
    V = np.repeat(V, 2, 0)
    
    U = yuvData[s+1::2]
    U = np.repeat(U, 2, 0)
    U = np.reshape(U, (h/2,w))
    U = np.repeat(U, 2, 0)
    
    RGBMatrix = (np.dstack([Y,U,V])).astype(np.uint8)
    RGBMatrix = cv2.cvtColor(RGBMatrix, cv2.COLOR_YUV2RGB, 3)

    cv2.namedWindow(IMGWIN)
    cv2.imshow(IMGWIN, RGBMatrix)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    pass

if __name__ == '__main__':
    main()