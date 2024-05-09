from termcolor import colored


def chat(chat):
    while True:
        user_input = input(colored("Pergunta: ","blue"))
        if user_input == "exit" or "sair":
            break
        print("\nSua Pergunta:", user_input)
        print(colored("\nBot: Processando...","green"))
        response = chat.send_message(user_input)
        print("\nBot:", response.text)