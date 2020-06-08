import math
import time
from machine import ADC

class MQ7(object):
	""" Class for dealing with MQ7 Sensor """
	# Constants needed for calculation
	COEFFICIENT_A = 19.32
	COEFFICIENT_B = -0.64
	# Load resistance on the sensor board
	R_LOAD = 10.0



	def __init__(self,pin,v_input):
		self.pin = pin
		self.v_input = v_input
	
	def __voltageConversion(self,int(value)):
		"""A private method"""
		return float(value*(self.v_input/1023.0))

	def getRatio(self):
		"""A private method"""
		adc = ADC(self.pin)  # Creating an ADC object
		value = adc.read()   # Reading the ADC pin
		v_output = float(self.__voltageConversion(value))
		return (self.v_input - v_output)/v_output

	def getPPM(self):
		"""Returning the value of carbon monoxide in PPM(Parts Per Million)"""
		return self.COEFFICIENT_A*math.pow(self.getRatio(),self.COEFFICIENT_B)

	def getSensorResistance(self):
		return R_LOAD*self.getRatio()