import requests
class OnlineServices:
    def __init__(self):
        self.search_engine = "https://www.google.com/webhp?hl=fr&sa=X&ved=0ahUKEwjxj8bD7fP_AhXqRaQEHSJDDGQQPAgI"

    def search_info(self, query):
        search_url = self.search_engine + query
        print(f"Cherche l'information: {query}")
        print(f"URL: {search_url}")

        response = requests.get(search_url)

        if response.status_code == 200:
            # Logique pour extraire les résultats de la réponse
            results = response.json()  # Supposons que la réponse est au format JSON

            # Affichage des résultats de la recherche
            print("Résultats de recherche:")
            for result in results:
                print(result)
        else:
            print("Une erreur s'est produite.")
