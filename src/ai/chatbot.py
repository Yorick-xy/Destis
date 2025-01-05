from transformers import AutoModelForCausalLM, AutoTokenizer
import torch


class Chatbot:
    def __init__(self, model_path="microsoft/DialoGPT-medium", temperature=0.9, top_p=0.8, max_length=200):
        """
        Initialise le chatbot avec les paramètres de génération de texte.
        """
        print("Chargement du modèle DialoGPT...")
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)

        # Configure le pad_token si absent
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token

        self.model = AutoModelForCausalLM.from_pretrained(model_path)
        self.chat_history_ids = None
        self.temperature = temperature
        self.top_p = top_p
        self.max_length = max_length
        self.conversation_turns = 0  # Compteur pour gérer les tours de conversation

    def respond(self, user_input):
        """
        Génère une réponse à partir de l'entrée utilisateur.
        """
        input_ids = self.tokenizer.encode(user_input + self.tokenizer.eos_token, return_tensors="pt")
        attention_mask = torch.ones(input_ids.shape, dtype=torch.long)  # Crée un masque explicite

        # Réinitialise l'historique après 10 tours de conversation
        self.conversation_turns += 1
        if self.conversation_turns > 10:
            print("Réinitialisation de l'historique de conversation.")
            self.chat_history_ids = None
            self.conversation_turns = 1

        # Combine l'historique avec le nouvel input
        if self.chat_history_ids is not None:
            max_history_tokens = 300  # Limite l'historique
            self.chat_history_ids = self.chat_history_ids[:, -max_history_tokens:]

            bot_input_ids = torch.cat([self.chat_history_ids, input_ids], dim=-1)
            attention_mask = torch.cat(
                [torch.ones(self.chat_history_ids.shape, dtype=torch.long), attention_mask], dim=-1
            )
        else:
            bot_input_ids = input_ids

        # Génération de réponse
        self.chat_history_ids = self.model.generate(
            bot_input_ids,
            max_length=self.max_length,
            pad_token_id=self.tokenizer.pad_token_id,
            temperature=self.temperature,
            do_sample=True,
            top_p=self.top_p,
            repetition_penalty=1.2,  # Appliquer une pénalité sur les répétitions
            num_beams=5,  # Recherche par faisceaux pour une génération plus cohérente
            no_repeat_ngram_size=2,  # Eviter les répétitions
            attention_mask=attention_mask,
            early_stopping = True
        )

        # Décodage de la réponse
        response = self.tokenizer.decode(self.chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
        return response


