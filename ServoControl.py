#!/usr/bin/env python

import rospy
import serial as ps
from std_msgs.msg import UInt16MultiArray

def callback(data):
    r = data.data[0]
    th = data.data[1]
#    print str((r*(380.0/180.0)+120.0))
#    print str((th*2*(380.0/180.0)+120))
    ser = ps.Serial()
    ser.baudrate = 115200
    ser.port = '/dev/ttyUSB0'
    ser.open()
#    if((r*(380.0/180.0)+((500.0-120.0)*(1/4))+120)<500 and
#    (th*(380.0/180.0)+((500.0-120.0)*(1/4))+120)<500):
#        ser.write("echo t"+str(r*(380.0/180.0)+((500.0-120.0)*(1/4))+120)+" >/dev/pwmservo\n")
#        ser.write("echo p"+str((th*2*(380.0/180.0)+120))+" >/dev/pwmservo\n")
    ser.write("echo t"+str(500-(r*(380.0/180.0)))+" >/dev/pwmservo\n")
    ser.write("echo p"+str(500 - (th*(380.0/180.0)))+" >/dev/pwmservo\n")

    ser.close()
    
def ServoControl():

    rospy.init_node('ServoControl', anonymous=True)
    rospy.Subscriber("coord_send",UInt16MultiArray , callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
	ServoControl()