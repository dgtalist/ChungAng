import RPi.GPIO as GPIO
import time, datetime

now = datetime.datetime.now()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
 
 #GPIO ports for the 7seg pins
segments =  (11,4,23,8,7,10,18,25)

 
for segment in segments:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, 0)
 
    #Digit 1
    GPIO.setup(22, GPIO.OUT)
    GPIO.output(22, 0) #Off initially
    #Digit 2
    GPIO.setup(27, GPIO.OUT)
    GPIO.output(27, 0) #Off initially
    #Digit 3
    GPIO.setup(17, GPIO.OUT)
    GPIO.output(17, 0) #Off initially
    #Digit 4
    GPIO.setup(24, GPIO.OUT)
    GPIO.output(24, 0) #Off initially

null = [0,0,0,0,0,0,0]
zero = [1,1,1,1,1,1,0]
one = [0,1,1,0,0,0,0]
two = [1,1,0,1,1,0,1]
three = [1,1,1,1,0,0,1]
four = [0,1,1,0,0,1,1]
five = [1,0,1,1,0,1,1]
six = [1,0,1,1,1,1,1]
seven = [1,1,1,0,0,0,0]
eight = [1,1,1,1,1,1,1]
nine = [1,1,1,1,0,1,1]

def print_segment(charector):
    if charector == 1:
        for i in range(7):
            GPIO.output(segments[i], one[i])

    if charector == 2:
        for i in range(7):
            GPIO.output(segments[i], two[i])

    if charector == 3:
        for i in range(7):
            GPIO.output(segments[i], three[i])

    if charector == 4:
        for i in range(7):
            GPIO.output(segments[i], four[i])

    if charector == 5:
        for i in range(7):
            GPIO.output(segments[i], five[i])

    if charector == 6:
        for i in range(7):
            GPIO.output(segments[i], six[i])

    if charector == 7:
        for i in range(7):
            GPIO.output(segments[i], seven[i])

    if charector == 8:
        for i in range(7):
            GPIO.output(segments[i], eight[i])

    if charector == 9:
        for i in range(7):
            GPIO.output(segments[i], nine[i])

    if charector == 0:
        for i in range(7):
            GPIO.output(segments[i], zero[i])        
            
    return;

while 1:

    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute
    h1 = hour/10
    h2 = hour % 10
    m1 = minute /10
    m2 = minute % 10
    print (h1,h2,m1,m2)
  
    delay_time = 0.001 #delay to create virtual effect
    
    GPIO.output(7, 1) #Turn on Digit One
    print_segment (h1) #Print h1 on segment
    time.sleep(delay_time)
    GPIO.output(7, 0) #Turn off Digit One

    GPIO.output(8, 1) #Turn on Digit One
    print_segment (h2) #Print h1 on segment
    GPIO.output(10, 1) #Display point On
    time.sleep(delay_time)
    GPIO.output(10, 0) #Display point Off
    GPIO.output(8, 0) #Turn off Digit One

    GPIO.output(25, 1) #Turn on Digit One
    print_segment (m1) #Print h1 on segment
    time.sleep(delay_time)
    GPIO.output(25, 0) #Turn off Digit One

    GPIO.output(24, 1) #Turn on Digit One
    print_segment (m2) #Print h1 on segment
    time.sleep(delay_time)
    GPIO.output(24, 0) #Turn off Digit One
 
   # time.sleep(1)
