import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

left_pwm = 23
left1 = 17
left2 = 27
right_pwm = 24
right1 = 21
right2 = 20

GPIO.setup(left_pwm, GPIO.OUT)
GPIO.setup(left1, GPIO.OUT)
GPIO.setup(left2, GPIO.OUT)
GPIO.setup(right_pwm, GPIO.OUT)
GPIO.setup(right1, GPIO.OUT)
GPIO.setup(right2, GPIO.OUT)

# left motor CCW rotation
GPIO.output(left1, GPIO.LOW)
GPIO.output(left2, GPIO.HIGH)
left_pwm_act = GPIO.PWM(left_pwm, 1000)
left_pwm_act.stop()

# right motor CW rotation
GPIO.output(right1, GPIO.HIGH)
GPIO.output(right2, GPIO.LOW)
right_pwm_act = GPIO.PWM(right_pwm, 1000)
right_pwm_act.stop()

TRGI = 5
ECHO = 6
print("Distance measurement with Ultrasonic")

GPIO.setup(TRGI, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRGI, False)
print("Waiting for sensor to settle")
time.sleep(2)

try:
    while True:
        GPIO.output(TRGI, True)
        time.sleep(0.00001)
        GPIO.output(TRGI, False)
        while GPIO.input(ECHO) == 0:
            start = time.time()
        while GPIO.input(ECHO) == 1:
            stop = time.time()
        check_time = stop - start
        distance = check_time*34300/2
        print("Distance : %.1f cm" %distance)
        if distance >= 5:
            left_pwm_act.start(100)
            right_pwm_act.start(100)
        elif distance < 5:
            left_pwm_act.start(0)
            right_pwm_act.start(0)
#        time.sleep(0.4)

except KeyboardInterrupt:
    print("Measuremenet stopped by User")
    GPIO.cleanup()
