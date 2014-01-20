#!/usr/bin/env python

import roslib
import rospy

roslib.load_manifest('ardrone_test')

# Import the messages we're interested in
from ardrone_autonomy.msg import Navdata
from std_msgs.msg import String

messages = []

def ReceiveData(data):
	messages.append(data)

rospy.init_node('ipn_min_publisher')
sub_Navdata = rospy.Subscriber('/ardrone/navdata', Navdata, ReceiveData)
pub_Average = rospy.Publisher('/ardrone/average_pitch', String)

r = rospy.Rate(1)

while not rospy.is_shutdown():
  if len(messages)>0:
    avgp = sum([m.rotY for m in messages])/len(messages)
    avgy = sum([m.rotX for m in messages])/len(messages)
    messages = []

    avgmsg = String()
    avgmsg.data = 'Average Pitch: {0:.3f}'.format(avgp) + '  Average Yaw: {0:.3f}'.format(avgy)
    pub_Average.publish(avgmsg)
  r.sleep()
