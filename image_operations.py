#!/usr/bin/env python
import rospy
from std_msgs.msg import UInt16MultiArray
import cv2
#import cv2.cv as cv
import matplotlib.pyplot as plt 

import numpy as np

pub = rospy.Publisher('pixel_coordinates', UInt16MultiArray, queue_size=10) 

'''start camera'''

camera = cv2.VideoCapture(1)

def ProcessImage():    
    '''take image from camera'''   


    ret_val, img = camera.read()
#    img = cv2.flip(img, 1)
    image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # convert to right format
#    plt.imshow(image)
    
#    image = cv2.fastNlMeansDenoisingColored(image,None,10,10,7,21)

    image_blur = cv2.GaussianBlur(image, (7,7),3)  #smoothen the image to remove noise
    img_gray = cv2.cvtColor(image_blur, cv2.COLOR_RGB2GRAY)
    '''find center of ball'''    
    circles = cv2.HoughCircles(img_gray,cv2.cv.CV_HOUGH_GRADIENT,1,20,
                                param1=50,param2=30,minRadius=0,maxRadius=0)
    for i in circles[0,:]:
    # draw the outer circle
        cv2.circle(image,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
        cv2.circle(image,(i[0],i[1]),2,(0,0,255),3)
    circles = np.uint16(np.around(circles))
    
    '''create message for topic to publish'''
    msg = UInt16MultiArray()
    
    msg.data = [circles[0,[0]][0][1], circles[0,[0]][0][0]]  #only 1 circle is assumed, multiple circles not supported
    
    '''send the coordinates to the conversion node'''
    pub.publish(msg)
#    cv2.imshow('boobs',image)
    cv2.waitKey()	
    rate = rospy.Rate(100) #10Hz
    rate.sleep()
    
    
def myhook():
    print "releasing camera..."
    camera.release()
    

if __name__ == '__main__':
    rospy.init_node('camera_node')
    print("camera node initialized")
    ProcessImage()
    rospy.on_shutdown(myhook)
    
 
 
 
 
