# robot/motor_control.py
import sys
import os

from mock_gpio import GPIO


# try:
#     import RPi.GPIO as GPIO
# except ImportError:
#     import mock_gpio as GPIO  # Utiliser le mock sur Mac

# Maintenant tu peux utiliser GPIO comme d'habitude sans erreur sur Mac
class MotorControl:
    def __init__(self, motor_pins):
        self.motor_pins = motor_pins
        GPIO.setmode(GPIO.BCM)
        for pin in motor_pins:
            GPIO.setup(pin, GPIO.OUT)
        self.pwm = [GPIO.PWM(pin, 100) for pin in motor_pins]
        for pwm in self.pwm:
            pwm.start(0)

    # Simulation
    def setup_motors():
        GPIO.setmode(GPIO.BCM)  # Utilise la méthode simulée
        GPIO.setup(18, GPIO.OUT)  # Simule la configuration du pin
        pwm = GPIO.PWM(18, 1000)  # Simule la création du PWM
        pwm.start(50)  # Démarre le PWM avec un cycle de travail de 50%
        return pwm

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
        GPIO.cleanup()


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
