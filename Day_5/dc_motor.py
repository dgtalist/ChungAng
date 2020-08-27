import RPi.GPIO as GPIO
import time
#Delay time
t = 0.01
#Set Used GPIO
Motor_R1_Pin = 21
Motor_R2_Pin = 20
Motor_L1_Pin = 27
Motor_L2_Pin = 17
Enable_1 = 23
Enable_2 = 24
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(Motor_R1_Pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Motor_R2_Pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Motor_L1_Pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Motor_L2_Pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Enable_1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Enable_2, GPIO.OUT, initial=GPIO.LOW)
pwm_e1 = GPIO.PWM(Enable_1, 500)
pwm_e2 = GPIO.PWM(Enable_2, 500)
pwm_e1.start(0)
pwm_e2.start(0)

# Use reverse rotation to hold the brakes.
def brake():
   pwm_e1.ChangeDutyCycle(10)
   pwm_e2.ChangeDutyCycle(10)
   GPIO.output(Motor_R1_Pin, False)
   GPIO.output(Motor_R2_Pin, True)
   GPIO.output(Motor_L1_Pin, False)
   GPIO.output(Motor_L2_Pin, True)
   time.sleep(t)
   GPIO.output(Motor_R1_Pin, False)
   GPIO.output(Motor_R2_Pin, False)
   GPIO.output(Motor_L1_Pin, False)
   GPIO.output(Motor_L2_Pin, False)
   print("BR")

# Use Stalled status
def stop():
   pwm_e1.ChangeDutyCycle(100)
   pwm_e2.ChangeDutyCycle(100)
   GPIO.output(Motor_R1_Pin, False)
   GPIO.output(Motor_R2_Pin, False)
   GPIO.output(Motor_L1_Pin, False)
   GPIO.output(Motor_L2_Pin, False)
   print("s")

# Low speed
def forward_1():
   pwm_e1.ChangeDutyCycle(40)
   pwm_e2.ChangeDutyCycle(40)
   GPIO.output(Motor_R1_Pin, True)
   GPIO.output(Motor_R2_Pin, False)
   GPIO.output(Motor_L1_Pin, True)
   GPIO.output(Motor_L2_Pin, False)
   print("F_L")
   time.sleep(t)

# Fast speed
def forward_2():
   pwm_e1.ChangeDutyCycle(65)
   pwm_e2.ChangeDutyCycle(65)
   GPIO.output(Motor_R1_Pin, True)
   GPIO.output(Motor_R2_Pin, False)
   GPIO.output(Motor_L1_Pin, True)
   GPIO.output(Motor_L2_Pin, False)
   print("F_F")
   time.sleep(t)

# Reverse
def Reverse():
   pwm_e1.ChangeDutyCycle(45)
   pwm_e2.ChangeDutyCycle(45)
   GPIO.output(Motor_R1_Pin, False)
   GPIO.output(Motor_R2_Pin, True)
   GPIO.output(Motor_L1_Pin, False)
   GPIO.output(Motor_L2_Pin, True)
   print("Re")
   time.sleep(t)

# turnLeft
def turnLeft():
   pwm_e1.ChangeDutyCycle(100)
   pwm_e2.ChangeDutyCycle(100)
   GPIO.output(Motor_R1_Pin, True)
   GPIO.output(Motor_R2_Pin, False)
   GPIO.output(Motor_L1_Pin, False)
   GPIO.output(Motor_L2_Pin, True)
   print ("T_L")
   
   time.sleep(t)

# turnRight 
def turnRight():
   pwm_e1.ChangeDutyCycle(100)
   pwm_e2.ChangeDutyCycle(100)
   GPIO.output(Motor_R1_Pin, False)
   GPIO.output(Motor_R2_Pin, True)
   GPIO.output(Motor_L1_Pin, True)
   GPIO.output(Motor_L2_Pin, False)
   print("T_R")
   time.sleep(t)

#If you want to test the motor, use the script below

'''
while True:
   a = input("")
   a = int(a)
   if a == 1:
      turnRight()
   elif a == 2:
      turnLeft()
   elif a == 3:
      forward_1()
   elif a == 4:
      Reverse()
'''
#GPIO Initialization
def cleanup():
   stop()  
   pwm_e1.stop()
   pwm_e2.stop()
   GPIO.cleanup()
