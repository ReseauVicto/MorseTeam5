#!/usr/bin/env python

from gpiozero import LED
from time import sleep

led = LED(17)

led.on()
sleep(2)
led.off()
sleep(1)
led.on()
sleep(2)
led.off()
sleep(1)
led.on()
sleep(2)
led.off()
