# back-end_project/app/read_xlsx.py
import os
import pandas as pd
from .json_utils import write_json

def read_xlsx(file, upload_folder='uploads', saved_file_name='entrada.json'):
    file_path = os.path.join(upload_folder, saved_file_name)

    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

    try:
        df = pd.read_excel(file, engine='openpyxl')

        result = {
            'cityOne': df.iloc[:, 0].tolist(),
            'cityTwo': df.iloc[:, 1].tolist(),
            'distance': df.iloc[:, 2].tolist()
        }

        file_path = os.path.join(upload_folder, saved_file_name)
        write_json(file_path, result)

        return result

    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo não encontrado!")
    except ValueError as ve:
        raise ValueError(f"Erro no arquivo Excel: {ve}")
    except Exception as e:
        raise Exception(f"Ocorreu um erro ao ler ou salvar o arquivo Excel: {e}")