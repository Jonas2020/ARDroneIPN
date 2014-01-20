#!/usr/bin/env python

# Simple project that create a topic to send data of IMU 
# from the AR Drone 
import roslib
import rospy

roslib.load_manifest('ardrone_test')

# Import the messages we're interested in
from ardrone_test.msg import Control

#messages = [1.0,1,0.5,2,0.3,3,0.7,4,0.5,5,0.8,6,1.0,1,0.5,2,0.3,3,0.7,4,0.5,5,0.8,6,1.0,1,0.5,2,0.3,3,0.7,4,0.5,5,0.8,6,1.0,1,0.5,2,0.3,3,0.7,4,0.5,5,0.8,6,1.0,1,0.5,2,0.3,3,0.7,4,0.5,5,0.8,6,1.0,1,0.5,2,0.3,3,0.7,4,0.5,5,0.8,6]
messages = [0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1,0.0,1]

rospy.init_node('ctrl_inter')
pub_Average = rospy.Publisher('/ardrone/ctrl_inter',Control)

a = 0
b = 1

r = rospy.Rate(1)
while not rospy.is_shutdown():
	c = 1
	envia = Control()
	if c < len(messages):
		envia.magnitud = messages[a]
		envia.direccion = messages[b]
		a = a + 2
		b = b + 2
		c = c + 1
		pub_Average.publish(envia)
	r.sleep()
