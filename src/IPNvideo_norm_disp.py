#!/usr/bin/env python

# Import the ROS libraries and load the manifest file which through 
# <depend package=... /> will give us access to the project dependencies
import roslib; roslib.load_manifest('ardrone_test')
import rospy

# Load the DroneController class, which handles interactions with the drone, 
# and the IPNVideoDisplay class, which handles video display
from IPNvideo_norm import IPNVideoDisplay

# Finally the GUI libraries
from PySide import QtCore, QtGui

# Setup the application
if __name__=='__main__':
	import sys
	# Firstly we setup a ros node, so that we can communicate with the other packages
	rospy.init_node('IPNvideo_norm_disp')

	# Now we construct our Qt Application and associated controllers and windows
	app = QtGui.QApplication(sys.argv)
	display = IPNVideoDisplay()

	# executes the QT application
	display.show()
	status = app.exec_()

	# and only progresses to here once the application has been shutdown
	rospy.signal_shutdown('Great Flying!')
	sys.exit(status)
