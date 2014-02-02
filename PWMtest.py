#!/usr/bin/python
import Adafruit_BBIO.PWM as PWM
import time

PRED = "P8_19"
PBLUE = "P8_13"
PGREEN = "P9_14"

PWM.start(PRED, 0)
PWM.start(PBLUE, 100)
PWM.start(PGREEN, 100)
for i in range(0, 100):
	PWM.set_duty_cycle(PRED, float(i))
	PWM.set_duty_cycle(PBLUE, float(0))
	PWM.set_duty_cycle(PGREEN, float(i))
	time.sleep(.1)
PWM.stop(PRED)
PWM.stop(PGREEN)
PWM.stop(PBLUE)
PWM.cleanup()
