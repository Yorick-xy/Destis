from robot import motor_control, obstacle_avoidance, navigation
from ai import data_preprocessing, models, nlp
from home_automation import mqtt_client, device_control
from utils import logger, exception_handler, config
from utils.config import load_config
from ai import data_preprocessing
import sys
import logging
import os

# Ajouter le chemin du dossier src
sys.path.append('/Users/yorick/Documents/05_Dev/Destis/src')
config_path = os.path.join(os.path.dirname(__file__), 'utils/config/config.yaml')

# Chargement de la configuration
config = load_config(config_path)

# Configuration du logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def main():
    try:
        # Initialisation des logs
        logger.info("Initialisation des moteurs...")

        # === Initialisations ===
        logger.info("Configuration des capteurs pour éviter les obstacles...")
        obstacle_avoidance.setup_sensors()

        logger.info("Initialisation de la navigation...")
        navigation.initialize_navigation()

        # === Préparation des données pour l'IA ===
        logger.info("Chargement des données...")
        data = data_preprocessing.load_data(config['data_path'])  # Utilisation de la fonction load_data

        logger.info("Chargement du modèle pré-entraîné...")
        model = models.load_trained_model(config['model_path'])

        logger.info("Configuration du modèle NLP...")
        nlp.setup_nlp_model()

        # === Automatisation domestique ===
        logger.info("Connexion au broker MQTT...")
        mqtt_client.connect_to_broker(config['mqtt_broker'])

        # Mode interactif
        print("Bienvenue dans Destis. Entrez une commande :")
        while True:
            command = input(">> ").strip().lower()
            if command == "quitte":
                print("Au revoir !")
                break
            elif command == "allume lumière":
                device_control.control_device('light', 'on')
                print("Lumière allumée")
            elif command == "déplace robot":
                navigation.move_to_target()
            else:
                print("Commande non reconnue.")

    except FileNotFoundError as e:
        logger.error(f"Fichier non trouvé : {e}")
    except ConnectionError as e:
        logger.error(f"Erreur de connexion : {e}")
    except Exception as e:
        logger.error(f"Erreur inattendue : {e}")
        exception_handler.handle_error(e)

if __name__ == "__main__":
    print(f"Chemin du fichier config.yaml : {config_path}")
    main()