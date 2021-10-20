#!/usr/bin/python3.7

import RPi.GPIO as GPIO
import time

RED = 26
GREEN = 16
BLUE = 13

LED_ARR = [RED, BLUE, GREEN]

GPIO.setup(LED_ARR, GPIO.OUT)

redLED = GPIO.PWM(RED, 100)
greenLED = GPIO.PWM(GREEN, 100)
blueLED = GPIO.PWM(BLUE, 100)

pwm = [redLED, greenLED, blueLED]

for i in pwm:
  i.start(0)
  time.sleep(.2)
  i.ChangeDutyCycle(30)
  time.sleep(.2)
  i.ChangeDutyCycle(60)
  time.sleep(.2)
  i.ChangeDutyCycle(100)
  time.sleep(.2)
  i.ChangeDutyCycle(0)


GPIO.cleanup
  

