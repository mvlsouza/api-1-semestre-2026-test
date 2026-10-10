# Cenários BDD — Sprint 2

**BDD (Behavior-Driven Development)** é uma técnica para escrever critérios de aceitação em linguagem natural, estruturados em três partes: **Dado** (o contexto antes da ação), **Quando** (a ação realizada pelo usuário) e **Então** (o resultado esperado). O objetivo é descrever o comportamento do sistema de forma clara tanto para quem desenvolve quanto para quem não é da área técnica.

Este documento mapeia, no formato **Dado / Quando / Então**, o cenário de teste básico de cada User Story da Sprint 2, conforme exigido pela [DoR](../README.md#dor) ("Critérios de Aceitação"). As variações de pergunta a testar estão no [Guia de Testes](./Guia%20de%20Testes%20-%20Sprint%202.md).

---

## Rank 5 — Produtos mais lucrativos (líder)

> US-05: Eu, como líder, quero saber quais produtos me trazem mais lucro, a fim de otimizar o tempo dos colaboradores.

**Dado** que o líder está conversando com a MIA pelo Telegram<br>
**Quando** ele envia a mensagem "Quais produtos da padaria me dão mais lucro?"<br>
**Então** a MIA responde com o ranking dos produtos do setor **Padaria**, do mais para o menos lucrativo, mostrando o lucro de cada item em R$

---

## Rank 6 — Reais descartados no setor (líder)

> US-06: Eu, como líder, quero saber quantos reais foram descartados, a fim de monitorar o impacto financeiro das perdas do meu setor.

**Dado** que o líder está conversando com a MIA pelo Telegram<br>
**Quando** ele envia a mensagem "Quantos reais foram descartados ontem na padaria?"<br>
**Então** a MIA responde com o valor total em R$ descartado pelo setor **Padaria** no dia anterior, com o detalhamento por produto (unidades descartadas × custo unitário)

---

## Rank 7 — Reais descartados na empresa (gerente)

> US-07: Eu, como gerente, quero saber quantos reais foram descartados, a fim de avaliar o custo global de desperdício da empresa.

**Dado** que o gerente está conversando com a MIA pelo Telegram<br>
**Quando** ele envia a mensagem "Quantos reais foram descartados ontem na empresa toda?"<br>
**Então** a MIA responde com o valor total em R$ descartado por **todos os setores** no dia anterior, igual à soma dos valores obtidos setor a setor

---

## Rank 8 — Produtos mais lucrativos na empresa (gerente)

> US-08: Eu, como gerente, quero saber quais produtos me trazem mais lucro, a fim de orientar estrategicamente os setores.

**Dado** que o gerente está conversando com a MIA pelo Telegram<br>
**Quando** ele envia a mensagem "Quais produtos da empresa trazem mais lucro?"<br>
**Então** a MIA responde com o ranking dos produtos de **todos os setores**, do mais para o menos lucrativo, indicando o setor e o lucro em R$ de cada item

---
