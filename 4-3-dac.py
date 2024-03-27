import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

pwm = 19
freq = 0.5
duty_cycle = 0

GPIO.setup(pwm, GPIO.OUT)

try:
    a = GPIO.PWM(pwm, freq)
    duty_cycle = int(input("Duty cycle (0-100): "))
    while True:
        a.start(duty_cycle)
        duty_cycle = int(input("Duty cycle (0-100): "))
        a.stop()
finally:
    GPIO.output(pwm, 0)
    GPIO.cleanup()