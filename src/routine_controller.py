#!/usr/bin/env python

import roslib; roslib.load_manifest('ardrone_test')
import rospy
import time

# Carga la clase DroneController, que mantiene las interacciones con el 
# Drone,y la clase IPNVideoDisplay, que mantiene el video normal.
from drone_controller import BasicDroneController
from IPNvideo_norm import IPNVideoDisplay
from ardrone_test.msg import Control
from std_msgs.msg import String

# Librerias para la GUI
from PySide import QtCore, QtGui

pausa = 0.01		# Constante ajuste de pausas
mag = [0.0]			# Variable
direc = [0]			# Variable
conta = [0]			# Variable

# Aqui se define el mapeo del teclado para el controlador
# (notese que python no enumera, por eso usamos una clase)
class KeyMapping(object):
	PitchForward     = QtCore.Qt.Key.Key_E
	PitchBackward    = QtCore.Qt.Key.Key_D
	RollLeft         = QtCore.Qt.Key.Key_S
	RollRight        = QtCore.Qt.Key.Key_F
	IncreaseAltitude = QtCore.Qt.Key.Key_Q
	DecreaseAltitude = QtCore.Qt.Key.Key_A
	Takeoff          = QtCore.Qt.Key.Key_Y
	Land             = QtCore.Qt.Key.Key_H
	Emergency        = QtCore.Qt.Key.Key_Space
	Prueba			 = QtCore.Qt.Key.Key_P
	Itera			 = QtCore.Qt.Key.Key_I	

# Definiciones del controlador, notese que se extiendo la clase DroneVideoDisplay
class KeyboardController(IPNVideoDisplay):
	def __init__(self):
		super(KeyboardController,self).__init__()

		# Nodo al cual nos Subscribimos y Publicamos
		self.sub_Ctrl = rospy.Subscriber('/ardrone/ctrl_inter', Control, self.ReceiveCtrl)
		self.pub_Average = rospy.Publisher('/ardrone/ctrl_interno', String)
		self.pitch = 0
		self.roll = 0
		self.yaw_velocity = 0 
		self.z_velocity = 0				
		self.activahoover = 0			
		self.veceshoover = 0
		self.veceshooverfin = 0
		self.cuentagder = 0
		self.cuentagizq = 0
		self.cuentafre  = 0

	def ReceiveCtrl(self,DataCtrl):
		#Solo estas dos lineas se deja para utilizar la tecla (I)
		mag[0] = DataCtrl.magnitud
		direc[0] = DataCtrl.direccion
		if (len(conta) > 10):
			if((self.activahoover == 1) and (self.veceshoover < 10)):
				self.rutina(7)
				self.veceshoover += 1	
				self.cuentagder = 0
				self.cuentagizq = 0
				self.cuentafre  = 0
				self.veceshooverfin = 0			
			elif mag[0] > 0.07 and mag[0] < 1:
				self.veceshoover = 0	
				self.activahoover = 0
				self.rutina(6)
				self.cuentagder += 1			
			elif mag[0] < -0.07:
				self.veceshoover = 0
				self.activahoover = 0
				self.rutina(5)
				self.cuentagizq += 1
			elif (mag[0] >= -0.07) and (mag[0] <= 0.07):
				self.veceshoover = 0
				self.activahoover = 0
				self.rutina(1)
				self.cuentafre += 1
				if (self.cuentafre >= 25):
					self.activahoover = 1
			elif mag[0] >= 1 and mag[0] < 2:
				self.veceshoover = 0
				self.activahoover = 0
				self.veceshooverfin += 1
				self.rutina(7)
				if(self.veceshooverfin >= 5):
					controller.SendLand()
					sal = String()
					sal.data = "Aterriza"
					self.pub_Average.publish(sal)
		elif len(conta) <= 10:
			conta.append(1)	
			time.sleep(1)
		
	def rutina(self,x):
		if x == 1:
			self.frentepulse()
			sal = String()
			sal.data = "Frente"
			self.pub_Average.publish(sal)
		elif x == 2:		
			self.atraspulse()
			sal = String()
			sal.data = "Atras"
			self.pub_Average.publish(sal)
		elif x == 3:		
			self.izqpulse()
			sal = String()
			sal.data = "Izquierda"
			self.pub_Average.publish(sal)
		elif x == 4:			
			self.derpulse()
			sal = String()
			sal.data = "Derecha"
			self.pub_Average.publish(sal)
		elif x == 5:			
			self.girizqpulse()
			sal = String()
			sal.data = "Giro Izquierda"
			self.pub_Average.publish(sal)
		elif x == 6:
			self.girderpulse()
			sal = String()
			sal.data = "Giro derecha"
			self.pub_Average.publish(sal)
		elif x == 7:
			self.hoover()
			sal = String()
			sal.data = "Hoover"
			self.pub_Average.publish(sal)

	def moverel(self,y):
		time.sleep(pausa)
		if y == 1: 
			self.pitch -= 1
		elif y == 2:
			self.pitch -= -1
		elif y == 3:
			self.roll -= 1
		elif y == 4:
			self.roll -= -1
		elif y == 5:
			self.yaw_velocity -= 1
		elif y == 6:
			self.yaw_velocity -= -1

	def frentepulse(self):
		self.pitch += 1
		controller.SetCommand(self.roll, self.pitch, self.yaw_velocity, self.z_velocity)
		self.moverel(1)
	
	def atraspulse(self):
		self.pitch += -1
		controller.SetCommand(self.roll, self.pitch, self.yaw_velocity, self.z_velocity)
		self.moverel(2)
	
	def izqpulse(self):
		self.roll += 1
		controller.SetCommand(self.roll, self.pitch, self.yaw_velocity, self.z_velocity)
		self.moverel(3)

	def derpulse(self):
		self.roll += -1
		controller.SetCommand(self.roll, self.pitch, self.yaw_velocity, self.z_velocity)
		self.moverel(4)
	
	def girizqpulse(self):
		self.yaw_velocity += 1
		controller.SetCommand(self.roll, self.pitch, self.yaw_velocity, self.z_velocity)
		self.moverel(5)
	
	def girderpulse(self):
		self.yaw_velocity += -1
		controller.SetCommand(self.roll, self.pitch, self.yaw_velocity, self.z_velocity)
		self.moverel(6)
		
	def hoover(self):
		self.pitch = 0
		self.roll = 0
		self.yaw_velocity = 0 
		self.z_velocity = 0	
		controller.SetCommand(self.roll, self.pitch, self.yaw_velocity, self.z_velocity)
							
