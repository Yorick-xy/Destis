from ai import chatbot
import os

def main():
    # Construction dynamique du chemin vers le fichier config.yaml
    folder_path = os.path.join(os.environ["HOME"], "Documents/05_Dev/Destis/src/utils/config/config.yaml")
    print(f"Chemin du fichier config.yaml : {folder_path}")

    # Chargement fictif des données (ajuster en fonction des besoins)
    dataset_path = os.path.join("data", "dataset.csv")
    if os.path.exists(dataset_path):
        print(f"Chargement des données depuis {dataset_path}...")
    else:
        print(f"Attention : Le fichier {dataset_path} est introuvable.")

    # Message de bienvenue
    print("Initialisation de Destis OK:")

    # Initialisation du chatbot
    bot = chatbot.Chatbot()

    while True:
        try:
            # Lecture de l'entrée utilisateur
            user_input = input(">> ")
            if user_input.lower() == "quit":
                print("Au revoir ! Merci d'avoir utilisé Destis.")
                break

            # Génération de la réponse par le chatbot
            response = bot.respond(user_input)
            print(f"Bot: {response}")
        except KeyboardInterrupt:
            print("\nInterruption détectée. Au revoir !")
            break
        except Exception as e:
            print(f"Erreur : {e}")


if __name__ == "__main__":
    main()