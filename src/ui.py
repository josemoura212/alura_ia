import os
import textwrap
from IPython.display import display,Markdown

def to_markdown(text):
    text = text.replace("º", "*")
    return Markdown(textwrap.indent(text,">",predicate=lambda _:True))

def print_history(message,chat):
    for message in chat.history:
        display(to_markdown(f"**{message.role}** : {message.parts[0].text}"))
        print("--------------------------------------------")

def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_options():
    print("1 - Iniciar conversa")
    print("2 - Transcrever audio")
    print("3 - Traduzir arquivos")
    print("4 - Sair")
    print("Selecione uma opção:")
    selected_option = input()
    clean_screen()
    return selected_option