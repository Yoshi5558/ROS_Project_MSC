#!/usr/bin/env python
import rospy
import numpy as np
from std_msgs.msg import Float64
from AR_week4_test.msg import Cubic_Traj_Coeffs

def callback(data):
    publisher(data.a0,data.a1,data.a2,data.a3,data.t0,data.tf)

def listener():
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('cubic_coeffs', Cubic_Traj_Coeffs, callback)
    rospy.spin()

def publisher(a0,a1,a2,a3,t0,tf):
    x = 0
    pub0 = rospy.Publisher('position_trajectory', Float64, queue_size=100)
    pub1 = rospy.Publisher('velocity_trajectory', Float64, queue_size=100)
    pub2 = rospy.Publisher('acceleration_trajectory', Float64, queue_size=100)
    r = rospy.Rate(50)
    while not rospy.is_shutdown():
	msg_position = a0 + (a1*x) + (a2*(x**2))+(a3*(x**3))
	msg_velocity = a1 + (2*a2)*(x) + (3*a3)*(x**2)
        msg_acceleration = 2*a2 + (6*a3)*(x)
        pub0.publish(msg_position)
	pub1.publish(msg_velocity)
	pub2.publish(msg_acceleration)
        x += 0.1
	r.sleep()
        if x >= tf:
	   break

if __name__ == '__main__':
    listener()



