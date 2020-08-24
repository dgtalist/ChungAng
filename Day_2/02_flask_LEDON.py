from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "SMART HOME"

@app.route("/led/on")
def led_on():
    return "LED ON"   

@app.route("/led/off")
def led_off():
    return "LED OFF" 

if __name__ == "__main__":
    app.run(host="0.0.0.0") #localhost
