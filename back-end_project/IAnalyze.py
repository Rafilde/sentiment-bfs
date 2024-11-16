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

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
  system_instruction="Analise o sentimento do seguinte comentário com base no conteúdo e contexto apresentados. Determine se o sentimento geral é positivo, neutro, ou negativo.\n    Considere os seguintes critérios:\n\n    Positivo: O comentário demonstra emoções positivas, como alegria, satisfação ou aprovação.\n    Neutro: O comentário é informativo ou objetivo, sem expressar sentimentos claros ou emocionais.\n    Negativo: O comentário transmite insatisfação, crítica, tristeza ou outras emoções negativas.\n    Retorne apenas uma palavra indicando o sentimento detectado: Positivo, Neutro ou Negativo.",
)

chat_session = model.start_chat(
  history=[
  ]
)

def consulta_IA(text):
  response = chat_session.send_message(text)
  return response.text
