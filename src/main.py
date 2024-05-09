from config import init_gemini
from ui import menu_options
from models import chat_model

def main():
    options = menu_options()

    match options:
        case "1":
            chat_model()

if __name__ == '__main__':
    main()