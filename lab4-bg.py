#!/usr/bin/python3.7

import RPi.GPIO as GPIO
import time
import datetime
import json

GPIO.setmode(GPIO.BCM)

# declare pin #s
RED = 26
GREEN = 16
BLUE = 13
LED_ARR = [RED,GREEN,BLUE]


GPIO.setup(LED_ARR, GPIO.OUT)

# setting up PWMs
redLED = GPIO.PWM(RED, 100)
greenLED = GPIO.PWM(GREEN, 100)
blueLED = GPIO.PWM(BLUE, 100)
pwm = [redLED, greenLED, blueLED]



for i in pwm:
  i.start(0) #start all LEDs off

while True:
  with open("/usr/lib/cgi-bin/demo/led-settings.txt", 'r') as f:

    data = json.load(f)

    LED = int(data["LED"])
    dutyCycle = float(data["Brightness"])

    # Old code, still works for troubleshooting but using json formatting instead
    # settings = f.read().split(',')  # create an array [ LED_selection , brighntess]
    # LED = pwm[int(settings[0])]
    # dutyCycle = float(settings[1])


    LED.ChangeDutyCycle(dutyCycle)

    # close the door behind you
    f.close()



    # troubleshooting
    with open("lab4_bg_log.txt", 'w') as log:
      log.write("I have set {} to {}".format(LED, dutyCycle))
      log.write(datetime.now())

  
  time.sleep(0.2)

  