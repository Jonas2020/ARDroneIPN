#!/usr/bin/env python

# Simple project that create a topic to send data of IMU 
# from the AR Drone 2.0

# Import the ROS libraries
import roslib
import rospy

# Load the manifest file which through <depend package=... /> 
# will give us access to the project dependencies
roslib.load_manifest('ardrone_test')

# Import the messages we're interested in
from ardrone_autonomy.msg import Navdata
from ardrone_test.msg import Send

messages = []

def ReceiveData(data):
	messages.append(data)

rospy.init_node('IPNdrone_navdata_send')
sub_Navdata = rospy.Subscriber('/ardrone/navdata', Navdata, ReceiveData)
pub_Average = rospy.Publisher('/ardrone/ipn_navdata_send', Send)

r = rospy.Rate(2)
while not rospy.is_shutdown():
	if len(messages)>0:
		avgy = sum([m.rotY for m in messages])/len(messages)
		avgx = sum([m.rotX for m in messages])/len(messages)
		avgz = sum([m.rotZ for m in messages])/len(messages)
		avgalt = sum([m.altd for m in messages])/len(messages)
		avgax = sum([m.ax for m in messages])/len(messages)
		avgay = sum([m.ay for m in messages])/len(messages)
		avgaz = sum([m.az for m in messages])/len(messages)
		avgt = sum([m.temp for m in messages])/len(messages)
		messages = []

		avgmsg = Send()
		avgmsg.aat_pitch = avgy
		avgmsg.aat_roll = avgx
		avgmsg.aat_yaw = avgz
		avgmsg.aat_ax = avgax
		avgmsg.aat_ay = avgay
		avgmsg.aat_az = avgaz
		avgmsg.aat_alt = avgalt
		avgmsg.aat_temp = avgt
		avgmsg.textos = "Probando ARDrone"
		pub_Average.publish(avgmsg)
	r.sleep()



