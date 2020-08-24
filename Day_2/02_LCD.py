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

    
[ 라이브러리 설치 ]
$ git clone https://github.com/the-raspberry-pi-guy/lcd
$ cd lcd
~/lcd $ sudo sh install.sh
~/lcd $ reboot
