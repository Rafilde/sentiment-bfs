# back-end_project/main.py
from app.read_xlsx import read_xlsx
from app.json_utils import transform_json
from app.graph_utils import create_graph, draw_graph_interactive

def main():
    # 1. Ler o arquivo Excel e gerar arquivo para controle
    file_path = 'destinos.xlsx'
    xlsx_data = read_xlsx(file_path)

    # 2. Transformar os dados do dicionário inicial para um formato relacional
    transformed_data = transform_json(xlsx_data)

    # 3. Criar e exibir o grafo com os dados transformados
    graph = create_graph(transformed_data)
    draw_graph_interactive(graph)

if __name__ == "__main__":
    main()
