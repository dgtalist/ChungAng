import RPi.GPIO as GPIO
import time

sensor = 4
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN)

print("Detect Ready~!")
time.sleep(3)

try:
    while True:
        if GPIO.input(sensor) == 1:
            print("Detect!")
            time.sleep(1)
        if GPIO.input(sensor) == 0:
            time.sleep(0.2)
        
except KeyboardInterrupt:
    print("Stopped by User")
    GPIO.cleanup
