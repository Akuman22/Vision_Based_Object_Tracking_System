#!/usr/bin/env python
import rospy
import serial as ps
from std_msgs.msg import UInt16MultiArray

def callback(data):
    r = data.data[0]
    th = data.data[1]
    ser = ps.Serial()
    ser.baudrate = 115200
    ser.port = '/dev/ttyUSB0'
    ser.open()
    '''max_pwm - radius*(min_pwm/180)'''
    ser.write("echo t"+str(500-(r*(380.0/180.0)))+" >/dev/pwmservo\n")
    ser.write("echo p"+str(500 - (th*(380.0/180.0)))+" >/dev/pwmservo\n")
    ser.close()
    
def ServoControl():
    rospy.init_node('ServoControl', anonymous=True)
    rospy.Subscriber("coord_send",UInt16MultiArray , callback)
    rospy.spin()

if __name__ == '__main__':
	ServoControl()
