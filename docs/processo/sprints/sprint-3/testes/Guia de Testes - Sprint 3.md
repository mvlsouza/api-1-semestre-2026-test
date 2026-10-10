# Guia de Testes — Sprint 3

Este documento é um **guia para você testar a MIA na prática**, e não um relatório do que já foi testado. A ideia é: você envia cada mensagem sugerida no Telegram, compara com o resultado esperado, anota o que realmente aconteceu e marca o status na tabela do final. Os resultados da execução serão registrados no Relatório de Testes da Sprint 3, criado ao final da execução.

## Pré-requisitos antes de começar

- [ ] Ollama aberto, com o modelo `ollama pull gemma4:e2b` baixado
- [ ] Arquivo `.env` configurado em `backend/src/.env` com `TELEGRAM_BOT_KEY` válido
- [ ] `python main.py` rodando sem erros no terminal (verifique se aparece "[IA] Modelo carregado e pronto para responder.")
- [ ] Bot respondendo a `/start` no Telegram
- [ ] Solução de transcrição de áudio instalada e funcionando localmente (definida no Planning da US09)
- [ ] CSVs de **matéria-prima** (consumo por produto e estoque por setor) disponíveis em `backend/dados/` (definição da Sprint 3)
- [ ] Registro de **transferências entre setores**, com motivo, disponível em `backend/dados/` (definição da Sprint 3)
- [ ] Celular com Telegram para gravar as mensagens de voz

---

## US09 — Perguntas por áudio (gestor)

| ID | Mensagem para enviar | Resultado esperado |
|---|---|---|
| 9.1 | Áudio dizendo: "O que devo produzir hoje?" | Transcreve e responde igual ao caso 1.1 da Sprint 1 (lista só com nomes) |
| 9.2 | Áudio dizendo: "Quantas unidades devo produzir amanhã na padaria?" | Resolve "amanhã" e o setor a partir da fala; resposta com nome e quantidade |
| 9.3 | Áudio dizendo: "Quanto de coxinha devo fazer amanhã?" em ambiente com ruído | Transcrição aceitável; se não entender, pede para repetir, sem inventar resposta |
| 9.4 | Áudio vazio ou só com silêncio | Mensagem amigável pedindo para enviar novamente, sem travar o bot |
| 9.5 | Áudio dizendo: "Qual é a capital da França?" | Agente Roteador identifica `INVALIDO`; mesma recusa padrão do texto |
| 9.6 | Áudio mais longo que o limite definido no Planning | Aviso claro sobre o limite, sem travar o bot |
| 9.7 | Enviar a mesma pergunta digitada e depois por áudio | As duas respostas têm o mesmo conteúdo |
| 9.8 | Enviar uma foto | Continua respondendo a mensagem fixa de formato não suportado (o caso 6.4 da Sprint 1 passa a valer só para formatos que não sejam texto nem áudio) |
| 9.9 | Após os testes, conferir a pasta de arquivos temporários da máquina | Não restaram arquivos de áudio temporários |

---

## US10 — Matéria-prima para o dia seguinte (líder)

*Os nomes das matérias-primas abaixo são exemplos: ajuste aos nomes reais da planilha.*

| ID | Mensagem para enviar | Resultado esperado |
|---|---|---|
| 10.1 | "Quanta matéria-prima preciso deixar preparada para amanhã na padaria?" | Lista de matérias-primas da Padaria, com quantidade e unidade, baseada na previsão de produção de amanhã |
| 10.2 | "O que preciso separar de ingredientes para amanhã na cozinha?" | Mesmo cálculo, fraseado diferente: verifica se o Agente Roteador entende variações de pergunta |
| 10.3 | "Quanto de farinha preciso para amanhã?" | Filtra uma matéria-prima e soma o consumo de todos os produtos que a usam |
| 10.4 | "Quanta matéria-prima preciso para amanhã?" (sem informar o setor) | Comportamento definido no Planning: todos os setores ou pedido do setor ao líder |
| 10.5 | "Quanta matéria-prima preciso para a padaira amanhã?" (erro de digitação proposital) | `normalizar_setor` deve corrigir para "Padaria" mesmo com o erro |
| 10.6 | Verificação cruzada: comparar com "Quantas unidades devo produzir amanhã na padaria?" | Quantidade de matéria-prima = quantidade prevista de cada produto × consumo por unidade |

