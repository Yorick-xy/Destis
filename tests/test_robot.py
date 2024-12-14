# tests/test_robot.py

import unittest
from src.robot import motor_control, obstacle_avoidance, navigation

class TestRobot(unittest.TestCase):

    def test_motor_control(self):
        # Tester l'initialisation des moteurs
        motor_control.init_motors()
        self.assertTrue(motor_control.is_motors_initialized())  # Vérifier si les moteurs sont initialisés

    def test_obstacle_avoidance(self):
        # Tester la configuration des capteurs d'évitement d'obstacles
        sensors_initialized = obstacle_avoidance.setup_sensors()
        self.assertTrue(sensors_initialized)  # Vérifier que les capteurs sont configurés correctement

    def test_navigation(self):
        # Tester l'initialisation de la navigation
        navigation_initialized = navigation.initialize_navigation()
        self.assertTrue(navigation_initialized)  # Vérifier que la navigation est prête

if __name__ == "__main__":
    unittest.main()
