# src/ai/models.py

from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import joblib

class Model:
    def __init__(self, hidden_layer_sizes=(10,), max_iter=1000):
        """
        Initialisation du modèle de réseau de neurones.

        :param hidden_layer_sizes: tuple, dimensions des couches cachées (par défaut (10,))
        :param max_iter: int, nombre maximum d'itérations pour l'entrainement (par défaut 1000)
        """
        self.model = MLPClassifier(hidden_layer_sizes=hidden_layer_sizes, max_iter=max_iter)
        self.scaler = StandardScaler()  # Pour la normalisation des données

    def train(self, X_train, y_train):
        """Entraînement du modèle"""
        # Normalisation des données d'entraînement
        X_train_scaled = self.scaler.fit_transform(X_train)
        self.model.fit(X_train_scaled, y_train)

    def evaluate(self, X_test, y_test):
        """Évaluation du modèle sur un jeu de test"""
        # Normalisation des données de test
        X_test_scaled = self.scaler.transform(X_test)
        y_pred = self.model.predict(X_test_scaled)
        accuracy = accuracy_score(y_test, y_pred)
        return accuracy

    def save_model(self, filename):
        """Sauvegarde du modèle entraîné"""
        try:
            joblib.dump(self.model, filename)
            joblib.dump(self.scaler, f"{filename}_scaler.pkl")
            print(f"Modèle sauvegardé sous {filename}.")
        except Exception as e:
            print(f"Erreur lors de la sauvegarde du modèle : {e}")

    def load_model(self, filename):
        """Chargement d'un modèle sauvegardé"""
        try:
            self.model = joblib.load(filename)
            self.scaler = joblib.load(f"{filename}_scaler.pkl")
            print(f"Modèle chargé depuis {filename}.")
        except Exception as e:
            print(f"Erreur lors du chargement du modèle : {e}")


def load_trained_model(param):
    return None