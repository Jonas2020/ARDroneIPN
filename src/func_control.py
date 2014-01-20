#!/usr/bin/env python

import roslib
import rospy

roslib.load_manifest('ardrone_test')

# Import the messages we're interested in
from ardrone_test.msg import Control

direc = [0]
mag = [0.0]

def ReceiveData(data):
	if data.direccion == 1:
		direc[0] = 1
		mag[0] = data.magnitud
	elif data.direccion == 2:
		direc[0] = 2
		mag[0] = data.magnitud
	elif data.direccion == 3:
		direc[0] = 3
		mag[0] = data.magnitud
	elif data.direccion == 4:
		direc[0] = 4
		mag[0] = data.magnitud
	elif data.direccion == 5:
		direc[0] = 5
		mag[0] = data.magnitud
	elif data.direccion == 6:
		direc[0] = 6
		mag[0] = data.magnitud
		
rospy.init_node('func_control')
sub_Navdata = rospy.Subscriber('/ardrone/ctrl_inter', Control, ReceiveData)

r = rospy.Rate(1)
while not rospy.is_shutdown():
	if direc[0] == 1:
		print "La direccion del vuelo sera derecha"
		print "La magnitud del vuelo sera: {0:.3f}".format(mag[0]) + "\n"
		direc = [0]
	elif direc[0] == 2:
		print "La direccion del vuelo sera izquierda"
		print "La magnitud del vuelo sera: {0:.3f}".format(mag[0]) + "\n"
		direc = [0]
	elif direc[0] == 3:
		print "La direccion del vuelo sera adelante"
		print "La magnitud del vuelo sera: {0:.3f}".format(mag[0]) + "\n"
		direc = [0]
	elif direc[0] == 4:
		print "La direccion del vuelo sera atras"
		print "La magnitud del vuelo sera: {0:.3f}".format(mag[0]) + "\n"
		direc = [0]
	elif direc[0] == 5:
		print "La direccion del vuelo sera giro horario"
		print "La magnitud del vuelo sera: {0:.3f}".format(mag[0]) + "\n"
		direc = [0]
	elif direc[0] == 6:
		print "La direccion del vuelo sera giro antihorario"
		print "La magnitud del vuelo sera: {0:.3f}".format(mag[0]) + "\n"
		direc = [0]
	r.sleep()
