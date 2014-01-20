#!/usr/bin/env python
import roslib
roslib.load_manifest('ardrone_test')
import sys
import rospy
import cv
import time

from procesaIma import *
from math import *

from ardrone_test.msg import Control
from ardrone_autonomy.msg import Navdata
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

ROLL = [0.0]
PITCH = [0.0]
YAW = [0.0]

def ReceiveData(data):
	ROLL[0] = data.rotX
	PITCH[0] = data.rotY
	YAW[0] = data.rotZ

pub_Average = rospy.Publisher('/ardrone/ctrl_inter', Control)
sub_Navdata = rospy.Subscriber('/ardrone/navdata', Navdata,ReceiveData)
	
class image_converter:

  def __init__(self):
    cv.NamedWindow("IPN Drone Video OpenCV", 1)
    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("/ardrone/image_raw",Image,self.callback)
    self.vision = Vision()
    self.var = 0
    self.cuenta = 0
    self.t0 = 0

  def callback(self,data):
	try:
	  cv_image = self.bridge.imgmsg_to_cv(data, "bgr8")
	except CvBridgeError, e:
	  print e
	  
	if self.cuenta == 0:
		self.t0 = time.clock()
	if self.cuenta == 600:
		print "Tiempo = %0.4f segundos" %((time.clock() - self.t0)/self.cuenta)
	if self.cuenta < 600:
		print "Control --->  %0.3f" %(self.vision.control1)
	self.cuenta = self.cuenta + 1
	self.vision.roll = pi*ROLL[0]/180 		
	self.vision.pitch = pi*PITCH[0]/180 	
	#self.vision.yaw = pi*YAW[0]/180
	#print "Roll --> %0.3f   Pitch --> %0.3f" %(self.vision.roll, self.vision.pitch)
	self.vision.src =  cv_image
	#Se toma una imagen de cada 3 para no alentar la vision artificial
	if self.var % 4 == 0: #valores de 3-5
		self.var=0
	self.vision.deteccionPuntoFuga(self.var)
	self.vision.control()
	signal = self.vision.control1
	
	envia = Control()
	envia.direccion = 0
	envia.magnitud = self.vision.control1
	pub_Average.publish(envia)
	
	cv.ShowImage("IPN Drone Video OpenCV", self.vision.color_dst)
	cv.WaitKey(2)
	self.var = self.var + 1
 

def main(args):
  ic = image_converter()
  rospy.init_node('openCV', anonymous=True)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print "Shutting down"
  cv.DestroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
