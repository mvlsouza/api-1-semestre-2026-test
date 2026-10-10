# Guia de Testes — Sprint 2

Este documento é um **guia para você testar a MIA na prática**, e não um relatório do que já foi testado. A ideia é: você envia cada mensagem sugerida no Telegram, compara com o resultado esperado, anota o que realmente aconteceu e marca o status na tabela do final. Os resultados da execução serão registrados no Relatório de Testes da Sprint 2, criado ao final da execução.

## Pré-requisitos antes de começar

- [ ] Ollama aberto, com o modelo `ollama pull gemma4:e2b` baixado
- [ ] Arquivo `.env` configurado em `backend/src/.env` com `TELEGRAM_BOT_KEY` válido
- [ ] `python main.py` rodando sem erros no terminal (verifique se aparece "[IA] Modelo carregado e pronto para responder.")
- [ ] Bot respondendo a `/start` no Telegram
- [ ] CSVs com **preço de venda** e **custo unitário** dos produtos disponíveis em `backend/dados/` (definição da Sprint 2)

---

## US05 — Produtos mais lucrativos (líder)

| ID | Mensagem para enviar | Resultado esperado |
|---|---|---|
| 5.1 | "Quais produtos da padaria me dão mais lucro?" | Ranking só com produtos da Padaria, do maior para o menor lucro, com valores em R$ |
| 5.2 | "Qual o produto mais lucrativo do açougue em setembro?" | Destaca o primeiro do ranking do Açougue para o período citado |
| 5.3 | "Me mostra o ranking de lucro da cozinha" | Mesmo cálculo, fraseado diferente: verifica se o Agente Roteador entende variações de pergunta |
| 5.4 | "Quais produtos da padaira dão mais lucro?" (erro de digitação proposital) | `normalizar_setor` deve corrigir para "Padaria" mesmo com o erro |
| 5.5 | "Quais produtos dão mais lucro?" (sem informar o setor) | Comportamento definido no Planning: ranking de todos os setores ou pedido do setor ao líder |

---

## US06 — Reais descartados no setor (líder)

| ID | Mensagem para enviar | Resultado esperado |
|---|---|---|
| 6.1 | "Quantos reais foram descartados ontem na padaria?" | Valor total em R$ descartado pela Padaria no dia, com detalhe por produto |
| 6.2 | "Quanto dinheiro eu perdi com descarte no açougue em setembro?" | Mesmo cálculo para o período; verifica variação de fraseado |
| 6.3 | "Quanto perdi em reais com cada produto da cozinha ontem?" | Valor descartado por produto da Cozinha/Rotisseria |
| 6.4 | "Quantos reais foram descartados no acugue ontem?" (erro de digitação proposital) | `normalizar_setor` deve corrigir para "Açougue" mesmo com o erro |

---

## US07 — Reais descartados na empresa (gerente)

| ID | Mensagem para enviar | Resultado esperado |
|---|---|---|
| 7.1 | "Quantos reais foram descartados ontem na empresa toda?" | Valor total em R$ somando todos os setores |
| 7.2 | "Qual foi o custo total de desperdício em setembro?" | Valor total do período; fraseado diferente |
| 7.3 | "Quantos reais foram descartados ontem? Separe por setores" | Total geral e o valor de cada setor, agrupados |
| 7.4 | Verificação cruzada: repetir o caso 6.1 para os 5 setores e somar | A soma dos setores é igual ao total do caso 7.1 |

---

## US08 — Produtos mais lucrativos na empresa (gerente)

| ID | Mensagem para enviar | Resultado esperado |
|---|---|---|
| 8.1 | "Quais produtos da empresa trazem mais lucro?" | Ranking geral de todos os setores, ordenado por lucro em R$, indicando o setor de cada produto |
| 8.2 | "Quais setores têm os produtos mais lucrativos?" | Lucro agrupado por setor, permitindo comparar os setores |
| 8.3 | "Me mostra os 5 produtos mais lucrativos do mercado" | Ranking limitado a 5 itens |
| 8.4 | Verificação cruzada: comparar o lucro de um produto do caso 8.1 com o mesmo produto no caso 5.1 | Os valores devem ser iguais |

---

## Regressão — funcionalidades da Sprint 1

Garante que as novas perguntas financeiras não quebraram o que já funcionava.

