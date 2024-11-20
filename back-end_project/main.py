import json
import google.generativeai as genai
from flask import Flask, jsonify
from json_utils import load_json, write_json
from text_analysis import sentiment_analysis_feedback, analyze_comments, analysis_of_the_most_common_words
from bfs import execution_graph

# Caminho do arquivo JSON
file_path = 'candy_comments.json'
comments_file_path = 'comments.json'

app = Flask(__name__)

def process_data():
    # Carregar e processar o arquivo JSON
    data = load_json(file_path)

    # Analisar os comentários e atualizar o campo 'analyzed' e transformar em uma lista de objetos
    updated_data = analyze_comments(data)
    updated_data_json = json.loads(updated_data)

    word_graph = execution_graph(updated_data_json)
    # Salvar o grafo de comentários em outro arquivo JSON
    write_json(comments_file_path, word_graph)

    # Função para ver qual ou quais são os sentimentos que mais apareceram
    sentiment = sentiment_analysis_feedback(updated_data_json)

    common_words = analysis_of_the_most_common_words(updated_data_json)

    result = {
        'comments': updated_data_json,
        'most_common_sentiments': sentiment,
        'most_common_words': common_words,
    }

    return result

@app.route('/comments', methods=['GET'])
def get_comments():
    with open(comments_file_path, 'r') as comments_file:
        comments = json.load(comments_file)
    return jsonify(comments)

@app.route('/feedback', methods=['GET'])
def get_feedback():
    result = process_data()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)



