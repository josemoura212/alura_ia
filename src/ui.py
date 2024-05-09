import os

def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_options():
    print("1 - Iniciar conversa")
    print("2 - Sair")
    print("Selecione uma opção:")
    selected_option = input()
    clean_screen()
    return selected_option