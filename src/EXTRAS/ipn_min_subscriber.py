#!/usr/bin/env python

import roslib
import rospy

roslib.load_manifest('ardrone_test')

# Import the messages we're interested in
from ardrone_autonomy.msg import Navdata

def ReceiveData(data):
	print '[{0:.3f}] Pitch: {1:.3f}'.format(data.header.stamp.to_sec(), data.rotY)
	print '[{0:.3f}] Yaw: {1:.3f}'.format(data.header.stamp.to_sec(), data.rotX)

rospy.init_node('ipn_min_subscriber')
sub_Navdata = rospy.Subscriber('/ardrone/navdata', Navdata, ReceiveData)

while not rospy.is_shutdown():
  pass
