import lcddriver
import time

display = lcddriver.lcd()

try:
    while True:
        print("Hello ChungAng University")
        display.lcd_display_string("Python Class!", 1)
        display.lcd_display_string("with physical", 2)
        time.sleep(2)                                     
        display.lcd_display_string("Nice meet you!", 1)
        display.lcd_display_string("              ", 2)
        time.sleep(2)
        display.lcd_clear()
        time.sleep(2)

except KeyboardInterrupt:
    print("Cleaning up!")
    display.lcd_clear()
