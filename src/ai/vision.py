# src/ai/vision.py

import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions

class Vision:
    def __init__(self, model_path=None):
        """
        Initialisation de la classe Vision.
        Si un chemin de modèle est fourni, charge le modèle spécifié.
        """
        if model_path:
            self.model = load_model(model_path)
        else:
            # Charge un modèle pré-entrainé (par exemple, ResNet50)
            self.model = ResNet50(weights='imagenet')
        
    def process_image(self, img_path, target_size=(224, 224)):
        """
        Charge et prétraite une image pour qu'elle soit compatible avec le modèle.
        
        :param img_path: Le chemin de l'image à traiter
        :param target_size: La taille cible pour redimensionner l'image
        :return: L'image prête à être passée au modèle
        """
        img = image.load_img(img_path, target_size=target_size)
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)  # Ajoute une dimension pour le batch
        img_array = preprocess_input(img_array)  # Prétraitement spécifique à ResNet50
        return img_array

    def predict(self, img_path):
        """
        Effectue une prédiction sur l'image spécifiée.
        
        :param img_path: Le chemin de l'image à prédire
        :return: La prédiction du modèle sous forme d'étiquette et de probabilité
        """
        # Traitement de l'image
        img_array = self.process_image(img_path)
        
        # Prédiction
        predictions = self.model.predict(img_array)
        
        # Décoder les prédictions pour obtenir les classes et probabilités
        decoded_predictions = decode_predictions(predictions, top=3)[0]
        
        # Retourner les 3 meilleures prédictions
        return decoded_predictions

    def display_image(self, img_path):
        """
        Affiche l'image à partir du chemin spécifié.
        
        :param img_path: Le chemin de l'image à afficher
        """
        img = cv2.imread(img_path)
        cv2.imshow("Image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def save_image(self, img, output_path):
        """
        Sauvegarde une image dans le répertoire spécifié.
        
        :param img: L'image à sauvegarder
        :param output_path: Le chemin où l'image sera sauvegardée
        """
        cv2.imwrite(output_path, img)

    def extract_faces(self, img_path, output_path="faces_detected.jpg"):
        """
        Extrait les visages d'une image et les enregistre dans un fichier.
        
        :param img_path: Le chemin de l'image
        :param output_path: Le chemin de sortie pour l'image avec les visages détectés
        """
        # Charger un classificateur pré-entrainé pour la détection de visages
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        
        # Charger l'image
        img = cv2.imread(img_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Détection des visages
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
        
        # Dessiner des rectangles autour des visages
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        # Sauvegarder l'image avec les visages détectés
        self.save_image(img, output_path)

if __name__ == "__main__":
    # Exemple d'utilisation du module
    vision = Vision(model_path=None)  # Utilise un modèle pré-entrainé par défaut (ResNet50)

    # Prédiction sur une image
    predictions = vision.predict('data/images/example.jpg')
    print("Predictions:", predictions)

    # Affichage d'une image
    vision.display_image('data/images/example.jpg')

    # Détection de visages
    vision.extract_faces('data/images/example.jpg', 'data/temp/faces_detected.jpg')
