# src/ai/models.py

from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

class Model:
    def __init__(self):
        # Création d'un modèle de réseau de neurones avec 1 couche cachée de 10 neurones
        self.model = MLPClassifier(hidden_layer_sizes=(10,), max_iter=1000)

    def train(self, X_train, y_train):
        """Entraînement du modèle"""
        self.model.fit(X_train, y_train)

    def evaluate(self, X_test, y_test):
        """Évaluation du modèle sur un jeu de test"""
        y_pred = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        return accuracy
