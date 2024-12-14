# tests/test_ai.py

import unittest
from src.ai import data_preprocessing, models, nlp

class TestAI(unittest.TestCase):

    def test_data_preprocessing(self):
        # Tester la fonction de prétraitement des données
        data = data_preprocessing.load_data('data/sample_data.csv')
        self.assertIsInstance(data, list)  # Supposons que la fonction retourne une liste

    def test_model_loading(self):
        # Tester le chargement d'un modèle
        model = models.load_trained_model('data/models/model.h5')
        self.assertIsNotNone(model)  # Le modèle ne doit pas être None

    def test_nlp_model(self):
        # Tester le setup du modèle NLP
        nlp_model = nlp.setup_nlp_model()
        self.assertTrue(nlp_model.is_initialized())  # Supposons qu'il y a une méthode pour vérifier l'initialisation

if __name__ == "__main__":
    unittest.main()
