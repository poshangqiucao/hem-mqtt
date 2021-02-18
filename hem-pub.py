import paho.mqtt.client as mqtt
import time
import random
import json

def on_connect(client, userdata, flags, rc):
    print("Connected with result code: " + str(rc))

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect('www.cgblogs.top', 1883, 15)
while True:
    data = {}
    data['temperature'] = random.randint(0,50)
    data['humidity'] = random.randint(25,95)
    data['air'] = random.randint(10,1000)
    data['light'] = random.randint(0,1000)
    data['pressure'] = random.randint(850,1100)
    data_str = json.dumps(data)
    print(data_str)
    client.publish('/devices/message', payload=data_str, qos=0)
    time.sleep(3)