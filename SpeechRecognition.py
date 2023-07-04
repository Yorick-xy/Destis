import speech_recognition as sr
import pyttsx3

class SpeechRecognition:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.speaker = pyttsx3.init()

    def recognize_speech(self):
        with sr.Microphone() as source:
            print("Dites quelque chose...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

            try:
                text = self.recognizer.recognize_google(audio, language="fr-FR")
                return text
            except sr.UnknownValueError:
                print("Impossible de reconnaître la parole")
            except sr.RequestError as e:
                print("Erreur lors de la demande à l'API de reconnaissance vocale : {0}".format(e))

    def speak(self, text):
        self.speaker.setProperty('voice', 'fr')  # Sélectionne la voix française
        self.speaker.say(text)
        self.speaker.runAndWait()

# Utilisation de la classe SpeechRecognition
speech_recognizer = SpeechRecognition()
text = speech_recognizer.recognize_speech()
if text:
    print("Vous avez dit : " + text)
    speech_recognizer.speak("Vous avez dit : " + text)
