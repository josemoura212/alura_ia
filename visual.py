import textwrap
from IPython.display import display,Markdown

def to_markdown(text):
    text = text.replace("º", "*")
    return Markdown(textwrap.indent(text,">",predicate=lambda _:True))

def print_history(message,chat):
    for message in chat.history:
        display(to_markdown(f"**{message.role}** : {message.parts[0].text}"))
        print("--------------------------------------------")


