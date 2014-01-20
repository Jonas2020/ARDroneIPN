#!/usr/bin/python
from math import *
import cv

class Vision:
	def __init__(self):
		self.src = 0
		self.dst = 0
		self.color_dst = 0
		self.pitch = 0
		self.roll = 0
		self.yaw = 0
		#parametros de la cam.
		self.n=640
		self.m=480
		self.Ln = 1.29
		self.Lfn = 1.78
		self.Lm = 1.98
		self.Lfm = 1.37
		self.alpha = pi/6/1.3
		self.foco = self.n/(2*tan(self.alpha))
		#horizonte
		self.h_rho=0
		self.h_theta=0
		#vertical
		self.v_rho=0
		self.v_theta=0
		#origen
		self.ox=0
		self.oy=0
		#interseccion
		self.intersecta=0
		self.x=0
		self.y=0
		#zona de busqueda
		self.epsilon = 100
		self.longitud = self.n*(1.0/2.0+1.0/3.0)
		self.resolucion = 30
		self.cuadros = [0]*int(2*self.longitud/self.resolucion+2)
		self.lines = 0
		#salida
		self.indice=0
		self.Prom = 4
		self.indiceProm = 0
		self.controles = [0.0]*int(self.Prom)
		self.control1=0
		self.blancos=0
		#contador auxiliar
		self.cuenta = 0
		
	def resize(self, height, width):
		src = cv.CreateMat(height, width, cv.CV_8UC3)
		cv.Resize(self.src, src,cv.CV_INTER_LINEAR)
		self.src = src
		self.dst = cv.CreateImage(cv.GetSize(self.src), 8, 1)
		self.color_dst = cv.CreateImage(cv.GetSize(self.src), 8, 3)
	
	def canny(self, threshold1, threshold2, aperture_size):
		cv.CvtColor(self.src,self.dst,cv.CV_BGR2GRAY)
		cv.Smooth(self.dst,self.dst,cv.CV_GAUSSIAN,3,3) 
		#cv.Threshold(self.dst, self.dst, 120, 255, cv.CV_THRESH_BINARY)
		#cv.Erode(self.dst,self.dst,None,2)
		cv.Canny(self.dst, self.dst, threshold1, threshold2, aperture_size)
		cv.CvtColor(self.dst, self.color_dst, cv.CV_GRAY2BGR)
		self.cruz(self.n/2,self.m/2,5,cv.RGB(0,255,0))

	def hough(self, rho, theta, threshold):
		self.lines = cv.HoughLines2(self.dst, cv.CreateMemStorage(0), cv.CV_HOUGH_STANDARD, rho, theta, threshold, 0, 0)
		
	def busqueda(self,numL):
		self.cuadros = [0]*int(2*self.longitud/self.resolucion+2)
		i=0
		for (rho, theta) in self.lines[:numL]:
			i=i+1
			if abs(theta-self.h_theta)>0.1 and pi/2-abs(theta-self.h_theta)>0.1:
				self.recta(rho,theta,1,cv.RGB(255, 0, 0))
				for (rho2, theta2) in self.lines[i:numL]: 
					if abs(theta2-self.h_theta)>0.1 and pi/2-abs(theta2-self.h_theta)>0.1:
						self.interseccion(rho,theta,rho2,theta2)
						x=self.x
						y=self.y
						self.cambioCoordenadas(self.x,self.y)
						if self.intersecta and abs(self.y)<self.epsilon and abs(self.x)<self.longitud:
							indice=int((self.x+self.longitud)/self.resolucion)
							self.cuadros[indice]=self.cuadros[indice]+1
							self.cruz(x,y,5,cv.RGB(0,255,0))
		
	def recta(self, rho, theta, tam, color):
		a = cos(theta)
		b = sin(theta)
		x0 = a * rho
		y0 = b * rho
		pt1 = (cv.Round(x0 + 1000*(-b)), cv.Round(y0 + 1000*(a)))
		pt2 = (cv.Round(x0 - 1000*(-b)), cv.Round(y0 - 1000*(a)))
		cv.Line(self.color_dst, pt1, pt2, color, tam, 8)
	
	def cruz(self, x, y, tam, color):
		cv.Line(self.color_dst, (x-tam,y), (x+tam,y), color, 2, 8 )
		cv.Line(self.color_dst, (x,y-tam), (x,y+tam), color, 2, 8 )

	def horizonte(self):
		self.h_theta = pi/2 - self.roll
		rho = self.foco * tan(self.pitch)
		theta_c = pi/2 - self.roll - atan2(self.m,self.n)
		self.h_rho = norma(self.n/2,self.m/2) * cos(theta_c) - rho
		self.recta(self.h_rho,self.h_theta,2,cv.RGB(0, 255, 0))

	def vertical(self):
		self.v_theta = - self.roll
		self.v_rho = (self.m*sin(self.v_theta)+self.n*cos(self.v_theta))/2
		self.recta(self.v_rho,self.v_theta,2,cv.RGB(0, 0, 255))

	def origen(self):
		self.interseccion(self.h_rho,self.h_theta,self.v_rho,self.v_theta)
		self.ox=self.x
		self.oy=self.y
		self.cruz(self.x,self.y,5,cv.RGB(0,255,0))

	def interseccion(self, rho1, theta1, rho2, theta2):
		if theta1==theta2:
			self.intersecta=0
		else:
			self.x=int(rho1*cos(theta1)+(rho2-rho1*cos(theta1-theta2))/sin(theta1-theta2)*sin(theta1))
        		self.y=int(rho1*sin(theta1)-(rho2-rho1*cos(theta1-theta2))/sin(theta1-theta2)*cos(theta1))
			self.intersecta=1

	def cambioCoordenadas(self, x, y):
		self.x = int((x-self.ox)*cos(self.v_theta)+(y-self.oy)*sin(self.v_theta))
		self.y = int((y-self.oy)*cos(self.v_theta)-(x-self.ox)*sin(self.v_theta))

	def deteccionPuntoFuga(self,op):
		if op==0:
			self.resize(self.m,self.n)
			self.canny(90, 180, 3)
			self.horizonte()
			self.vertical()
			self.origen()
			self.hough(1, pi / 360, 80)
			self.busqueda(12)
	
	def control(self):	
		self.indice = self.cuadros.index(max(self.cuadros))
		if self.cuadros[self.indice] > 0:
			self.indiceProm = self.indiceProm + 1
			self.blancos = 0
			self.control1 = 0.5 * (self.indice-18)/18
			
			#Inicia Promediado
			if self.indiceProm < self.Prom:
				self.controles[self.indiceProm-1] = self.control1
				control1 = sum(self.controles)/self.indiceProm
			else:
				self.controles[self.indiceProm % self.Prom]= self.control1
				self.control1 = sum(self.controles)/self.Prom
				if self.indiceProm % self.Prom == 0:
					self.indiceProm = self.Prom
			#Termina Promediado
			
		#Indica ausencia de punto de fuga y aterriza		
		elif self.blancos<10:
			if abs(self.control1)<=0.07:
				self.controles = [0.0]*int(self.Prom)
				self.indiceProm = 0
				self.blancos = self.blancos +1
			else: 
				self.blancos=0
		else:
			self.control1 = 1.3
		
def norma(x,y): return sqrt(pow(x,2)+pow(y,2));
