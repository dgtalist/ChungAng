import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

# Steering Motor Pins_left
steering_enable_1 = 23 # Physical Pin 15
in1 = 17 # Physical Pin 11
in2 = 27 # Physical Pin 13

# Steering Motor Pins_right
steering_enable_2 = 24 # Physical Pin 22
in3 = 21 # Physical Pin 16
in4 = 20 # Physical Pin 18

GPIO.setmode(GPIO.BCM) # Use GPIO numbering instead of physical numbering
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
GPIO.setup(steering_enable_1, GPIO.OUT)
GPIO.setup(steering_enable_2, GPIO.OUT)

# Steering Motor Control_left
GPIO.output(in1, GPIO.HIGH) 
GPIO.output(in2, GPIO.LOW)
steering1 = GPIO.PWM(steering_enable_1, 1000) # set the switching frequency to 1000 Hz
steering1.stop()

# Steering Motor Control_right
GPIO.output(in3, GPIO.HIGH)
GPIO.output(in4, GPIO.LOW)
steering2 = GPIO.PWM(steering_enable_2, 1000) # set the switching frequency to 1000 Hz
steering2.stop()

time.sleep(1)

steering1.start(100) # starts the motor at 100% PWM signal-> (1 * Battery Voltage) - driver's loss
steering2.start(100) # starts the motor at 100% PWM signal-> (1 * Battery Voltage) - driver's loss


time.sleep(3)

steering1.stop()
steering2.stop()
