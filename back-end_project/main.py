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

# Função para ver qual ou quais são os sentimentos que mais apareceram
def sentiment_analysis_feedback(updated_data_json):
    sentiment_count = {'Positivo': 0, 'Neutro': 0, 'Negativo': 0}

    for data in updated_data_json:
        analyzed = data.get('analyzed')
        if analyzed in sentiment_count:
            sentiment_count[analyzed] += 1

    max_count = max(sentiment_count.values())
    most_common_sentiments = [sentiment for sentiment, count in sentiment_count.items() if count == max_count]
    return most_common_sentiments

def main():
    # Carregar e processar o arquivo JSON
    data = load_json(file_path)

    # Analisar os comentários e atualizar o campo 'analyzed' e transformar em uma lista de objetos
    updated_data = analyze_comments(data)
    updated_data_json = json.loads(updated_data)

    # Função para ver qual ou quais são os sentimentos que mais apareceram
    sentiment = sentiment_analysis_feedback(updated_data_json)

    result = {
        'comments': updated_data_json,
        'most_common_sentiments': sentiment,
    }

    return json.dumps(result, ensure_ascii=False, indent=4)

print(main())



