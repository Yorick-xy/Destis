# robot/motor_control.py
import sys

#from mock_gpio import GPIO
from .mock_gpio import GPIO
#from src.robot.mock_gpio import GPIO
#from mock_gpio import GPIO
import os
import sys

folder_path = os.path.join(os.environ["HOME"], "Documents/05_Dev/Destis/src/robot")
sys.path.append(folder_path)

import mock_gpio as GPIO


#if os.getenv("USE_MOCK_GPIO", "false").lower() == "true":
#    from mock_gpio import GPIO
#else:
#    import RPi.GPIO as GPIO

try:
    import RPi.GPIO as GPIO
    GPIO_AVAILABLE = True
except ImportError:
    try:
        import mock_gpio as GPIO
        GPIO_AVAILABLE = False
    except ImportError:
        print("Erreur : Aucune bibliothèque GPIO disponible. Utilisez un Raspberry Pi ou un module de simulation.")
        raise

class MotorControl:
    def __init__(self, motor_pins):
        self.motor_pins = motor_pins

        if GPIO_AVAILABLE:
            print("Utilisation des GPIO du Raspberry Pi.")
            GPIO.setmode(GPIO.BCM)
            for pin in motor_pins:
                GPIO.setup(pin, GPIO.OUT)
            self.pwm = [GPIO.PWM(pin, 100) for pin in motor_pins]
            for pwm in self.pwm:
                pwm.start(0)
        else:
            print("Simulation des moteurs avec mock_gpio.")
            self.pwm = [self.setup_motor_simulation(pin) for pin in motor_pins]

    # Méthode pour simuler l'initialisation des moteurs (si on est en simulation)
    def setup_motor_simulation(self, pin):
        print(f"Simulation de l'initialisation du moteur sur le pin {pin}")
        pwm = GPIO.PWM(pin, 1000)  # Simule la création du PWM
        pwm.start(50)  # Démarre le PWM avec un cycle de travail de 50%
        return pwm

    def init_motors(self):
        # Simulation de l'initialisation des moteurs
        print("Initialisation des moteurs...")
        GPIO.setmode(GPIO.BCM)
        # Exemple de configuration de pins, vous pouvez les ajuster en fonction de votre setup
        GPIO.setup(17, GPIO.OUT)  # Pin 17 pour un moteur
        GPIO.setup(18, GPIO.OUT)  # Pin 18 pour un autre moteur
        print("Moteurs initialisés.")

    def move_forward(self, speed=50):
        self._set_motor_speed(speed)
        print("Déplacement en avant")

    def move_backward(self, speed=50):
        self._set_motor_speed(-speed)
        print("Déplacement en arrière")

    def stop(self):
        self._set_motor_speed(0)
        print("Arrêt du robot")

    def _set_motor_speed(self, speed):
        for pwm in self.pwm:
            pwm.ChangeDutyCycle(abs(speed))

    def cleanup(self):
        if GPIO_AVAILABLE:
            GPIO.cleanup()
        else:
            print("Simulation terminée.")

# class MotorControl:
#     """Classe pour contrôler les moteurs du robot."""

#     def __init__(self, motor_pins):
#         """Initialise les pins des moteurs."""
#         self.motor_pins = motor_pins
#         GPIO.setmode(GPIO.BCM)
#         for pin in motor_pins:
#             GPIO.setup(pin, GPIO.OUT)
#         self.pwm = [GPIO.PWM(pin, 100) for pin in motor_pins]
#         for pwm in self.pwm:
#             pwm.start(0)

#     def move_forward(self, speed=50):
#         """Déplace le robot en avant avec une vitesse donnée."""
#         self._set_motor_speed(speed)
#         print("Déplacement en avant")

#     def move_backward(self, speed=50):
#         """Déplace le robot en arrière avec une vitesse donnée."""
#         self._set_motor_speed(-speed)
#         print("Déplacement en arrière")

#     def stop(self):
#         """Arrête tous les moteurs."""
#         self._set_motor_speed(0)
#         print("Arrêt du robot")

#     def _set_motor_speed(self, speed):
#         """Définit la vitesse des moteurs."""
#         for pwm in self.pwm:
#             pwm.ChangeDutyCycle(abs(speed))

#     def cleanup(self):
#         """Libère les ressources GPIO."""
#         GPIO.cleanup()
def init_motors():
    return None