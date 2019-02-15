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


#Global Variables
color_marker=1
num_marker = 10
marks_updated = False

#CALL BACK FUNCTION
def mouseCallBack(action,x,y,flags,params):
    global marks_updated

    if action == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(marker_image,(x,y),10,(color_marker),-1)
        
        cv2.circle(image_copy,(x,y),10,colors[color_marker],-1)

        marks_updated = True
    
cv2.namedWindow('Image')
cv2.setMouseCallback('Image',mouseCallBack)

while True:
    cv2.putText(image_copy,'IIIIIIII',(3,15),cv2.FONT_HERSHEY_SIMPLEX,.5,colors[color_marker],2)
    cv2.imshow('Segments',segments)
    cv2.imshow('Image',image_copy)
    
    k = cv2.waitKey(1)

    if k == 27:
        break 
    
    #CLEARING COLOR 
    elif k == ord('c'):
        image_copy = image.copy()
        marker_image = np.zeros(image.shape[:2],dtype=np.int32)
        segments = np.zeros(image.shape,dtype=np.int8)
    
    elif k > 0 and chr(k).isdigit():
        color_marker = int(chr(k))


    if marks_updated:
        
        marker_image_copy = marker_image.copy()
        
        cv2.watershed(image, marker_image_copy)
        
        segments = np.zeros(image.shape,dtype=np.uint8)
        
        for color_idx in range(num_marker):
            segments[marker_image_copy == (color_idx)] = colors[color_idx]
        
        marks_updated = False

cv2.destroyAllWindows()