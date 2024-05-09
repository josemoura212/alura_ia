from termcolor import colored
from google.generativeai import ChatSession

special_input = ["sair","arquivo","audio"]

def chat_model(chat_model:ChatSession):
    while True:
        user_input = input(colored("Pergunta: ","blue"))
        if user_input.lower() == "sair":
            print(colored("\nBot: Até mais!","red"))
            break
        print("\nSua Pergunta:",user_input)
        print(colored("\nBot: Processando...","green"))
        response = chat_model.send_message(user_input)
        print("\nBot:", response.text + "\n")