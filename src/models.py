import os
from termcolor import colored
from pydub.utils import make_chunks

from config import init_gemini
from pydub import AudioSegment
import speech_recognition as sr

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
AUDIO_PATH = BASE_PATH + "\\arquivos\\audio.ogg"
def chat_model():
    special_input = ["sair","limpar","comandos","ajuda","audio"]

    model = init_gemini()

    chat = model.start_chat(history=[])
    while True:
        user_input = input(colored("Prompt ou comando: ","blue"))
        if user_input in special_input:
            if user_input.lower() == "sair":
                print(colored("\nBot: Até mais!","red"))
                break
            elif user_input.lower() == "audio":
                audio = AudioSegment.from_file(AUDIO_PATH, "ogg")

                size = 240000 # o milisegundo para cortar o audio no maximo 3 min

                chunks = make_chunks(audio, size) # Corte o arquivo em pedaços

                for i, chunk in enumerate(chunks):
                   # Enumeration, i is the index, chunk is the cut file
                   # convert mp3 file to wav
                   chunk_name = "audio{0}.wav".format(i)
                   # save document
                   chunk.export(chunk_name, format="wav")
                   file_audio = sr.AudioFile("./" + chunk_name)

                   # use the audio file as the audio source
                   r = sr.Recognizer()
                   with file_audio as source:
                      audio_text = r.record(source)
                      text = r.recognize_google(audio_text,language='pt-BR')

                   arq = open(chunk_name.replace('.wav', '') + '.txt','w')
                   arq.write(text)
                   arq.close()
                   input_text = input(colored("Prompt para ir junto ao audio: ","blue"))
                   print(colored("\nBot: Processando...","green"))
                   input_text = text + " " + input_text
                   response = chat.send_message(input_text)
                   print("\nBot:", response.text + "\n")
                continue
            elif user_input.lower() == "limpar":
                chat_model()
                break
            elif user_input.lower() == "comandos":
                for command in special_input:
                    print(colored(command,"green"))
            elif user_input.lower() == "ajuda":
                print(colored("\nBot: Digite 'sair' para encerrar a conversa.","green"))
                print(colored("Bot: Digite 'limpar' para limpar o historico.","green"))
                print(colored("Bot: Digite 'comandos' para ver os comandos disponíveis.","green"))
        print("\nSua Pergunta:",user_input)
        print(colored("\nBot: Processando...","green"))
        response = chat.send_message(user_input)
        print("\nBot:", response.text + "\n")