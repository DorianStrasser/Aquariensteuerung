#!/usr/bin/python
import Adafruit_BBIO.PWM as PWM
import time

PRED = "P8_19"
PBLUE = "P8_13"
PGREEN = "P9_14"

def init():
	PWM.start(PRED, 0)
	PWM.start(PBLUE, 0)
	PWM.start(PGREEN, 0)

def setPixel(R, G, B):
	lr = float(float(R)/255.0*100.0)
	lg = float(float(G)/255.0*100.0)
	lb = float(float(B)/255.0*100.0)
	print("Red: " + str(lr))
	print("Green: " + str(lg))
	print("Blue: " + str(lb))	
	PWM.set_duty_cycle(PRED, lr)
	PWM.set_duty_cycle(PBLUE, lb)
	PWM.set_duty_cycle(PGREEN, lg)
	
def finalize():
	PWM.stop(PRED)
	PWM.stop(PGREEN)
	PWM.stop(PBLUE)
	PWM.cleanup()

