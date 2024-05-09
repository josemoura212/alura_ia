# Imersão Alura/Google IA

## Projeto Python

## Configuração API_KEY
Para configurar a chave de API do Google, adicione a variável de ambiente GOOGLE_API_KEY com a chave de API.
Copiei o código abaixo e cole no terminal do PowerShell.

```$Env:GOOGLE_API_KEY="Sua chave de API"```

[Acesse o Google API Key](https://aistudio.google.com/app/apikey/?utm_content=)

## Preparação do ambiente
Configure o ambiente virtual com o comando abaixo.
```python -m venv venv```

Ative o ambiente virtual com o comando abaixo.
* Windows : ```venv\Scripts\Activate```
* Linux : ```source venv/bin/activate```

Instale as dependências do projeto com o comando abaixo.
```pip install -r requirements.txt```

## Iniciar o projeto
```python src/main.py```