---

## US11 — Matérias-primas disponíveis para transferir (líder)

*Os nomes das matérias-primas abaixo são exemplos: ajuste aos nomes reais da planilha.*

| ID | Mensagem para enviar | Resultado esperado |
|---|---|---|
| 11.1 | "Quais matérias-primas estão disponíveis para transferir para outros setores?" | Lista as matérias-primas com sobra, com quantidade e setor que as possui |
| 11.2 | "O que a padaria tem sobrando que outro setor pode usar?" | Filtra pelo setor de origem |
| 11.3 | "Tem farinha sobrando em algum setor?" | Responde só sobre a matéria-prima citada |
| 11.4 | Perguntar quando nenhum setor tem sobra | A MIA informa que não há sobras, sem inventar itens |
| 11.5 | Verificação cruzada: comparar com o caso 10.1 do mesmo setor | Nenhuma matéria-prima listada como disponível é necessária ao mesmo setor no dia seguinte |

---

## US12 — Motivo da transferência de um produto (gerente)

| ID | Mensagem para enviar | Resultado esperado |
|---|---|---|
| 12.1 | "Por que a coxinha está sendo transferida de setor?" | Motivo registrado, setor de origem, setor de destino e data |
| 12.2 | "Qual o motivo da transferência do pudim?" | Mesmo cálculo, fraseado diferente |
| 12.3 | "Por que o produto xyz foi transferido?" (produto inexistente) | Informa que não encontrou o produto, sem inventar motivo |
| 12.4 | "Por que o pão francês foi transferido de setor?" (produto sem transferência registrada) | Informa que não há transferência registrada, sem inventar motivo |
| 12.5 | "POR QUE A COXINHA FOI TRANSFERIDA?" (em maiúsculas) | Mesmo resultado do caso 12.1 (o bot converte o texto para minúsculas antes de enviar à IA) |

---

## Regressão — funcionalidades das Sprints 1 e 2

Garante que as novas funcionalidades não quebraram o que já funcionava.

| ID | Mensagem para enviar | Resultado esperado |
|---|---|---|
| 13.1 | "O que devo produzir hoje?" | Continua listando só os **nomes** dos produtos (caso 1.1 da Sprint 1) |
| 13.2 | "O que foi produzido ontem na padaria?" | Continua mostrando Total Produzido, Vendas e Descarte em unidades (caso 3.1 da Sprint 1) |
| 13.3 | "Quais produtos da padaria me dão mais lucro?" | Continua devolvendo o ranking de lucro da Padaria (caso 5.1 da Sprint 2) |
| 13.4 | "Quantos reais foram descartados ontem na empresa toda?" | Continua devolvendo o total em R$ (caso 7.1 da Sprint 2) |

---

## Roteamento e comportamento social (`agentes.py`)

| ID | Mensagem para enviar | Resultado esperado |
|---|---|---|
| 14.1 | "Oi" / "Bom dia" | Agente Roteador identifica `SAUDACAO`; resposta curta e simpática, sem acionar nenhuma tool |
| 14.2 | "Tchau" / "Obrigado!" | Mesma rota `SAUDACAO` |
| 14.3 | "Qual é a capital da França?" (fora do escopo) | Agente Roteador identifica `INVALIDO`; resposta de recusa padrão |
| 14.4 | "Quanto devo produzir amanhã?" | Responde em unidades de **produto**, sem confundir com matéria-prima (US10) |

---

## Formatação da resposta

