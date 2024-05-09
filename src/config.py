import google.generativeai as genai
import os

from termcolor import colored

from ui import clean_screen

def init_gemini():
    genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

    print("Modelos disponíveis para geração de conteúdo:")
    list_models = []
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            model = m.name.split("/")[1]
            list_models.append(model)
            print(model)
    print(colored("\nSelecione um modelo para geração de conteúdo:", "green"))
    print(colored("Ou aperte enter para selecionar o modelo padrão (gemini-pro)", "red"))

    selected_model = input()

    if selected_model in list_models or selected_model == "":

        if selected_model == "":
            selected_model = "gemini-pro"
        print("Modelo inválido")
        clean_screen()

        generation_config = {
          "candidate_count": 1,  
          "temperature": 0.8,
          "top_p": 0.95,
          "max_output_tokens": 8192,
        }

        safety_settings = {
            "HARASSMENT" : "BLOCK_NONE",
            "HATE": "BLOCK_NONE",
            "SEXUAL": "BLOCK_NONE",
            "DANGEROUS" : "BLOCK_NONE",
        }

        model = genai.GenerativeModel(model_name=selected_model,
                                      generation_config=generation_config,
                                      safety_settings=safety_settings)

        return model
    else:
        print("Modelo inválido")
        clean_screen()
        return init_gemini()


    



