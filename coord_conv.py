#!/usr/bin/env python

import rospy
import numpy as np
import math
from std_msgs.msg import UInt16MultiArray

pub = rospy.Publisher('coord_send',UInt16MultiArray , queue_size=10)  

def callback(data):
    x = data.data[0]
    y = data.data[1]
    x = (100.0/1100.0)*(338 - x) 
    y = (100.0/1100.0)*(403 - y)
    r = np.sqrt((x*x)+(y*y))
    if(y!=0):
        th = math.degrees(math.atan(x/y))
    else:
        th = math.degrees(math.atan(0))
    print "x = ",x 
    print "y = ",y
    print r
    print th
    coord = UInt16MultiArray()
    coord.data = [r,th]
    rate = rospy.Rate(100) # 10hz
    pub.publish(coord)
    rate.sleep()
    
def coord_conv():
    
    rospy.init_node('coord_conv', anonymous=True)
    rospy.Subscriber("pixel_coordinates",UInt16MultiArray , callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
	coord_conv()
