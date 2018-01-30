import cv2  
import numpy as np  

CHANGE_STEP = 50
#param "color": r,g,or b color array
#param "operation": plus or minus 
def changeColor(color, operation):
    arr = color.copy()
    for i in range(color.shape[1]):
        for j in range(color.shape[0]):
            if operation == "plus":
                if arr[j,i] < 255 - CHANGE_STEP:
                    arr[j,i] += CHANGE_STEP
                else:
                    arr[j,i] = 255
            elif operation == "minus":
                if arr[j,i] > CHANGE_STEP:
                    arr[j,i] -= CHANGE_STEP
                else:
                    arr[j,i] = 0
    return arr

img = cv2.imread("cat.jpg")  
  
b = np.zeros((img.shape[0],img.shape[1]), dtype=img.dtype)  
g = np.zeros((img.shape[0],img.shape[1]), dtype=img.dtype)  
r = np.zeros((img.shape[0],img.shape[1]), dtype=img.dtype)  
  
b[:,:] = img[:,:,0]  
g[:,:] = img[:,:,1]  
r[:,:] = img[:,:,2]  

merged = cv2.merge([b,g,r])  
print "Merge by OpenCV"   
print merged.strides  
print merged  
 
#exchange r, b
merged_rgb = cv2.merge([r,g,b])

#plus b, minus r
pb = changeColor(b, "plus")
mr = changeColor(r, "minus")
merged_new = cv2.merge([pb,g,r])
 
mergedByNp = np.dstack([b,g,r])   
print "Merge by NumPy "   
print mergedByNp.strides  
print mergedByNp  
  
cv2.imshow("Merged", merged)
cv2.imshow("merged_new", merged_new)
#cv2.imshow("MergedByNp", merged)  
#cv2.imshow("Blue", b)  
#cv2.imshow("Red", r)  
#cv2.imshow("Green", g)  
cv2.waitKey(0)  
cv2.destroyAllWindows()  