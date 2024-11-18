import spacy
from collections import deque

# Carregar modelo do SpaCy para o português (se necessário)
nlp = spacy.load("pt_core_news_sm")

# Função para processar um comentário e criar o grafo de palavras
def build_graph(comments):
    graph = {}

    for comment in comments:
        doc = nlp(comment)
        words = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct and not token.is_space]

        # Criar conexões entre as palavras
        for i in range(len(words)):
            if words[i] not in graph:
                graph[words[i]] = set()
            for j in range(i+1, len(words)):
                if words[j] not in graph:
                    graph[words[j]] = set()
                graph[words[i]].add(words[j])
                graph[words[j]].add(words[i])

    return graph

#def build_graph(comments):
    #graph = {}

    #for comment in comments:
        #doc = nlp(comment)
        #words = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct and not token.is_space]

        #for i in range(len(words) - 1):  # Conectar palavras sequenciais
            #word1 = words[i]
            #word2 = words[i + 1]

            #if word1 not in graph:
                #graph[word1] = set()
            #if word2 not in graph:
                #graph[word2] = set()


            #graph[word1].add(word2)
            #graph[word2].add(word1)

    #return graph

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

def bfs_execution():
    # Construir o grafo de palavras
    graph = build_graph([
        "Eu gosto de programar em Python e Java.",
        "Python é uma linguagem de programação poderosa.",
        "Java também é muito popular entre os desenvolvedores."
    ])

    print(graph)

    # Palavra raiz para buscar suas palavras relacionadas
    root_word = "python"

    # Realizar o BFS a partir da palavra raiz
    related_words = bfs_algorithm(graph, root_word)

    # Exibir as palavras relacionadas
    print(f"Palavras relacionadas à '{root_word}':", related_words)

bfs_execution()