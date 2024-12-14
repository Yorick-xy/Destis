# home_automation/mqtt_client.py
import paho.mqtt.client as mqtt

class MqttClient:
    def __init__(self, broker_address="localhost", port=1883):
        self.client = mqtt.Client()
        self.client.connect(broker_address, port)

    def publish(self, topic, message):
        self.client.publish(topic, message)
