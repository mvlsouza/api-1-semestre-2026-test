# Checklist de DoR e DoD — Sprint 3

> **Status:** Sprint ainda não iniciada. Os itens abaixo são os critérios a validar durante a Sprint; marque `[x]` conforme forem atendidos. Itens com **"a definir"** dependem de decisão no Planning.

A US09 adiciona uma nova **forma de entrada** (voz) e não depende das demais. As US 10, 11 e 12 dependem de dados que ainda não existem na base (receitas, estoque e transferências) e a US10 reaproveita a previsão de produção da Sprint 1. Em todas, a MIA deve informar quando não houver registro, em vez de inventar uma resposta.

---

## US09 — Perguntas por áudio (gestor)
> *"Eu, como gestor, quero interagir com o assistente de análise de dados enviando perguntas por áudio, a fim de obter insights das planilhas de forma fluida e sem contato manual (semelhante a uma Alexa)."*

**Previsto em:** `bot/telegram_bot.py` (hoje a mensagem de voz recebe a resposta de formato não suportado) + etapa de transcrição antes do `processar_mensagem`. A confirmar no Planning.

### DoR
- [ ] Objetivo da User Story está claramente definido
- [ ] Usuário da funcionalidade está identificado (gestor)
- [ ] Solução de transcrição escolhida e executada **localmente** (restrição do projeto: sem APIs externas de terceiros)
- [ ] Idioma (pt-BR), formato do áudio do Telegram e duração máxima estão definidos
- [ ] Está definido se a resposta será em texto, em voz ou em ambos (a definir)
- [ ] Está definido o comportamento quando a transcrição falha (áudio vazio, ruído ou longo demais)
- [ ] Exemplos de perguntas faladas estão mapeados (as mesmas das Sprints 1 e 2, ditas em voz alta)
- [ ] Critérios de aceite estão definidos
- [ ] Dependências necessárias estão identificadas

### DoD
- [ ] O gestor envia um áudio e recebe a resposta correta, sem digitar nada
- [ ] A resposta ao áudio tem o mesmo conteúdo da resposta à pergunta digitada
- [ ] Áudio vazio, com ruído ou acima do limite recebe uma mensagem amigável, sem travar o bot
- [ ] Mensagens de texto continuam funcionando; formatos não suportados (ex.: foto) continuam recusados
- [ ] A transcrição funciona sem nenhuma API externa de terceiros
- [ ] Arquivos de áudio temporários são apagados após o uso
- [ ] O fluxo de áudio foi documentado no `arquitetura.md`
- [ ] A funcionalidade foi testada sem erros (casos 9.1 a 9.9 do Guia de Testes)
- [ ] Os critérios de aceite foram atendidos
- [ ] O resultado foi validado pelo gestor ou responsável

---

## US10 — Matéria-prima para o dia seguinte (líder)
> *"Eu, como líder, quero saber quanta matéria-prima eu preciso deixar preparada para o dia seguinte, a fim de otimizar o tempo e reduzir o desperdício de matéria-prima."*

**Previsto em:** `services.producao` (previsão do dia, US01/US02) × consumo de matéria-prima por produto (novo CSV). A confirmar no Planning.

### DoR
- [ ] Objetivo da User Story está claramente definido
- [ ] Usuário da funcionalidade está identificado (líder)
- [ ] Está definida a origem do consumo de matéria-prima por unidade de cada produto (receita; ainda inexistente na base)
- [ ] Está definida a unidade de medida de cada matéria-prima (kg, L, unidade)
- [ ] Está definido que a data alvo é o dia seguinte e que o parâmetro `data` aceita "amanhã"
- [ ] Está definido que a necessidade parte da previsão de produção já existente (média de dias similares + 30%)
- [ ] Está definido como o resultado será apresentado (matéria-prima, quantidade e unidade, por setor)
- [ ] Critérios de aceite estão definidos
- [ ] Dependências necessárias estão identificadas (previsão de produção da Sprint 1)

### DoD
- [ ] O líder consegue consultar a matéria-prima necessária para amanhã no seu setor
- [ ] O sistema apresenta cada matéria-prima com quantidade e unidade
- [ ] A mesma matéria-prima usada por vários produtos aparece somada
- [ ] A quantidade é coerente com a previsão de produção do mesmo dia (verificação cruzada)
- [ ] O setor com erro de digitação é corrigido por `normalizar_setor`
- [ ] A funcionalidade foi testada sem erros (casos 10.1 a 10.6 do Guia de Testes)
- [ ] Os critérios de aceite foram atendidos
- [ ] O resultado foi validado pelo líder ou responsável

---

## US11 — Matérias-primas disponíveis para transferir (líder)
> *"Eu, como líder, quero saber quais matérias-primas estão disponíveis para transferir a outros setores, a fim de reaproveitar recursos parados e evitar compras desnecessárias."*

**Previsto em:** novo *service* de estoque de matéria-prima, usando a necessidade calculada na US10. A confirmar no Planning.

### DoR
- [ ] Objetivo da User Story está claramente definido
- [ ] Usuário da funcionalidade está identificado (líder)
- [ ] Está definida a origem do estoque atual de matéria-prima por setor (ainda inexistente na base)
- [ ] Está definida a regra de "disponível para transferir" (a definir; proposta: estoque menos a necessidade prevista da US10)
- [ ] Está definido como o resultado será apresentado (matéria-prima, quantidade e setor que a possui)
- [ ] Critérios de aceite estão definidos
- [ ] Dependências necessárias estão identificadas (US10)

### DoD
- [ ] O líder consegue consultar as matérias-primas com sobra
- [ ] O sistema apresenta quantidade e setor de cada item disponível
- [ ] Nenhum item é listado como disponível quando o próprio setor precisa dele no dia seguinte (verificação cruzada com a US10)
- [ ] Quando não há sobra, a MIA informa isso, sem inventar itens
- [ ] A funcionalidade foi testada sem erros (casos 11.1 a 11.5 do Guia de Testes)
- [ ] Os critérios de aceite foram atendidos
- [ ] O resultado foi validado pelo líder ou responsável

---

## US12 — Motivo da transferência de um produto (gerente)
> *"Eu, como gerente, quero saber por que o produto X está sendo transferido de setor, a fim de identificar falhas no planejamento original da produção."*

**Previsto em:** novo *service* de transferências, a partir de um registro com data, produto, setor de origem, setor de destino e motivo. A confirmar no Planning.

### DoR
- [ ] Objetivo da User Story está claramente definido
- [ ] Usuário da funcionalidade está identificado (gerente)
- [ ] Está definido o que é uma "transferência" (produto que muda de setor ou matéria-prima enviada a outro setor)
- [ ] Está definida a origem do registro de transferências, com o campo de **motivo** (ainda inexistente na base)
- [ ] Está definido o comportamento quando o produto não existe ou não tem transferência registrada
- [ ] Está definido como o resultado será apresentado (motivo, setor de origem, setor de destino e data)
- [ ] Critérios de aceite estão definidos
- [ ] Dependências necessárias estão identificadas

### DoD
- [ ] O gerente consegue perguntar o motivo da transferência de um produto pelo nome
- [ ] O motivo apresentado corresponde exatamente ao registro
- [ ] Produto inexistente ou sem transferência registrada recebe uma resposta clara, sem motivo inventado
- [ ] O nome do produto é reconhecido independentemente de maiúsculas e minúsculas
- [ ] A funcionalidade foi testada sem erros (casos 12.1 a 12.5 do Guia de Testes)
- [ ] Os critérios de aceite foram atendidos
- [ ] O resultado foi validado pelo gerente ou responsável
