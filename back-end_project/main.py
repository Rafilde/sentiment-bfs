import json
import google.generativeai as genai
from flask import Flask, jsonify
from json_utils import load_json, write_json
from text_analysis import sentiment_analysis_feedback, analyze_comments, analysis_of_the_most_common_words
from read_xlsx import read_xlsx_and_create_dictionary

# Caminho do arquivo JSON
file_path = '../destinos.xlsx'
json_of_destination = 'destination_data.json'

app = Flask(__name__)

def process_data():
    destination_dictionary = read_xlsx_and_create_dictionary(file_path)
    write_json(json_of_destination, destination_dictionary)

@app.route('/json_data', methods=['GET'])
def get_feedback():
    process_data()
    return load_json(json_of_destination)

if __name__ == '__main__':
    app.run(debug=True)



