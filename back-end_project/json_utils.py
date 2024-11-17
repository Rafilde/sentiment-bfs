import json

# Função para carregar o arquivo JSON
def load_json(file_path):
    with open(file_path, 'r', encoding="utf-8") as file:
        return json.load(file)
