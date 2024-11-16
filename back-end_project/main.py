import spacy
import json
from IAnalyze import ia_query
import time
import google.generativeai as genai
from flask import Flask

# Carregar modelo do SpaCy para o português (se necessário)
nlp = spacy.load("pt_core_news_sm")

# Caminho do arquivo JSON
file_path = 'candy_comments.json'

# Função para processar os comentários e enviar para IA
def analyze_comments(data):
    data_string = json.dumps(data, ensure_ascii=False, indent=4)
    analysis_result = ia_query(data_string)
    return analysis_result

# Função para carregar o arquivo JSON
def load_json(file_path):
    with open(file_path, 'r', encoding="utf-8") as file:
        return json.load(file)

# Função para salvar o JSON atualizado
def save_json(file_path, data):
    with open(file_path, 'w', encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def main():
    # Carregar e processar o arquivo JSON
    data = load_json(file_path)

    # Analisar os comentários e atualizar o campo 'analyzed'
    updated_data = analyze_comments(data)

    print(updated_data)

main()



