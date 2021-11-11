#!/usr/bin/env python

from __future__ import print_function
from AR_week4_test.srv import compute_cubic_traj, compute_cubic_trajResponse
import rospy
import numpy as np

def handle_traj_coeffs(req):
    print("Requested")
    p0 = req.p0
    pf = req.pf
    v0 = req.v0
    vf = req.vf
    t0 = req.t0
    tf = req.tf
    #req.a = p0,req.b = pf,req.c = v0,req.d = vf,req.e = t0,req.f = tf
    time_matrix = np.array([[1,t0,t0**2,t0**3],[0,1,2*t0,3*(t0**3)],[1,tf,tf**2,tf**3],[0,1,2*tf,3*(tf**2)]])
    v_p_matrix = np.array([p0,v0,pf,vf])
    coeff_matrix = np.linalg.solve(time_matrix, v_p_matrix)
    return compute_cubic_trajResponse(coeff_matrix[0],coeff_matrix[1],coeff_matrix[2],coeff_matrix[3])

def compute_traj_coeffs():
    rospy.init_node('compute_traj_coeffs')
    s = rospy.Service('compute_cubic_traj', compute_cubic_traj, handle_traj_coeffs)
    print("Ready to Compute Trajectory")
    rospy.spin()

if __name__ == "__main__":
    compute_traj_coeffs()
