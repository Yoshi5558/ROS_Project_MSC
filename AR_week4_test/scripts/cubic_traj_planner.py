#!/usr/bin/env python

from __future__ import print_function
from std_msgs.msg import Float64
from AR_week4_test.msg import Cubic_Traj_Params, Cubic_Traj_Coeffs
from AR_week4_test.srv import compute_cubic_traj 
import sys
import rospy

def cubic_traj_coeffs_client(p0,pf,v0,vf,t0,tf):
    rospy.wait_for_service('compute_cubic_traj')
    try:
        compute_cubic_coeffs = rospy.ServiceProxy('compute_cubic_traj', compute_cubic_traj)
        response = compute_cubic_coeffs(p0,pf,v0,vf,t0,tf)
        return response
    except rospy.ServiceException as e:
        print("Service call failed:")

def callback(data):
    rospy.loginfo("Received message from:" + rospy.get_caller_id())
    print(data)
    response = cubic_traj_coeffs_client(data.p0, data.pf, data.v0, data.vf, data.t0, data.tf)
    coeff_server(response.a0,response.a1,response.a2,response.a3,data.t0,data.tf)
    return True

def listener():
    rospy.Subscriber("cubic_params", Cubic_Traj_Params, callback)
    rospy.spin()

def coeff_server(a0,a1,a2,a3,t0,tf):
    publisher = rospy.Publisher('cubic_coeffs', Cubic_Traj_Coeffs, queue_size=1)
    msg = Cubic_Traj_Coeffs()
    msg.a0 = a0
    msg.a1 = a1
    msg.a2 = a2
    msg.a3 = a3
    msg.t0 = t0
    msg.tf = tf
    publisher.publish(msg)

if __name__ == "__main__":
    rospy.init_node('listener', anonymous=True)
    listener()
    print("Program Exited!")

