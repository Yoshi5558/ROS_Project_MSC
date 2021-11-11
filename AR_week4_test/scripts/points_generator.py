#!/usr/bin/env python
import rospy
import random
from AR_week4_test.msg import Cubic_Traj_Params

def points_generator():
    rospy.init_node('points_generator', anonymous=True)
    publisher = rospy.Publisher('cubic_params', Cubic_Traj_Params, queue_size = 1)
    msg = Cubic_Traj_Params()
    rate = rospy.Rate(0.2)
    while not rospy.is_shutdown():
        p0,pf,v0,vf = random.sample(range(-10,10),4)
        tf = random.sample(range(5,10), 1)[0]
        t0 = 0.0
        msg.p0 = float(p0)
        msg.pf = float(pf)
	msg.v0 = float(v0)
	msg.vf = float(vf)
	msg.t0 = t0
	msg.tf = float(tf)
	print(msg)
        publisher.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        points_generator()
    except rospy.ROSInterruptException:
        pass

