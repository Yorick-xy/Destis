# ai/speech_synthesis.py

import pyttsx3

class SpeechSynthesis:
    """Classe pour la synthèse vocale du robot."""

    def __init__(self, language='fr'):
        """Initialise le moteur de synthèse vocale."""
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)  # Vitesse de la voix
        self.engine.setProperty('volume', 1)  # Volume maximal
        self.engine.setProperty('voice', language)  # Langue

    def speak(self, message):
        """Fait parler le robot."""
        print(f"Robot: {message}")
        self.engine.say(message)
        self.engine.runAndWait()
