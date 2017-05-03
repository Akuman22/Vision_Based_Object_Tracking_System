#!/usr/bin/env python

import rospy
import serial as ps
from std_msgs.msg import UInt16MultiArray

pub = rospy.Publisher('pixel_coordinates',UInt16MultiArray , queue_size=10)  
rospy.init_node('testing', anonymous=True)

while(1):
    x = raw_input("enter x pixel")
    y = raw_input("enter y pixel")
    coord = UInt16MultiArray()
    coord.data = [int(x),int(y)]
    rate = rospy.Rate(100) # 10hz
    pub.publish(coord)
    rate.sleep()
    
    