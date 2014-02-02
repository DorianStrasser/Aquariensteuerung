#!/usr/bin/python
import PWMRGBW as RGB
import time

RGB.init()
RGB.setPixel(200, 0, 0)
time.sleep(3)
RGB.setPixel(0, 100, 120)
time.sleep(3)
RGB.finalize()

