#Aqui a gente cria o grafo das cidades
def build_city_graph(data):
    graph = {}

    city_one_list = data["cityOne"]
    city_two_list = data["cityTwo"]
    distances = data["distance"]

    for i in range(len(city_one_list)):
        city_one = city_one_list[i]
        city_two = city_two_list[i]
        distance = distances[i]

        if city_one not in graph:
            graph[city_one] = []

        connection_exists = False
        for connection in graph[city_one]:
            if connection["nome"] == city_two:
                connection_exists = True
                break

        if not connection_exists:
            graph[city_one].append({"nome": city_two, "distancia": distance})

        if city_two not in graph:
            graph[city_two] = []

        connection_exists = False
        for connection in graph[city_two]:
            if connection["nome"] == city_one:
                connection_exists = True
                break

        if not connection_exists:
            graph[city_two].append({"nome": city_one, "distancia": distance})

    return graph
