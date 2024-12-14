# src/ai/testing.py

import unittest
from .core import AI

class TestAI(unittest.TestCase):
    def test_decision_making(self):
        ai = AI()
        sensor_data = [1, 2, 3]  # Exemple de données de capteurs
        ai.process_input(sensor_data)
        ai.make_decision()
        self.assertEqual(ai.output_action(), "action attendue")
