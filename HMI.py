class HMI:
    def __init__(self):
        pass

    def display_welcome_message(self):
        print("Welcome to Destis!")

    def display_goodbye_message(self):
        print("Goodbye!")

    def get_user_input(self):
        return input("Please enter a command: ")

    def display_unknown_command(self):
        print("Unknown command!")
