#! /usr/bin/python

import subprocess
import random
import time
import atexit

import RPi.GPIO as GPIO

pin_number = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin_number, GPIO.IN)

def cleanup():
    GPIO.cleanup()

atexit.register(cleanup)

tracks_as_string = str((subprocess.run("ls /media/hoyby/KINGSTON | grep '.mp3'", shell=True, capture_output=True).stdout), "utf-8")
tracks = tracks_as_string.split("\n")
tracks.pop(-1)

while True:
    pin_state = GPIO.input(pin_number) # Returns 1 if HIGH and 0 if LOW

    if pin_state == 1:
        print("PIN is high")
        track=tracks[random.randint(0, len(tracks)-1)]

        subprocess.run(f"mpg123 --stereo /media/hoyby/KINGSTON/{track}", shell=True)
        time.sleep(19)

    time.sleep(1)
