import json
import spacy
from IAnalyze import ia_query
from collections import Counter

# Carregar o modelo da língua (ajuste para 'en_core_web_sm', 'pt_core_news_sm', etc.)
nlp = spacy.load('pt_core_news_sm')

# Função para processar os comentários e enviar para IA
def analyze_comments(data):
    data_string = json.dumps(data, ensure_ascii=False, indent=4)
    analysis_result = ia_query(data_string)
    return analysis_result

# Função para ver qual ou quais são os sentimentos que mais apareceram
def sentiment_analysis_feedback(updated_data_json):
    sentiment_count = {'Positivo': 0, 'Neutro': 0, 'Negativo': 0}

    for data in updated_data_json:
        analyzed = data.get('analyzed')
        if analyzed in sentiment_count:
            sentiment_count[analyzed] += 1

    max_count = max(sentiment_count.values())
    most_common_sentiments = [sentiment for sentiment, count in sentiment_count.items() if count == max_count]
    return most_common_sentiments

# Função responsável pela lematização das palavras
def lemmatization_of_comment(comment):
    doc = nlp(comment)

    filtered_tokens = [
        token.lemma_.lower() for token in doc
        if (not token.is_stop  # Remove stop words
           and not token.is_punct  # Remove pontuação
           and not token.is_space  # Remove espaços em branco
           and (token.is_alpha or token.is_digit))  # Mantém palavras ou números
    ]

    return " ".join(filtered_tokens)

# Nessa função vamos analisar as palavras mais comuns (o número de vezes que elas se repetem) de todos os comentários positivos, neutros ou negativos
def analysis_of_the_most_common_words(updated_data_json):

    most_common_words = {
        'Positivo': Counter(),
        'Neutro': Counter(),
        'Negativo': Counter(),
    }

    for data in updated_data_json:
        analyzed = data.get('analyzed')
        comment = data.get('comment', '')

        if analyzed in most_common_words:
            lemmatized_comment = lemmatization_of_comment(comment)

            words = lemmatized_comment.split()
            most_common_words[analyzed].update(words)

    result = {
        sentiment: {
            'words': [word for word, _ in counter.most_common()],
            'count': [count for _, count in counter.most_common()],
        }
        for sentiment, counter in most_common_words.items()
    }

    return result