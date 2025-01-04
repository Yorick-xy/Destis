from ai import chatbot

def main():
    print("Chemin du fichier config.yaml : /Users/yorick/Documents/05_Dev/Destis/src/utils/config/config.yaml")
    print("Chargement des données depuis data/dataset.csv...")
    print("Bienvenue dans Destis. Entrez une commande :")
    bot = chatbot.Chatbot()
    while True:
        user_input = input(">> ")
        response = bot.respond(user_input)
        print(response)

if __name__ == "__main__":
    main()