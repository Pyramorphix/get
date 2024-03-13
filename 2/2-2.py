import RPi.GPIO as GPIO
from time import sleep as zzz

dac = [, , , , , , , ]
num = [0, 0, 0, 0, 0, 0, 0, 0]
dec_num = 0
for i in range(7, -1, -1):
    if dec_num >= 2**i:
        num[7-i] = 1
        dec_num -= 2**i

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

GPIO.output(dac, num)
zzz(10)
GPIO.output(dac, 0)


GPIO.cleanup()