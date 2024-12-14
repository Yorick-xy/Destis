# robot/obstacle_avoidance.py
from robot.mock_gpio import GPIO
import time
#import RPi.GPIO as GPIO

class ObstacleAvoidance:
    """Classe pour détecter et éviter les obstacles."""

    def __init__(self, trig_pin, echo_pin):
        """Initialise les pins du capteur à ultrasons."""
        self.trig_pin = trig_pin
        self.echo_pin = echo_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trig_pin, GPIO.OUT)
        GPIO.setup(self.echo_pin, GPIO.IN)

    def measure_distance(self):
        """Mesure la distance de l'obstacle en utilisant le capteur à ultrasons."""
        GPIO.output(self.trig_pin, GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(self.trig_pin, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(self.trig_pin, GPIO.LOW)
        
        pulse_start = time.time()
        pulse_end = time.time()
        
        while GPIO.input(self.echo_pin) == GPIO.LOW:
            pulse_start = time.time()
        
        while GPIO.input(self.echo_pin) == GPIO.HIGH:
            pulse_end = time.time()
        
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2)
        
        return distance

    def cleanup(self):
        """Libère les ressources GPIO."""
        GPIO.cleanup()
