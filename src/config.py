import google.generativeai as genai
import os

from ui import clean_screen

def init_gemini():
    genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

    print("Modelos disponíveis para geração de conteúdo:")
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)

    print("Selecione um modelo para geração de conteúdo:")
    selected_model = input()

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
    
    model = genai.GenerativeModel(selected_model,
                                  generation_config=generation_config,
                                  safety_settings=safety_settings)
    
    clean_screen()
    return model



