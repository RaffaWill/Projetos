from pathlib import Path
from openai import OpenAI


client = OpenAI(api_key='')


texto = "Meu nome é raffael e estou aplicando conhecimento em IA!"


caminho_arquivo_audio = Path("audio.mp3")

resposta = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input=texto
)

# Salve o áudio no arquivo especificado
resposta.stream_to_file(caminho_arquivo_audio)

print(f"Áudio salvo em: {caminho_arquivo_audio}")
