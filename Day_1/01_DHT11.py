import time
import Adafruit_DHT as dht

while True:
    h,t = dht.read_retry(dht.DHT11,4)
    print('Humidity', h, '%', ', temperature', t, 'C’)
    time.sleep(1)

          
          
[ 사전 설치 모듈 ]
sudo apt-get update 
sudo apt-get install python3-pip 
sudo python3 -m pip install --upgrade pip setuptools wheel
sudo pip3 install Adafruit_DHT
cd Adafruit_Python_DHT
./Adafruit_Python_DHT/$ sudo python3 setup.py install
