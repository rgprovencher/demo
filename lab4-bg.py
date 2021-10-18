#!/usr/bin/python3.7

import RPi.GPIO as GPIO
import time

RED = 26
GREEN = 16
BLUE = 13

LED_ARR = [RED,GREEN,BLUE]

GPIO.setmode(GPIO.BCM)

GPIO.setup(LED_ARR, GPIO.OUT)

redLED = GPIO.PWM(RED, 100)
greenLED = GPIO.PWM(GREEN, 100)
blueLED = GPIO.PWM(BLUE, 100)

pwm = [redLED, greenLED, blueLED]

for i in pwm:
  i.start(0) #start all LEDs off

while True:
  with open("led-settings.txt", 'r') as f:

    settings = split(f.read())  # create an array [ LED_selection , brighntess]

    LED = pwm[int(settings[0])]
    dutyCycle = float(settings[1])

    LED.ChangeDutyCycle(dutyCycle)
    time.sleep(0.2)