# We add a keyboard handler to the DroneVideoDisplay to react to keypresses
	def keyPressEvent(self, event):
		key = event.key()

		# If we have constructed the drone controller and the key is not generated from an auto-repeating key
		if controller is not None and not event.isAutoRepeat():
			# Handle the important cases first!
			if key == KeyMapping.Emergency:
				controller.SendEmergency()
			elif key == KeyMapping.Takeoff:
				controller.SendTakeoff()
			elif key == KeyMapping.Land:
				controller.SendLand()
			else:
				# Now we handle moving, notice that this section 
				# is the opposite (+=) of the keyrelease section
				if key == KeyMapping.RollLeft:
					self.roll += 1
				elif key == KeyMapping.RollRight:
					self.roll += -1				

				elif key == KeyMapping.PitchForward:
					self.pitch += 1
				elif key == KeyMapping.PitchBackward:
					self.pitch += -1

				elif key == KeyMapping.DecreaseAltitude:
					self.z_velocity += -1
					
				elif key == KeyMapping.IncreaseAltitude:
					self.z_velocity += 1
				#Senal que se envia cada vez que se presiona la tecla (I)
				#Es necesario dejar unicamente las dos primeras lineas de
				#la funcion ReceiveCtrl
				elif key == KeyMapping.Itera:
					if mag[0] > 0.07:
						self.rutina(6)
					elif mag[0] < -0.07:
						self.rutina(5)
					elif (mag[0] >= -0.07) and (mag[0] <= 0.07):
						self.rutina(1)
					
			# finally we set the command to be sent. The controller handles sending this at regular intervals
			controller.SetCommand(self.roll, self.pitch, self.yaw_velocity, self.z_velocity)

	def keyReleaseEvent(self,event):
		key = event.key()

		# If we have constructed the drone controller and the key is not generated from an auto-repeating key
		if controller is not None and not event.isAutoRepeat():
			# Note that we don't handle the release of emergency/takeoff/landing keys here, there is no need.
			# Now we handle moving, notice that this section is the opposite (-=) of the keypress section
			if key == KeyMapping.DecreaseAltitude:
				self.z_velocity -= -1

			elif key == KeyMapping.RollLeft:
				self.roll -= 1
			elif key == KeyMapping.RollRight:
				self.roll -= -1

			elif key == KeyMapping.PitchForward:
				self.pitch -= 1
			elif key == KeyMapping.PitchBackward:
				self.pitch -= -1
				
			elif key == KeyMapping.IncreaseAltitude:
				self.z_velocity -= 1
	
			# finally we set the command to be sent. The controller handles sending this at regular intervals
			controller.SetCommand(self.roll, self.pitch, self.yaw_velocity, self.z_velocity)

# Setup the application
if __name__=='__main__':
	import sys
	# Firstly we setup a ros node, so that we can communicate with the other packages
	rospy.init_node('routine_controller')

	# Now we construct our Qt Application and associated controllers and windows
	app = QtGui.QApplication(sys.argv)
	controller = BasicDroneController()
	display = KeyboardController()

	display.show()

	# executes the QT application
	status = app.exec_()

	# and only progresses to here once the application has been shutdown
	rospy.signal_shutdown('Great Flying!')
	sys.exit(status)
