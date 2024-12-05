import heapq

def dijkstra(graph, source, target, weight='weight'):
    """
    Implementação do algoritmo de Dijkstra para encontrar o menor caminho.

    - graph (networkx.Graph): O grafo.
    - source (str): O nó de origem.
    - target (str): O nó de destino.
    - weight (str): O atributo de peso nas arestas.

    retorna:
    - path (list): Lista com o menor caminho do nó de origem para o nó de destino.
    """
    # Inicialização
    queue = []
    heapq.heappush(queue, (0, source))  # (distância acumulada, nó atual)
    distances = {node: float('inf') for node in graph.nodes()}
    distances[source] = 0
    predecessors = {node: None for node in graph.nodes()}

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_node == target:  # Chegamos ao destino
            break

        for neighbor in graph.neighbors(current_node):
            edge_weight = graph[current_node][neighbor].get(weight, 1)
            distance = current_distance + edge_weight

            if distance < distances[neighbor]:  # Encontramos um caminho melhor
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    # Reconstrução do caminho
    path = []
    node = target
    while node is not None:
        path.insert(0, node)
        node = predecessors[node]

    if path[0] != source:
        return []

    return path
