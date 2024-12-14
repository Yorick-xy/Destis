# src/ai/data_preprocessing.py

import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

class DataPreprocessing:
    def __init__(self):
        self.imputer = SimpleImputer(strategy='mean')  # Remplacer les valeurs manquantes par la moyenne
        self.scaler = StandardScaler()  # Normalisation des données

    def preprocess_data(self, data):
        """Prétraitement des données : imputation et normalisation"""
        # Imputation des valeurs manquantes
        data_imputed = self.imputer.fit_transform(data)

        # Normalisation des données
        data_scaled = self.scaler.fit_transform(data_imputed)

        return data_scaled
