import spacy
from collections import deque

# Carregar modelo do SpaCy para o português (se necessário)
nlp = spacy.load("pt_core_news_sm")

def build_graph(comments):
    graph = {}

    for comment in comments:
        doc = nlp(comment)
        words = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct and not token.is_space]

        for i in range(len(words) - 1):  # Conectar palavras sequenciais
            word1 = words[i]
            word2 = words[i + 1]

            if word1 not in graph:
                graph[word1] = set()
            if word2 not in graph:
                graph[word2] = set()


            graph[word1].add(word2)
            graph[word2].add(word1)

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

def execution_graph(data_json):

    negative_comments = []
    positive_comments = []
    neutral_comments = []

    # Classificar comentários
    for comment in data_json:
        analyse = comment.get('analyzed', '')
        if analyse == 'Negativo':
            negative_comments.append(comment.get('comment', ''))
            print(comment.get('comment', ''))
        elif analyse == 'Positivo':
            positive_comments.append(comment.get('comment', ''))
            print(comment.get('comment', ''))
        elif analyse == 'Neutro':
            neutral_comments.append(comment.get('comment', ''))
            print(comment.get('comment', ''))

    # Criar grafos para cada categoria
    negative_graph = build_graph(negative_comments)
    positive_graph = build_graph(positive_comments)
    neutral_graph = build_graph(neutral_comments)

    # Retornar como JSON
    result = {
        'negative_graph': negative_graph,
        'positive_graph': positive_graph,
        'neutral_graph': neutral_graph,
    }

    return result