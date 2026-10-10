import asyncio
import edge_tts

vozes_pt_br = [
    "pt-BR-FranciscaNeural",
    "pt-BR-AntonioNeural",
    "pt-BR-ThalitaNeural"
]

texto_teste = "Olá! Eu sou a MIA, sua assistente inteligente. Como posso ajudar com a produção hoje?"

async def gerar_amostras():
    for voz in vozes_pt_br:
        nome_arquivo = f"amostra_{voz.split('-')[2]}.mp3"
        print(f"Gerando áudio com: {voz}...")
        
        comunicacao = edge_tts.Communicate(
            text=texto_teste, 
            voice=voz,
            rate="+10%",     # Ajuste de velocidade (ex: "+10%", "-5%")
            pitch="+7Hz"    # Ajuste de tom
        )
        await comunicacao.save(nome_arquivo)
        print(f"Salvo em: {nome_arquivo}")

if __name__ == "__main__":
    asyncio.run(gerar_amostras())