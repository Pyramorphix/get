import RPi.GPIO as GPIO

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]


GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setup(dac, GPIO.OUT)

try:
    while True:
        a = input('Number (0-255, q to exit): ')
        if a == 'q':
            print('exiting...')
            break
        if int(a) != float(a):
            print('The number is not an integer\n')
        elif int(a) < 0:
            print('The number is negative\n')
        elif int(a) > 255:
            print('The number is too large\n')
        else:
            a = int(a)
            print("Voltage:", a*3.3/255, '\n')
            GPIO.output(dac, decimal2binary(a))
except ValueError:
    print('Wrong input format')
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()