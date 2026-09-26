# 📘 Manual do Usuário - MIA (Assistente de Análise de Dados)

Bem-vindo ao manual de utilização da **MIA**! Este documento destina-se aos usuários finais (Líderes e Gerentes de Produção) e explica como interagir com a nossa assistente inteligente integrada diretamente no Telegram através do módulo `telegram_bot.py`.

## 1. O que é a MIA?
A MIA é uma Assistente de Inteligência Artificial desenhada para processar dados de supermercados (vendas, descartes e regras de produção) e devolver *insights* valiosos de forma rápida. Seu grande diferencial é a **ausência de comandos complexos**: toda a interação é feita através de linguagem natural.

## 2. Primeiros Passos
1. **Acesso:** Abra o aplicativo do Telegram no seu celular ou computador.
2. **Início:** Pesquise pelo *username* do nosso bot (fornecido pela equipe técnica) e clique no botão **"Iniciar"**.
3. **Apresentação:** Ao iniciar, o Telegram envia um comando oculto (`/start`) e a MIA vai se apresentar prontamente no chat, ficando imediatamente pronta para receber suas perguntas.

## 3. Como Interagir (Linguagem Natural)
Esqueça os menus numéricos e as barras de comandos. Trate a MIA como uma colega de trabalho! O motor de IA local foi treinado para compreender seu texto e extrair o contexto necessário.

**Exemplos de perguntas que você pode fazer:**
* *"MIA, quais produtos precisam ser produzidos hoje para evitar desperdícios?"*
* *"Quantas unidades devemos fazer do produto X com base no histórico do último mês?"*
* *"Qual foi a produtividade do setor de padaria na segunda-feira passada?"*
* *"O que deveria ter sido produzido ontem em comparação com a meta estabelecida?"*

## 4. Origem das Informações e Confiança
Para garantir que as recomendações de produção são exatas, a MIA trabalha de forma autônoma, lendo e cruzando arquivos de dados internos que ficam na pasta `backend/dados/`.
Quando você faz uma pergunta, ela analisa instantaneamente:
* **Catálogo e Ingredientes:** Arquivos como `produtos_mercado.csv` e `ingredientes_produtos.csv`.
* **Histórico de Vendas:** Relatórios comerciais como `vendas_supermercado_agosto_2026.csv` e `vendas_supermercado_setembro_2026.csv`.
* **Perdas e Descartes:** O arquivo de controle `descarte_supermercado_setembro_2026.csv`.
* **Regras Sazonais:** Arquivos de regras de negócio (`regras_agosto_2026.csv` e `regras_setembro_2026.csv`).

## 5. Dicas de Utilização e Solução de Problemas

* **Seja Específico no Contexto:** Se quiser dados de um dia específico, mencione isso na frase (ex: *"Mostre-me o que foi produzido em 24/09/2026"*). A IA conseguirá filtrar a resposta com muito mais precisão.
* **MIA não compreendeu:** Se a assistente não encontrar a resposta, tente reformular a pergunta, garantindo que o nome do produto ou setor está escrito de forma semelhante ao registrado no sistema.
* **Sem Resposta (Bot Offline):** Se você enviar uma mensagem e a MIA não responder depois de alguns segundos, significa que o serviço central (`main.py`) ou a infraestrutura do motor de IA não estão em execução no servidor local. Neste caso, contate o administrador do sistema para que o ambiente seja ativado.