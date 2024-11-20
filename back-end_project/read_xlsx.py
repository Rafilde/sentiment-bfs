import pandas as pd

#Função para ler o arquivo xlsx e transformar em dicionário
def read_xlsx_and_create_dictionary(file):
    df = pd.read_excel(file, engine='openpyxl')

    result = {
        'cityOne': df.iloc[:, 0].tolist(),
        'cityTwo': df.iloc[:, 1].tolist(),
        'distance': df.iloc[:, 2].tolist()
    }

    return result
