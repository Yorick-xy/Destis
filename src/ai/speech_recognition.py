# src/ai/speech_recognition.py

import speech_recognition as sr

class SpeechRecognition:
    """Classe pour la reconnaissance vocale."""

    def __init__(self):
        """Initialise le moteur de reconnaissance vocale."""
        self.recognizer = sr.Recognizer()

    def listen(self):
        """Écoute la commande vocale de l'utilisateur."""
        with sr.Microphone() as source:
            print("Robot: Je vous écoute...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
            try:
                command = self.recognizer.recognize_google(audio, language='fr-FR')
                print(f"Utilisateur: {command}")
                return command
            except sr.UnknownValueError:
                print("Désolé, je n'ai pas compris.")
                return None
            except sr.RequestError:
                print("Erreur de connexion au service de reconnaissance vocale.")
                return None
