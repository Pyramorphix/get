import RPi.GPIO as GPIO
from time import sleep as zzz

leds = [, , , , , , , ]

GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)

for i in range(3):
    for led in leds:
        GPIO.output(led, 1)
        zzz(.2)
        GPIO.output(led, 0)
GPIO.output(leds, 0)


GPIO.cleanup()