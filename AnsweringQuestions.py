import requests
from bs4 import BeautifulSoup

class AnsweringQuestions:
    def answer_questions(self):
        while True:
            question = input("Posez une question (ou entrez 'exit' pour revenir) : ")

            if question == "exit":
                break

            answer = self.search_answer(question)
            if answer:
                print(f"Réponse : {answer}")
            else:
                print("Désolé, je ne connais pas la réponse à cette question.")

    def search_answer(self, question):
        search_url = "https://www.google.com/search?q=" + question
        response = requests.get(search_url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            answer = self.extract_answer(soup)
            return answer

        return None

    def extract_answer(self, soup):
        answer = None
        # Exemple simplifié : Recherchez l'élément <div class="answer"> qui contient la réponse
        answer_div = soup.find('div', class_='answer')

        if answer_div:
            answer = answer_div.text
        return answer

