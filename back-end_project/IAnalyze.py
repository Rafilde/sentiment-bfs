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
  system_instruction="""
  Você receberá um array de locais (podem ser cidades, estados, ou outros pontos de interesse). Para cada local do array, forneça uma descrição detalhada do que os visitantes podem fazer nesse local, incluindo atrações turísticas populares, atividades culturais, naturais e gastronômicas, eventos locais, e outros pontos de interesse que tornam esse lugar único.

  A descrição deve ser clara, envolvente e focada em informar o que há de interessante para um visitante em cada cidade ou região. Se necessário, use informações sobre a história e a cultura local para enriquecer a resposta.

  Responda com uma descrição para cada um desses locais.
  """
)

chat_session = model.start_chat(
  history=[]
)


def ia_query(locations_array):
  text = f"Os locais são: {', '.join(locations_array)}"

  response = chat_session.send_message(text)

  return response.text
