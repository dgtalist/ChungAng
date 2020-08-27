import cv2
import dc_motor as motor

# Set the color recognition range
# If you want a different color, change it.(Blue)
Color_Lower = (36,130,46)
Color_Upper = (113, 255, 255)

# Camera Frame Range and Setting
Frame_Width  = 640
Frame_Height = 480
camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH,  Frame_Width)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, Frame_Height)

try:
    while True:
        #Camera Option
        (_, frame) = camera.read()
        # Do gaussian blur if needed
        frame = cv2.GaussianBlur(frame, (11, 11),1)

        # Convert to HSV color space
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Convert to binary with given color
        mask = cv2.inRange(hsv, Color_Lower, Color_Upper)

        #Do erode if needed
        #mask = cv2.erode(mask, None, iterations=2)

        # Do dilate if needed
        #mask = cv2.dilate(mask, None, iterations=2)

        # Find the contours
        #_, contours, _= cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2:]
        center = None
       
    
        if len(contours) > 0:
            # Find the max length of contours
            c = max(contours, key=cv2.contourArea)
          
            # Find the x, y, radius of given contours       
            ((x, y), radius) = cv2.minEnclosingCircle(c)

            # Find the moments
            M = cv2.moments(c)
          

            try:
                # mass center
                center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

                # process every frame
                cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)
                cv2.circle(frame, center, 5, (0, 0, 255), -1)
        
                # Forward, backward, Turn rules
                # Size of the recognized object           

                if radius < 25 and radius > 5 :
                    if center[0] > Frame_Width/2 + 55 :
                        motor.turnRight()
                      
                    elif center[0] < Frame_Width/2 -55 : #turnLeft_Area Set
                        motor.turnLeft()
                      
                    else:
                        motor.forward_2()                #Fast Run
                elif radius < 45 and radius > 25 :
                    if center[0] > Frame_Width/2 + 55 :
                        motor.turnRight()
                      
                    elif center[0] < Frame_Width/2 -55 :
                        motor.turnLeft()
                    else:
                        motor.forward_1()               #Low Run
       
                elif radius > 65:
                    motor.Reverse()
                                
                else:
                    motor.brake()
                          
            except:
                pass

        else:
            motor.stop()

        cv2.imshow("Frame", frame)  # if you don't need to display and the car will get faster
        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break

#except KeyboardInterrupt:

finally:
    motor.cleanup()
    camera.release()
    cv2.destroyAllWindows()