| ID | O que verificar | Resultado esperado |
|---|---|---|
| 15.1 | Listas na resposta | Sempre usam `•`, nunca `*` |
| 15.2 | Início da resposta | Nunca começa repetindo saudação ("Olá! Aqui está...") |
| 15.3 | Quantidades de matéria-prima | Sempre acompanhadas da unidade de medida (kg, L, unidade) |
| 15.4 | Resposta a um áudio | Mesma formatação da resposta a um texto |

---

## Tabela de registro (preencha ao testar)

| Caso | Mensagem enviada | Resultado obtido | Status | Observações |
|---|---|---|---|---|
| 9.1 | Áudio dizendo: "O que devo produzir hoje?" |  |  |  |
| 9.2 | Áudio dizendo: "Quantas unidades devo produzir amanhã na padaria?" |  |  |  |
| 9.3 | Áudio dizendo: "Quanto de coxinha devo fazer amanhã?" em ambiente com ruído |  |  |  |
| 9.4 | Áudio vazio ou só com silêncio |  |  |  |
| 9.5 | Áudio dizendo: "Qual é a capital da França?" |  |  |  |
| 9.6 | Áudio mais longo que o limite definido no Planning |  |  |  |
| 9.7 | Enviar a mesma pergunta digitada e depois por áudio |  |  |  |
| 9.8 | Enviar uma foto |  |  |  |
| 9.9 | Após os testes, conferir a pasta de arquivos temporários da máquina |  |  |  |
| 10.1 | Quanta matéria-prima preciso deixar preparada para amanhã na padaria? |  |  |  |
| 10.2 | O que preciso separar de ingredientes para amanhã na cozinha? |  |  |  |
| 10.3 | Quanto de farinha preciso para amanhã? |  |  |  |
| 10.4 | Quanta matéria-prima preciso para amanhã? |  |  |  |
| 10.5 | Quanta matéria-prima preciso para a padaira amanhã? |  |  |  |
| 10.6 | Verificação cruzada: comparar com "Quantas unidades devo produzir amanhã na padaria?" |  |  |  |
| 11.1 | Quais matérias-primas estão disponíveis para transferir para outros setores? |  |  |  |
| 11.2 | O que a padaria tem sobrando que outro setor pode usar? |  |  |  |
| 11.3 | Tem farinha sobrando em algum setor? |  |  |  |
| 11.4 | Perguntar quando nenhum setor tem sobra |  |  |  |
| 11.5 | Verificação cruzada: comparar com o caso 10.1 do mesmo setor |  |  |  |
| 12.1 | Por que a coxinha está sendo transferida de setor? |  |  |  |
| 12.2 | Qual o motivo da transferência do pudim? |  |  |  |
| 12.3 | Por que o produto xyz foi transferido? |  |  |  |
| 12.4 | Por que o pão francês foi transferido de setor? |  |  |  |
| 12.5 | POR QUE A COXINHA FOI TRANSFERIDA? |  |  |  |
| 13.1 | O que devo produzir hoje? |  |  |  |
| 13.2 | O que foi produzido ontem na padaria? |  |  |  |
| 13.3 | Quais produtos da padaria me dão mais lucro? |  |  |  |
| 13.4 | Quantos reais foram descartados ontem na empresa toda? |  |  |  |
| 14.1 | Oi" / "Bom dia |  |  |  |
| 14.2 | Tchau" / "Obrigado! |  |  |  |
| 14.3 | Qual é a capital da França? |  |  |  |
| 14.4 | Quanto devo produzir amanhã? |  |  |  |
| 15.1 | Listas na resposta |  |  |  |
| 15.2 | Início da resposta |  |  |  |
| 15.3 | Quantidades de matéria-prima |  |  |  |
| 15.4 | Resposta a um áudio |  |  |  |

> Os casos 9.6, 10.4 e 11.4 dependem de decisões do Planning; ajuste o resultado esperado quando elas forem tomadas.
