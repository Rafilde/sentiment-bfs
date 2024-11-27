import heapq

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

def dijkstra(graph, start, end):
    distances = {city: float('inf') for city in graph}
    previous_cities = {city: None for city in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_distance, current_city = heapq.heappop(pq)

        if current_city == end:
            break

        if current_distance > distances[current_city]:
            continue

        for neighbor in graph[current_city]:
            neighbor_city = neighbor["nome"]
            weight = neighbor["distancia"]
            distance = current_distance + weight

            if distance < distances[neighbor_city]:
                distances[neighbor_city] = distance
                previous_cities[neighbor_city] = current_city
                heapq.heappush(pq, (distance, neighbor_city))

    path = []
    current_city = end
    while current_city is not None:
        path.insert(0, current_city)
        current_city = previous_cities[current_city]

    return {
        "caminho": path,
        "distancia_total": distances[end]
    }