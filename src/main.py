from config import init_gemini
from termcolor import colored
from ui import menu_options

model = init_gemini()

chat = model.start_chat(history=[])

option = menu_options()

while True:
    user_input = input(colored("Pergunta: ","blue"))
    if user_input == "exit" or "sair":
        break
    print("\nSua Pergunta:", user_input)
    print(colored("\nBot: Processando...","green"))
    response = chat.send_message(user_input)
    print("\nBot:", response.text)


print(colored("\nSessão encerrada!","red"))