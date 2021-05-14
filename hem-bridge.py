import paho.mqtt.client as mqtt
from kafka import KafkaProducer
import time
import random
import json

def on_connect(client, userdata, flags, rc):
    print("已连接 返回码: " + str(rc))

def on_message(client, userdata, msg):
    data = json.loads(str(msg.payload,'utf-8'))
    data['record_time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(data)
    producer.send('message',data)

def on_disconnect(client, userdata, rc):
    client.reconnect()
    print("客户端已重连！")

def on_subscribe(client, userdata, mid, granted_qos):
    print("订阅主题成功！")

def on_unsubscribe(client, userdata, mid):
    print("代理取消订阅!")
    client.subscribe("/devices/+")
    print("正在重新订阅")

producer = KafkaProducer(bootstrap_servers='192.168.10.30:9092,192.168.10.30:9093,192.168.10.30:9094',value_serializer=lambda v: json.dumps(v).encode('utf-8'))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect
client.on_subscribe = on_subscribe
client.on_unsubscribe = on_unsubscribe

client.connect('www.cgblogs.top', 1883, 15)
client.subscribe("/devices/+")

while True:
    client.loop()
