import RPi.GPIO as GPIO
from time import sleep

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def adc(comp, dac):
    for val in range(256):
        GPIO.output(dac, decimal2binary(i))
        sleep(.01)
        compVal = GPIO.input(comp)
        if compVal == 1:
            return val
    # If something goes wrong:
    return -1 

GPIO.setmode(GPIO.BCM)

dac = [, , , , , , , ]
comp = 
troyka = 

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)


try:
    GPIO.output(troyka, 1)
    while True:
        out = adc(comp, dac)
        voltage = out / 256 * 3.3
        print(voltage, 'V')

finally:
    GPIO.output(troyka, 0)
    GPIO.output(dac, 0)
    GPIO.cleanup()
