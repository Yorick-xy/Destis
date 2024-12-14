# tests/test_utils.py

import unittest
from src.utils import config, logger, exception_handler

class TestUtils(unittest.TestCase):

    def test_config_loading(self):
        # Tester le chargement des configurations YAML/JSON
        robot_config = config.load_config('src/utils/config/robot_config.yaml')
        self.assertIsInstance(robot_config, dict)  # Vérifier que la configuration est un dictionnaire

    def test_logger_setup(self):
        # Tester l'initialisation du logger
        logger.setup_logging()
        self.assertTrue(logger.is_logging_initialized())  # Supposons qu'il y a une méthode pour vérifier l'initialisation

    def test_exception_handler(self):
        # Tester le gestionnaire d'exceptions
        try:
            raise ValueError("Test exception")
        except Exception as e:
            response = exception_handler.handle_error(e)
            self.assertEqual(response, "Handled: Test exception")  # Vérifier que l'exception est gérée correctement

if __name__ == "__main__":
    unittest.main()
