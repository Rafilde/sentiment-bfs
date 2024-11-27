# back-end_project/app/json_utils.py
import json

def load_json(file_path):
    """
    Carrega dados de um arquivo JSON e retorna o conteúdo como um dicionário.
    """
    with open(file_path, 'r', encoding="utf-8") as file:
        return json.load(file)

def write_json(file_path, data):
    """
    Salva um dicionário em um arquivo JSON no caminho especificado.
    """
    with open(file_path, 'w', encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def transform_json(data):
    """
    Transforma o dicionário de entrada para um formato onde cada cidade é uma chave
    e possui uma lista de cidades ligadas com a distância. A relação é bidirecional.
    Retorna um dicionário com a estrutura desejada.
    """
    transformed_data = {}

    for city_one, city_two, distance in zip(data['cityOne'], data['cityTwo'], data['distance']):
        if city_one not in transformed_data:
            transformed_data[city_one] = []

        transformed_data[city_one].append({
            "nome": city_two,
            "distancia": distance
        })

        if city_two not in transformed_data:
            transformed_data[city_two] = []

        transformed_data[city_two].append({
            "nome": city_one,
            "distancia": distance
        })

        write_json('uploads/tratamento.json', transformed_data)

    return transformed_data
