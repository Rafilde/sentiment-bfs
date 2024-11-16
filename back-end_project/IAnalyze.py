import os
from dotenv import load_dotenv
import google.generativeai as genai

#Função que pega o valor das minhas variáveis de ambiente
load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
generation_config = {
  "candidate_count": 1,
  "temperature": 0.3,
  "top_p": 0.2,
  "top_k": 80,
}

safe_security = {
  "HARASSMENT": "BLOCK_NONE",  # Remover filtro sobre conteúdo de assédio
  "HATE": "BLOCK_NONE",         # Remover filtro sobre conteúdo de ódio
  "SEXUAL": "BLOCK_NONE",       # Remover filtro sobre conteúdo sexual
  "DANGEROUS": "BLOCK_NONE"     # Remover filtro sobre conteúdo perigoso
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
  safety_settings=safe_security,
  system_instruction="Você receberá um JSON contendo uma lista de comentários, cada um com um id, comment, e um campo analyzed (onde o valor será inicialmente 'null'). O objetivo é analisar o conteúdo de cada comentário e determinar o sentimento geral de cada um, com base nos seguintes critérios:\n\nPositivo: O comentário demonstra emoções positivas, como alegria, satisfação ou aprovação.\nNeutro: O comentário é informativo ou objetivo, sem expressar sentimentos claros ou emocionais.\nNegativo: O comentário transmite insatisfação, crítica, tristeza ou outras emoções negativas.\nVocê deve retornar um JSON com os mesmos id dos comentários e os mesmos comentários, mas com o campo analyzed preenchido com o valor do sentimento detectado: 'Positivo', 'Neutro' ou 'Negativo'. O JSON deve ser retornado como uma única string em uma única linha"
)

chat_session = model.start_chat(
  history=[]
)

def ia_query(text):
  response = chat_session.send_message(text)
  return response.text
