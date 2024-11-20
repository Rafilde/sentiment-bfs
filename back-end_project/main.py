import json
import google.generativeai as genai
from flask import Flask, request, jsonify
from flask_cors import CORS
from json_utils import load_json, write_json
from text_analysis import sentiment_analysis_feedback, analyze_comments, analysis_of_the_most_common_words
from read_xlsx import read_xlsx_and_create_dictionary
import os

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads'
ALLOWED_EXTENSIONS = {'xlsx'}
CORS(app)

json_data_destination = 'destination_data.json'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'message': 'Nenhum arquivo enviado'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'message': 'Nenhum arquivo selecionado'}), 400
    if file and allowed_file(file.filename):

        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])

        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)

        destination_dictionary = read_xlsx_and_create_dictionary(filename)
        write_json(json_data_destination, destination_dictionary)

        return jsonify(destination_dictionary)

    return jsonify({'message': 'Tipo de arquivo inválido'}), 400

@app.route('/json_data', methods=['GET'])
def json_data():
    return load_json(json_data_destination)

if __name__ == '__main__':
    app.run(debug=True)



