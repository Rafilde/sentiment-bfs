import spacy
import json
import os
from dotenv import load_dotenv
import google.generativeai as genai
from flask import Flask

#Função que pega o valor das minhas variáveis de ambiente
load_dotenv()
# Carregar modelo do SpaCy para o português (se necessário)
nlp = spacy.load("pt_core_news_sm")

# Caminho do arquivo JSON
file_path = 'event_feedback.json'

#Configuração e chamado da api do Google IA Studio
genai.configure(api_key=os.environ["GOOGLE_IA_STUIDO"])
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content(
    "Tell me a story about a magic backpack.",
    generation_config=genai.types.GenerationConfig(
        # Only one candidate for now.
        temperature=0.0,
    ),
)

# Função de análise de sentimentos
# def sentiment_analyzer_transformers(text):


# Abrir e ler o arquivo JSON
with open(file_path, 'r', encoding="utf-8") as file:
    data = json.load(file)