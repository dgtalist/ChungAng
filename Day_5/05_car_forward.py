import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

left_pwm = 23
left1 = 17
left2 = 27
right_pwm = 24
right1 = 21
right2 = 20

GPIO.setmode(GPIO.BCM)
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

# forward
left_pwm_act.start(100)
right_pwm_act.start(100)
time.sleep(1)

left_pwm_act.stop()
right_pwm_act.stop()
