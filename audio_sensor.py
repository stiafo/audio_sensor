#! /usr/bin/python

import subprocess
import random
import time
import atexit

import RPi.GPIO as GPIO

pin_left = 8
pin_right = 22
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin_number, GPIO.IN)

def cleanup():
    GPIO.cleanup()

atexit.register(cleanup)

tracks_as_string = str((subprocess.run("ls /media/hoyby/KINGSTON | grep '.mp3'", shell=True, capture_output=True).stdout), "utf-8")
tracks = tracks_as_string.split("\n")
tracks.pop(-1)

while True:
    pin_state_right = GPIO.input(pin_right) # Returns 1 if HIGH and 0 if LOW
    pin_state_left = GPIO.input(pin_left)

    if pin_state_right == 1 or pin_state_left == 1:
        sleep(1)

        # Only play track if the other sensor is not activated within a second (probably a car)
        if not (pin_state_left == 1 and pin_state_right == 1):
            track=tracks[random.randint(0, len(tracks)-1)]
            subprocess.run(f"mpg123 --stereo /media/hoyby/KINGSTON/{track}", shell=True)
            sleep(14)

        sleep(5)

    time.sleep(1)
