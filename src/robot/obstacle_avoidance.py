from robot.mock_gpio import GPIO
import time


# import RPi.GPIO as GPIO

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
        try:
            GPIO.output(self.trig_pin, GPIO.LOW)
            time.sleep(0.1)
            GPIO.output(self.trig_pin, GPIO.HIGH)
            time.sleep(0.00001)
            GPIO.output(self.trig_pin, GPIO.LOW)

            pulse_start = time.time()
            pulse_end = time.time()

            # Attente du signal de début d'écho
            while GPIO.input(self.echo_pin) == GPIO.LOW:
                pulse_start = time.time()
                if time.time() - pulse_start > 1:  # Timeout après 1 seconde
                    print("Erreur : Pas de réponse du capteur.")
                    return None

            # Attente de la fin du signal d'écho
            while GPIO.input(self.echo_pin) == GPIO.HIGH:
                pulse_end = time.time()
                if time.time() - pulse_end > 1:  # Timeout après 1 seconde
                    print("Erreur : Temps d'écho trop long.")
                    return None

            pulse_duration = pulse_end - pulse_start
            distance = pulse_duration * 17150
            distance = round(distance, 2)

            return distance
        except Exception as e:
            print(f"Erreur lors de la mesure de la distance : {e}")
            return None

    def setup_sensors(self):
        # Simulation de la configuration des capteurs
        print("Configuration des capteurs pour éviter les obstacles...")
        # Exemple de capteur avec GPIO, à ajuster selon votre matériel
        GPIO.setup(23, GPIO.IN)  # Pin 23 pour un capteur d'obstacle
        GPIO.setup(24, GPIO.IN)  # Pin 24 pour un autre capteur
        print("Capteurs d'obstacles configurés.")

    def cleanup(self):
        """Libère les ressources GPIO."""
        GPIO.cleanup()


def setup_sensors():
    return None