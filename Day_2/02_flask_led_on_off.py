from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT, initial=GPIO.LOW)

@app.route("/")
def hello():
    return "SMART HOME"

@app.route("/led/on")
def led_on():
    GPIO.output(14, GPIO.HIGH)
    return "LED ON"   

@app.route("/led/off")
def led_off():
    GPIO.output(14, GPIO.LOW)
    return "LED OFF"

@app.route("/gpio/cleanup")
def gpio_cleanup():
    GPIO.cleanup()
    return "GPIO CLEAN UP"

if __name__ == "__main__":
    app.run(host="0.0.0.0") #localhost
