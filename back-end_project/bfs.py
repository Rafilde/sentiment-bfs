import spacy
from collections import deque

# Carregar modelo do SpaCy para o português (se necessário)
nlp = spacy.load("pt_core_news_sm")

# Função para processar um comentário e criar o grafo de palavras
def build_graph(comments):
    graph = {}

    for comment in comments:
        # Tokenizar o comentário
        doc = nlp(comment)
        words = [token.text.lower() for token in doc if not token.is_stop and not token.is_punct]

        # Criar conexões entre as palavras
        for i in range(len(words)):
            if words[i] not in graph:
                graph[words[i]] = set()
            for j in range(i+1, len(words)):
                graph[words[i]].add(words[j])
                graph[words[j]].add(words[i])

    return graph

# Função para realizar o BFS e encontrar palavras relacionadas à palavra raiz
def bfs_algorithm(graph, start_word):
    if start_word not in graph:
        print(f"Palavra raiz '{start_word}' não encontrada no grafo.")
        return []

    visited = set()
    queue = deque([start_word])
    visited.add(start_word)
    related_words = []

    while queue:
        word = queue.popleft()
        related_words.append(word)

        for neighbor in graph[word]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return related_words

def bfs_execution(data_json):
    # Construir o grafo de palavras
    graph = build_graph(data_json)

    # Palavra raiz para buscar suas palavras relacionadas
    root_word = "sabor"

    # Realizar o BFS a partir da palavra raiz
    related_words = bfs_algorithm(graph, root_word)

    # Exibir as palavras relacionadas
    print(f"Palavras relacionadas à '{root_word}':", related_words)
