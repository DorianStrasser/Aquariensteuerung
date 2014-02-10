#!/usr/bin/python
import Adafruit_BBIO.PWM as PWM
import time
import logging

# Define Pins
PRED = "P8_19"
PBLUE = "P8_13"
PGREEN = "P9_14"


class LEDDriver(object):
	def __init__(self,r=0,g=0,b=0):
		self.red = PWMchannel(PRED,r)
		self.green = PWMchannel(PGREEN,g)
		self.blue = PWMchannel(PBLUE,b)
		
	def setColor(self,r,g,b,duration=0):
		stepsPerSecond = 8.0
		if duration == 0:
			self.red.setChannelColor(r)
			self.green.setChannelColor(g)
			self.blue.setChannelColor(b)
		else:
			steps = duration * stepsPerSecond
			logging.debug("Stepcount: " + str(steps))
			stepRed = (r - self.red.getChannelColor()) / steps
			stepBlue = (b - self.blue.getChannelColor()) / steps
			stepGreen = (g - self.green.getChannelColor()) / steps
			logging.debug("Red step: " + str(stepRed))
			logging.debug("Blue step: " + str(stepBlue))
			logging.debug("Green step: " + str(stepGreen))
			logging.debug("Sleep time: " + str(1/stepsPerSecond))

			for i in range(0, int(steps)):
				self.red.setChannelColor(self.red.getChannelColor()+stepRed)
				self.green.setChannelColor(self.green.getChannelColor()+stepGreen)
				self.blue.setChannelColor(self.blue.getChannelColor()+stepBlue)
				time.sleep(1/stepsPerSecond)

class PWMchannel(object):
	def __init__(self, channel, colorRGB=0):
		self.channel = channel
		logging.debug("Channel " + channel + " created")
		self.colorRGB = colorRGB
		PWM.start(channel,colorRGB)

	def getChannelColor(self):
		return self.colorRGB


	def setChannelColor(self,value):
		PWM.set_duty_cycle(self.channel, self.RGBtoPercentage(value))
		logging.debug("Set channel " + self.channel + " to " + str(value))
		self.colorRGB = value
	
	def RGBtoPercentage(self,rgb):
		return float(rgb)/255.0*100.0
	
	def __del__(self):
		PWM.stop(self.channel)
		PWM.cleanup()
