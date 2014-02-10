#!/usr/bin/python
import Adafruit_BBIO.PWM as PWM
import time
import PWMRGBW
import logging


logging.basicConfig(level=logging.DEBUG)
currentColor =PWMRGBW.LEDDriver()
#currentColor.setColor(50,255,255)
#time.sleep(2)
#currentColor.setColor(90,200,90)
#time.sleep(2)
currentColor.setColor(230,0,50)
#time.sleep(2)
currentColor.setColor(0,255,255,5)
time.sleep(2)
