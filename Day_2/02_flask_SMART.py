from flask import Flask, request
from flask import render_template
import RPi.GPIO as GPIO

app = Flask(__name__)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT, initial=GPIO.LOW)

@app.route("/")
def hello():
    return render_template("index.html")
    return "SMART HOME"

@app.route("/led/on")
def led_on():
    try:
        GPIO.output(14, GPIO.HIGH)
        return "ok"
    except expression as identifier:
        return "fail"

@app.route("/led/off")
def led_off():
    try:
        GPIO.output(14, GPIO.LOW)
        return "ok"
    except expression as identifier:
        return "fail"

@app.route("/gpio/cleanup")
def gpio_cleanup():
    GPIO.cleanup()
    return "GPIO CLEAN UP"

if __name__ == "__main__":
    app.run(host="192.168.0.204") #localhost
