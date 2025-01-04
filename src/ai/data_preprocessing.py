# src/ai/data_preprocessing.py

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

class DataPreprocessing:
    def __init__(self):
        # Initialisation de l'imputer pour remplacer les valeurs manquantes
        self.imputer = SimpleImputer(strategy='mean')  # Remplacer les valeurs manquantes par la moyenne
        # Initialisation du scaler pour normaliser les données
        self.scaler = StandardScaler()

    def preprocess_data(self, data):
        """
        Prétraitement des données :
        - Remplace les valeurs manquantes par la moyenne.
        - Normalise les données pour avoir une moyenne de 0 et un écart type de 1.

        Paramètres :
        data (array-like ou DataFrame) : Données à prétraiter.

        Retourne :
        data_scaled (array) : Données après imputations et normalisation.
        """
        try:
            # Vérifie que l'entrée est un tableau NumPy ou un DataFrame
            if not isinstance(data, (np.ndarray, pd.DataFrame)):
                raise ValueError("Les données doivent être sous forme de tableau NumPy ou DataFrame.")

            # Imputation des valeurs manquantes
            data_imputed = self.imputer.fit_transform(data)

            # Normalisation des données
            data_scaled = self.scaler.fit_transform(data_imputed)

            return data_scaled

        except ValueError as ve:
            print(f"Erreur de valeur : {ve}")
            return None
        except Exception as e:
            print(f"Erreur lors du prétraitement des données : {e}")
            return None

    def save_transformers(self, imputer_filename, scaler_filename):
        """Sauvegarder les objets d’imputation et de normalisation pour une réutilisation future."""
        try:
            # Sauvegarder l’imputer et le scaler avec pickle (ou joblib)
            import joblib
            joblib.dump(self.imputer, imputer_filename)
            joblib.dump(self.scaler, scaler_filename)
            print("Les transformateurs ont été sauvegardés avec succès.")
        except Exception as e:
            print(f"Erreur lors de la sauvegarde des transformateurs : {e}")

    def load_transformers(self, imputer_filename, scaler_filename):
        """Charger les objets d’imputation et de normalisation depuis un fichier sauvegardé."""
        try:
            # Charger les objets d’imputation et de normalisation
            import joblib
            self.imputer = joblib.load(imputer_filename)
            self.scaler = joblib.load(scaler_filename)
            print("Les transformateurs ont été chargés avec succès.")
        except Exception as e:
            print(f"Erreur lors du chargement des transformateurs : {e}")


def load_data(data_path):
    # Simulation du chargement des données
    print(f"Chargement des données depuis {data_path}...")
    # Exemple de données chargées
    data = {"example_data": [1, 2, 3, 4]}  # Exemple de données
    return data
