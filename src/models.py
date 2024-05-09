from termcolor import colored
from google.generativeai import ChatSession

from config import init_gemini



def chat_model():
    special_input = ["sair","limpar"]

    model = init_gemini()

    chat = model.start_chat(history=[])
    while True:
        user_input = input(colored("Pergunta: ","blue"))
        if user_input in special_input:
            if user_input.lower() == "sair":
                print(colored("\nBot: Até mais!","red"))
                break
            elif user_input.lower() == "limpar":
                chat_model()
                break
        print("\nSua Pergunta:",user_input)
        print(colored("\nBot: Processando...","green"))
        response = chat.send_message(user_input)
        print("\nBot:", response.text + "\n")