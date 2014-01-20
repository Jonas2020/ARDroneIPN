#!/usr/bin/env python

import roslib
import rospy

roslib.load_manifest('ardrone_test')

# Import the messages we're interested in
from ardrone_test.msg import Control

direc = [0]
mag = [0.0]
frec = [2]

def ReceiveData(data):
	mag[0] = data.magnitud
	
	if mag[0] > 0.05:
		direc[0] = 6		#derecha
	elif mag[0] < -0.05:
		direc[0] = 5		#izquierda
	elif (mag[0] >= -0.05) and (mag[0] <= 0.05):
		direc[0] = 1	
	#print direc[0]
	#print frec[0]
	
rospy.init_node('inter')
sub_Navdata = rospy.Subscriber('/ardrone/ctrl_inter', Control, ReceiveData)
pub_Ctrl = rospy.Publisher('/ardrone/ctrl_interno', Control)


r = rospy.Rate(frec[0])
while not rospy.is_shutdown():
	if direc[0] == 1:
		#time.sleep(0.5)
		hola = Control()
		hola.magnitud = mag[0]
		hola.direccion = direc[0]
		pub_Ctrl.publish(hola)
	elif direc[0] == 5:
		hola = Control()
		hola.magnitud = mag[0]
		hola.direccion = direc[0]
		pub_Ctrl.publish(hola)
	elif direc[0] == 6:
		hola = Control()
		hola.magnitud = mag[0]
		hola.direccion = direc[0]
		pub_Ctrl.publish(hola)		
	r.sleep()
