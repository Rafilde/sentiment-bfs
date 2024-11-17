import json
import google.generativeai as genai
from flask import Flask
from json_utils import load_json
from text_analysis import sentiment_analysis_feedback, analyze_comments, analysis_of_the_most_common_words
from bfs import bfs_execution

# Caminho do arquivo JSON
file_path = 'event_feedback.json'

def main():
    # Carregar e processar o arquivo JSON
    data = load_json(file_path)

    # Analisar os comentários e atualizar o campo 'analyzed' e transformar em uma lista de objetos
    updated_data = analyze_comments(data)
    updated_data_json = json.loads(updated_data)

    # Função para ver qual ou quais são os sentimentos que mais apareceram
    sentiment = sentiment_analysis_feedback(updated_data_json)

    common_words = analysis_of_the_most_common_words(updated_data_json)

    result = {
        'comments': updated_data_json,
        'most_common_sentiments': sentiment,
        'most_common_words': common_words,
    }

    return json.dumps(result, ensure_ascii=False, indent=4)

print(main())



