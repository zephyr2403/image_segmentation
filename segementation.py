'''
This algorithm is usefull for segmenting images into background and 
foreground in situations that are difficult for other algorithm 
'''
import cv2
import numpy as np 
from matplotlib import cm

image = cv2.imread('/mnt/488266AE8266A064/Images/nature4.jpg')
#image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
image = cv2.resize(image,(800,400))
image_copy = image.copy()


marker_image = np.zeros(image.shape[:2],dtype=np.int32)

segments = np.zeros(image.shape,dtype=np.int8)

def selectColor(i):
    return tuple(np.array(cm.tab10(i)[:3])*255)
    
colors=[]
for i in range(10):
    colors.append(selectColor(i))



