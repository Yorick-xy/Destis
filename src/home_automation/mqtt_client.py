# home_automation/mqtt_client.py
import paho.mqtt.client as mqtt
import yaml
import logging

class MqttClient:
    def __init__(self, config_file='config/mqtt_config.yaml'):
        """Initialisation du client MQTT"""
        # Charger la configuration à partir du fichier YAML
        self.config = self.load_config(config_file)

        # Initialiser le client MQTT avec les paramètres de la configuration
        self.client = mqtt.Client(client_id=self.config['mqtt']['client_id'])
        self.client.username_pw_set(self.config['mqtt']['yorick'], self.config['mqtt']['root'])

        # Configurer le callback de connexion
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        try:
            self.client.connect(self.config['mqtt']['broker'], self.config['mqtt']['port'], self.config['mqtt']['keepalive'])
        except Exception as e:
            logging.error(f"Erreur de connexion au broker MQTT : {e}")
            raise

    def load_config(self, config_file):
        """Charge le fichier de configuration YAML"""
        try:
            with open(config_file, 'r') as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            logging.error(f"Le fichier de configuration {config_file} est introuvable.")
            raise
        except yaml.YAMLError as e:
            logging.error(f"Erreur lors du chargement du fichier YAML : {e}")
            raise

    def publish(self, topic, message):
        """Publie un message sur le topic spécifié"""
        try:
            self.client.publish(topic, message)
            logging.info(f"Message publié sur {topic}: {message}")
        except Exception as e:
            logging.error(f"Erreur lors de la publication du message : {e}")

    def subscribe(self, topic):
        """Souscrit à un topic spécifique"""
        try:
            self.client.subscribe(topic)
            logging.info(f"Souscription au topic {topic}")
        except Exception as e:
            logging.error(f"Erreur lors de la souscription au topic {topic}: {e}")

    def loop_start(self):
        """Démarre la boucle de gestion des messages"""
        self.client.loop_start()

    def loop_stop(self):
        """Arrête la boucle de gestion des messages"""
        self.client.loop_stop()

    def on_connect(self, client, userdata, flags, rc):
        """Callback appelé lors de la connexion au broker MQTT"""
        if rc == 0:
            logging.info("Connecté avec succès au broker MQTT")
        else:
            logging.error(f"Échec de la connexion avec le code de retour {rc}")

    def on_message(self, client, userdata, msg):
        """Callback appelé lors de la réception d'un message"""
        logging.info(f"Message reçu sur {msg.topic}: {msg.payload.decode()}")

    def disconnect(self):
        """Se déconnecte proprement du broker MQTT"""
        try:
            self.client.disconnect()
            logging.info("Déconnexion réussie du broker MQTT")
        except Exception as e:
            logging.error(f"Erreur lors de la déconnexion : {e}")


def connect_to_broker(param):
    return None