| ID | Mensagem para enviar | Resultado esperado |
|---|---|---|
| 9.1 | "O que devo produzir hoje?" | Continua listando só os **nomes** dos produtos (caso 1.1 da Sprint 1) |
| 9.2 | "Quantas unidades devo produzir hoje na padaria?" | Continua devolvendo nome e quantidade, só da Padaria (caso 2.3 da Sprint 1) |
| 9.3 | "O que foi produzido ontem na padaria?" | Continua mostrando Total Produzido, Vendas e Descarte **em unidades** (caso 3.1 da Sprint 1) |
| 9.4 | "Quais produtos vocês têm?" | Continua listando o catálogo completo (caso 5.1 da Sprint 1) |

---

## Roteamento e comportamento social (`agentes.py`)

| ID | Mensagem para enviar | Resultado esperado |
|---|---|---|
| 10.1 | "Quantas unidades de coxinha foram descartadas ontem?" | Responde em **unidades**, sem converter para R$ (não confunde com a US06) |
| 10.2 | "Oi" / "Bom dia" | Agente Roteador identifica `SAUDACAO`; resposta curta e simpática, sem acionar nenhuma tool |
| 10.3 | "Qual é a capital da França?" (fora do escopo) | Agente Roteador identifica `INVALIDO`; resposta de recusa padrão |
| 10.4 | "Quanto lucro a concorrência teve?" (fora do escopo) | Recusa padrão: a MIA só responde sobre os dados do próprio supermercado, sem inventar valores |
| 10.5 | Enviar um áudio ou uma foto | Mensagem fixa de formato não suportado, sem acionar a IA |

---

## Formatação da resposta

| ID | O que verificar | Resultado esperado |
|---|---|---|
| 11.1 | Valores monetários | Sempre no padrão brasileiro, com duas casas decimais (ex.: R$ 1.234,56) |
| 11.2 | Listas na resposta | Sempre usam `•`, nunca `*` |
| 11.3 | Início da resposta | Nunca começa repetindo saudação ("Olá! Aqui está...") |
| 11.4 | Ranking longo | A ordem decrescente de lucro ou valor é preservada na resposta final do Agente Redator |

---

## Tabela de registro (preencha ao testar)

| Caso | Mensagem enviada | Resultado obtido | Status | Observações |
|---|---|---|---|---|
| 5.1 | Quais produtos da padaria me dão mais lucro? |  |  |  |
| 5.2 | Qual o produto mais lucrativo do açougue em setembro? |  |  |  |
| 5.3 | Me mostra o ranking de lucro da cozinha |  |  |  |
| 5.4 | Quais produtos da padaira dão mais lucro? |  |  |  |
| 5.5 | Quais produtos dão mais lucro? |  |  |  |
| 6.1 | Quantos reais foram descartados ontem na padaria? |  |  |  |
| 6.2 | Quanto dinheiro eu perdi com descarte no açougue em setembro? |  |  |  |
| 6.3 | Quanto perdi em reais com cada produto da cozinha ontem? |  |  |  |
| 6.4 | Quantos reais foram descartados no acugue ontem? |  |  |  |
| 7.1 | Quantos reais foram descartados ontem na empresa toda? |  |  |  |
| 7.2 | Qual foi o custo total de desperdício em setembro? |  |  |  |
| 7.3 | Quantos reais foram descartados ontem? Separe por setores |  |  |  |
| 7.4 | Verificação cruzada: repetir o caso 6.1 para os 5 setores e somar |  |  |  |
| 8.1 | Quais produtos da empresa trazem mais lucro? |  |  |  |
| 8.2 | Quais setores têm os produtos mais lucrativos? |  |  |  |
| 8.3 | Me mostra os 5 produtos mais lucrativos do mercado |  |  |  |
| 8.4 | Verificação cruzada: comparar o lucro de um produto do caso 8.1 com o mesmo produto no caso 5.1 |  |  |  |
| 9.1 | O que devo produzir hoje? |  |  |  |
| 9.2 | Quantas unidades devo produzir hoje na padaria? |  |  |  |
| 9.3 | O que foi produzido ontem na padaria? |  |  |  |
| 9.4 | Quais produtos vocês têm? |  |  |  |
| 10.1 | Quantas unidades de coxinha foram descartadas ontem? |  |  |  |
| 10.2 | Oi" / "Bom dia |  |  |  |
| 10.3 | Qual é a capital da França? |  |  |  |
| 10.4 | Quanto lucro a concorrência teve? |  |  |  |
| 10.5 | Enviar um áudio ou uma foto |  |  |  |
| 11.1 | Valores monetários |  |  |  |
| 11.2 | Listas na resposta |  |  |  |
| 11.3 | Início da resposta |  |  |  |
| 11.4 | Ranking longo |  |  |  |

> O caso 5.5 depende de uma decisão do Planning; ajuste o resultado esperado quando ela for tomada.
