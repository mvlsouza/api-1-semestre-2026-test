import os; import sys
from urllib.request import urlopen; from urllib.error import URLError
import urllib3.util.connection as urllib3_cn
from dotenv import load_dotenv; from paths import ENV_PATH 
from bot.telegram_bot import iniciar_bot; from ia.config import IA_APRIMORADA, iniciar_configuracoes_ia

# Desabilita o uso de IPv6 para evitar problemas de conexão (acelera o tempo de resposta do bot)
urllib3_cn.HAS_IPV6 = False

load_dotenv(dotenv_path=ENV_PATH)
TELEGRAM_BOT_KEY = os.getenv("TELEGRAM_BOT_KEY")
if not TELEGRAM_BOT_KEY: 
    raise ValueError("A chave do Telegram (TELEGRAM_BOT_KEY) não foi encontrada no arquivo .env!")

def verificar_ia_online():
    url = "http://localhost:11434/api/tags"
    print("[IA] Conectando à IA...")
    
    try:
        urlopen(url, timeout=3)
        print("[IA] IA conectada.")
    except URLError:
        print("[ERRO] Não foi possível conectar à IA. Abra o Ollama e inicie o bot novamente.")
        sys.exit(1)

def aquecer_modelo_na_gpu():
    print("[IA] Carregando o modelo (pode levar alguns segundos)...")
    try:
        IA_APRIMORADA("Responda apenas 'ok'.")
        print("[IA] Modelo carregado e pronto para responder.")
    except Exception:
        print("[AVISO] Não foi possível carregar o modelo agora. A primeira resposta pode demorar; confira se ele está baixado.")

if __name__ == "__main__":
    verificar_ia_online()
    iniciar_configuracoes_ia()
    aquecer_modelo_na_gpu()
    iniciar_bot(TELEGRAM_BOT_KEY)