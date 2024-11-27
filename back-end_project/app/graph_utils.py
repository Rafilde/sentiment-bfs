import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np
from matplotlib.animation import FuncAnimation

def create_graph(data):
    """
    Cria um grafo utilizando os dados fornecidos.

    Args:
    - data: Dicionário onde cada chave é uma cidade e os valores são listas de conexões.

    Returns:
    - G (networkx.Graph): Grafo criado.
    """
    G = nx.Graph()

    for city, connections in data.items():
        for conn in connections:
            G.add_edge(city, conn["nome"], weight=conn["distancia"])
    
    return G

def draw_graph_interactive(G):
    """
    Desenha o grafo e cria uma animação interativa simulando duas viaturas da polícia
    movendo-se suavemente entre os nós (cidades), considerando o peso das arestas.

    Args:
    - G (networkx.Graph): Grafo a ser exibido.
    """
    pos = nx.spring_layout(G, seed=42)

    nodes = list(G.nodes())
    prision = 'Jail'

    linked_node = random.choice(nodes)
    G.add_edge(prision, linked_node, weight=50)
    pos[prision] = pos[linked_node] + np.array([0.1, 0.1])

    fig, ax = plt.subplots()
    nx.draw(G, pos, with_labels=True, ax=ax, node_size=700, font_size=10)

    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)
    nx.draw_networkx_nodes(G, pos, nodelist=[prision], node_color='#F2F2F2', node_size=800, ax=ax)

    police_positions = [random.choice([node for node in nodes if node != prision]) for _ in range(2)]
    police_states = ['random', 'random']
    pending_crime_paths = [None, None]
    pending_crime_targets = [None, None] 
    
    police_scatters = [
        ax.scatter([], [], s=200, color='gray') for _ in range(2)
    ]

    directions = [None, None]
    current_steps = [0, 0]
    num_steps_list = [0, 0]
    current_paths = [[], []]

    def move_police(i, path):
        """
        Define a rota que a viatura deve seguir.

        Args:
        - i (int): Índice da viatura.
        - path (list): Caminho a ser seguido pela viatura.
        """
        current_paths[i] = path
        if len(path) > 1:
            num_steps_list[i] = max(int(G[path[0]][path[1]]['weight'] / 10), 10)
            directions[i] = np.linspace(pos[path[0]], pos[path[1]], num_steps_list[i])
            current_steps[i] = 0
        else:
            directions[i] = None

    def start_random_movement(i):
        """
        Inicia o movimento aleatório de uma viatura.

        Args:
        - i (int): Índice da viatura.
        """
        if police_states[i] == 'random':
            neighbors = list(G.neighbors(police_positions[i]))
            neighbors = [n for n in neighbors if n != prision]
            if neighbors:
                random_target = random.choice(neighbors)
                path = [police_positions[i], random_target]
                move_police(i, path)

    def on_click(event):
        """
        Identifica qual vértice foi clicado e aciona a função perseguição de crime.

        Args:
        - event: Evento de clique do mouse.
        """
        for node, (x, y) in pos.items():
            if (event.xdata - x)**2 + (event.ydata - y)**2 < 0.01:
                if node != prision:
                    handle_crime(node)

    def handle_crime(node):
        """
        Envia a viatura mais próxima para responder a um crime.

        Args:
        - node: Nó da cidade onde ocorreu o crime.
        """
        distances = []
        for i in range(2):
            if police_states[i] == 'random':
                try:
                    path = nx.shortest_path(G, source=police_positions[i], target=node, weight='weight')
                    distances.append((len(path), i, path))
                except nx.NetworkXNoPath:
                    continue

        if distances:
            _, police_index, path_to_crime = min(distances, key=lambda x: x[0])
            if len(path_to_crime) > 1:
                police_states[police_index] = 'pending_to_crime'
                pending_crime_targets[police_index] = node

    def update(frame):
        """
        Atualiza a posição das viaturas no quadro da animação.

        Args:
        - frame: Índice do quadro atual da animação.
        """
        for i in range(len(police_positions)):
            new_position = None

            if directions[i] is not None and current_steps[i] < num_steps_list[i]:
                new_position = directions[i][current_steps[i]]
                current_steps[i] += 1

            elif directions[i] is not None and current_steps[i] >= num_steps_list[i]:
                if len(current_paths[i]) > 1:
                    police_positions[i] = current_paths[i][1]
                    current_paths[i] = current_paths[i][1:] 

                    if len(current_paths[i]) > 1:
                        move_police(i, current_paths[i])
                    else:
                        if police_states[i] == 'pending_to_crime':
                            next_target = pending_crime_targets[i]
                            path_to_crime = nx.shortest_path(G, source=police_positions[i], target=next_target, weight='weight')
                            police_states[i] = 'to_crime'
                            move_police(i, path_to_crime)
                            pending_crime_targets[i] = None

                        elif police_states[i] == 'to_crime':
                            path_to_prision = nx.shortest_path(G, source=police_positions[i], target=prision, weight='weight')
                            police_states[i] = 'to_prision'
                            move_police(i, path_to_prision)

                        elif police_states[i] == 'to_prision':
                            police_states[i] = 'random'
                            start_random_movement(i)

                else:
                    if police_states[i] == 'random':
                        start_random_movement(i)

            if new_position is not None:
                police_scatters[i].set_offsets([new_position])

            if police_states[i] in ['to_crime', 'to_prision', 'pending_to_crime']:
                police_scatters[i].set_color('red')
            else:
                police_scatters[i].set_color('gray')

        return police_scatters

    fig.canvas.mpl_connect('button_press_event', on_click)

    for i in range(2):
        start_random_movement(i)

    ani = FuncAnimation(fig, update, frames=200, interval=100, blit=True, repeat=True)

    plt.show()