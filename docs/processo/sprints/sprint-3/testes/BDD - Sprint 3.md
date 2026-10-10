# Cenários BDD — Sprint 3

**BDD (Behavior-Driven Development)** é uma técnica para escrever critérios de aceitação em linguagem natural, estruturados em três partes: **Dado** (o contexto antes da ação), **Quando** (a ação realizada pelo usuário) e **Então** (o resultado esperado). O objetivo é descrever o comportamento do sistema de forma clara tanto para quem desenvolve quanto para quem não é da área técnica.

Este documento mapeia, no formato **Dado / Quando / Então**, o cenário de teste básico de cada User Story da Sprint 3, conforme exigido pela [DoR](../README.md#dor) ("Critérios de Aceitação"). As variações de pergunta a testar estão no [Guia de Testes](./Guia%20de%20Testes%20-%20Sprint%203.md).

---

## Rank 9 — Perguntas por áudio (gestor)

> US-09: Eu, como gestor, quero interagir com o assistente de análise de dados enviando perguntas por áudio, a fim de obter insights das planilhas de forma fluida e sem contato manual (semelhante a uma Alexa).

**Dado** que o gestor está conversando com a MIA pelo Telegram<br>
**Quando** ele envia uma mensagem de voz dizendo "O que devo produzir hoje?"<br>
**Então** a MIA transcreve o áudio e responde com o mesmo conteúdo que daria à pergunta digitada, sem exigir nenhum contato manual com o teclado

---

## Rank 10 — Matéria-prima para o dia seguinte (líder)

> US-10: Eu, como líder, quero saber quanta matéria-prima eu preciso deixar preparada para o dia seguinte, a fim de otimizar o tempo e reduzir o desperdício de matéria-prima.

**Dado** que o líder está conversando com a MIA pelo Telegram<br>
**Quando** ele envia a mensagem "Quanta matéria-prima preciso deixar preparada para amanhã na padaria?"<br>
**Então** a MIA responde com a lista de matérias-primas do setor **Padaria**, com a quantidade e a unidade de cada uma, calculada a partir da previsão de produção de amanhã e do consumo de cada produto

---

## Rank 11 — Matérias-primas disponíveis para transferir (líder)

> US-11: Eu, como líder, quero saber quais matérias-primas estão disponíveis para transferir a outros setores, a fim de reaproveitar recursos parados e evitar compras desnecessárias.

**Dado** que o líder está conversando com a MIA pelo Telegram<br>
**Quando** ele envia a mensagem "Quais matérias-primas estão disponíveis para transferir para outros setores?"<br>
**Então** a MIA responde com as matérias-primas que têm sobra, informando a quantidade e o setor que as possui, sem incluir o que o próprio setor precisa no dia seguinte

---

## Rank 12 — Motivo da transferência de um produto (gerente)

> US-12: Eu, como gerente, quero saber por que o produto X está sendo transferido de setor, a fim de identificar falhas no planejamento original da produção.

**Dado** que o gerente está conversando com a MIA pelo Telegram<br>
**Quando** ele envia a mensagem "Por que a coxinha está sendo transferida de setor?"<br>
**Então** a MIA responde com o motivo registrado da transferência, informando o setor de origem, o setor de destino e a data; se não houver registro, informa que não encontrou, sem inventar um motivo

---
