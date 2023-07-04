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
                self.hmi.display_exit_message()
                break

            command = self.nlp.process_input(user_input)

            if command == 'home_automation':
                self.manage_home_automation()

            elif command == 'answering_questions':
                self.answering_questions.answer_questions()

            elif command == 'online_services':
                self.manage_online_services()

            elif command == 'speech_recognition':
                self.speech_recognition.start_recognition()

            else:
                self.hmi.display_unknown_command()

    def manage_home_automation(self):
        self.hmi.display_home_automation_options()

        while True:
            user_input = self.hmi.get_user_input()

            if user_input == 'stop':
                break

            if user_input == 'add_light':
                light_name = self.hmi.get_user_input("Enter the light name: ")
                self.home_automation.add_light(light_name)

            elif user_input == 'add_outlet':
                outlet_name = self.hmi.get_user_input("Enter the outlet name: ")
                self.home_automation.add_outlet(outlet_name)

            elif user_input == 'turn_on_light':
                light_name = self.hmi.get_user_input("Enter the light name: ")
                self.home_automation.turn_on_light(light_name)

            elif user_input == 'turn_off_light':
                light_name = self.hmi.get_user_input("Enter the light name: ")
                self.home_automation.turn_off_light(light_name)

            elif user_input == 'switch_on_outlet':
                outlet_name = self.hmi.get_user_input("Enter the outlet name: ")
                self.home_automation.switch_on_outlet(outlet_name)

            elif user_input == 'switch_off_outlet':
                outlet_name = self.hmi.get_user_input("Enter the outlet name: ")
                self.home_automation.switch_off_outlet(outlet_name)

            else:
                self.hmi.display_unknown_command()

    def manage_online_services(self):
        query = self.hmi.get_user_input("Enter your search query: ")
        self.online_services.search_info(query)

if __name__ == '__main__':
    destis = Destis()
    destis.run()
