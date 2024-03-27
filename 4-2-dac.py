import RPi.GPIO as GPIO
from time import sleep

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]


GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setup(dac, GPIO.OUT)

try:
    T = int(input("Enter delay (ms): "))
    while True:
        for i in range(511):
            GPIO.output(dac, decimal2binary(255 - abs(i - 255)))
            sleep(T/1000)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()