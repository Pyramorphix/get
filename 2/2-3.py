import RPi.GPIO as GPIO
from time import sleep as zzz

leds = [, , , , , , , ]
aux = [, , , , , , , ]

GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(aux, GPIO.IN)

while True:
    for i in range(7):
        GPIO.output(leds[i], GPIO.input(aux[i]))