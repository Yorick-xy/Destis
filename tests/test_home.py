# tests/test_home.py

import unittest
from src.home_automation import mqtt_client, device_control

class TestHomeAutomation(unittest.TestCase):

    def test_mqtt_connection(self):
        # Tester la connexion au broker MQTT
        connected = mqtt_client.connect_to_broker()
        self.assertTrue(connected)  # Vérifier que la connexion a réussi

    def test_device_control(self):
        # Tester le contrôle d'un appareil
        response = device_control.control_device('light', 'on')
        self.assertEqual(response, 'Device light is turned on')  # Supposons que la réponse soit cette chaîne

if __name__ == "__main__":
    unittest.main()
