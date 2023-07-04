from hmi import HMI
from HomeAutomation import HomeAutomation
from AnsweringQuestions import AnsweringQuestions
from NaturalLanguageProcessing import NaturalLanguageProcessing
from OnlineServices import OnlineServices
from SpeechRecognition import SpeechRecognition

class Destis:
    def __init__(self):
        self.hmi = HMI()
        self.home_automation = HomeAutomation()
        self.answering_questions = AnsweringQuestions()
        self.nlp = NaturalLanguageProcessing()
        self.online_services = OnlineServices()
        self.speech_recognition = SpeechRecognition()

    def run(self):
        self.hmi.display_welcome_message()

        while True:
            user_input = self.hmi.get_user_input()

            if user_input == 'exit':
                self.hmi.display_goodbye_message()
                break

            command = self.nlp.process_input(user_input)

            if command == 'home_automation':
                self.home_automation.execute_command()

            elif command == 'answering_questions':
                self.answering_questions.answer_questions()

            elif command == 'online_services':
                self.online_services.access_services()

            elif command == 'speech_recognition':
                self.speech_recognition.start_recognition()

            else:
                self.hmi.display_unknown_command()

if __name__ == '__main__':
    destis = Destis()
    destis.run()
