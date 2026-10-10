# Checklist de DoR e DoD — Sprint 2

> **Status:** Sprint ainda não iniciada. Os itens abaixo são os critérios a validar durante a Sprint; marque `[x]` conforme forem atendidos. Itens com **"a definir"** dependem de decisão no Planning.

As US 05 e 06 compartilham o **custo unitário** dos produtos e as US 07 e 08 reaproveitam o mesmo cálculo com escopo de empresa (sem filtro de setor). Por isso, o cálculo de lucro e o de valor descartado devem ficar em um único *service*, usado pelo líder e pelo gerente.

---

## US05 — Produtos mais lucrativos (líder)
> *"Eu, como líder, quero saber quais produtos me trazem mais lucro, a fim de otimizar o tempo dos colaboradores."*

**Previsto em:** categoria `VENDAS` do Agente Roteador (já reconhecida, ainda sem tools registradas) + novo *service* de lucro. A confirmar no Planning.

### DoR
- [ ] Objetivo da User Story está claramente definido
- [ ] Usuário da funcionalidade está identificado (líder)
- [ ] Está definido como o setor do líder é informado (parâmetro `setor` na mensagem, com correção ortográfica via `normalizar_setor`)
- [ ] Fórmula de lucro está definida (a definir; proposta: (preço de venda − custo unitário) × quantidade vendida) e se o custo do descarte entra no cálculo
- [ ] Origem do preço de venda e do custo unitário está definida (o código atual não usa essas colunas: confirmar se já existem nos CSV ou se serão adicionadas)
- [ ] Período de análise está definido (dia, semana ou mês) e o que acontece quando o período não é informado
- [ ] Serão utilizados os csv `produtos_mercado.csv` e `vendas_supermercado_<mês>_<ano>.csv`
- [ ] Está definido como o ranking será apresentado (ordem decrescente, valores em R$)
- [ ] Critérios de aceite estão definidos
- [ ] Dependências necessárias estão identificadas (custo unitário compartilhado com a US06)

### DoD
- [ ] O líder consegue consultar os produtos mais lucrativos do seu setor
- [ ] O sistema apresenta os produtos do mais para o menos lucrativo, com o lucro de cada item em R$
- [ ] Os valores conferem com o cálculo manual feito sobre uma amostra dos CSV
- [ ] O setor com erro de digitação é corrigido por `normalizar_setor`
- [ ] Produtos sem vendas no período não distorcem o ranking
- [ ] O ranking permite ao líder priorizar o tempo dos colaboradores nos produtos de maior retorno
- [ ] A funcionalidade foi testada sem erros (casos 5.1 a 5.5 do Guia de Testes)
- [ ] Os critérios de aceite foram atendidos
- [ ] O resultado foi validado pelo líder ou responsável

---

## US06 — Reais descartados no setor (líder)
> *"Eu, como líder, quero saber quantos reais foram descartados, a fim de monitorar o impacto financeiro das perdas do meu setor."*

**Previsto em:** *services* financeiro de descarte, a partir de `procedures.descarte` + custo unitário. A confirmar no Planning.

### DoR
- [ ] Objetivo da User Story está claramente definido
- [ ] Usuário da funcionalidade está identificado (líder)
- [ ] Está definido como o setor do líder é informado (parâmetro `setor`)
- [ ] Fórmula do valor descartado está definida (a definir; proposta: unidades descartadas × custo unitário)
- [ ] Origem do custo unitário está definida (mesma fonte da US05)
- [ ] Período de análise está definido (dia, semana ou mês)
- [ ] Serão utilizados os csv `descartes_supermercado_<mês>_<ano>.csv` e `produtos_mercado.csv`
- [ ] Está definido como o resultado será apresentado (total do setor em R$ e detalhe por produto)
- [ ] Critérios de aceite estão definidos
- [ ] Dependências necessárias estão identificadas

### DoD
- [ ] O líder consegue consultar o valor descartado do seu setor em um dia ou período
- [ ] O sistema apresenta o total em R$ e o detalhamento por produto
- [ ] O valor em R$ é coerente com as unidades descartadas já exibidas na Sprint 1 (caso 3.1 do Guia de Testes da Sprint 1)
- [ ] A pergunta em **unidades** ("quantas unidades foram descartadas") continua respondida em unidades, sem virar R$
- [ ] O setor com erro de digitação é corrigido por `normalizar_setor`
- [ ] A funcionalidade foi testada sem erros (casos 6.1 a 6.4 do Guia de Testes)
- [ ] Os critérios de aceite foram atendidos
- [ ] O resultado foi validado pelo líder ou responsável

---

## US07 — Reais descartados na empresa (gerente)
> *"Eu, como gerente, quero saber quantos reais foram descartados, a fim de avaliar o custo global de desperdício da empresa."*

**Previsto em:** mesmo *service* da US06, sem filtro de setor. A confirmar no Planning.

### DoR
- [ ] Objetivo da User Story está claramente definido
- [ ] Usuário da funcionalidade está identificado (gerente)
- [ ] Está definido que o escopo é a empresa inteira (todos os setores)
- [ ] Está definido que o cálculo é o mesmo da US06, sem duplicar regra de negócio
- [ ] Período de análise está definido (dia, semana ou mês)
- [ ] Serão utilizados os csv `descartes_supermercado_<mês>_<ano>.csv` e `produtos_mercado.csv`
- [ ] Está definido como o resultado será apresentado (total geral e, quando solicitado, separado por setor)
- [ ] Critérios de aceite estão definidos
- [ ] Dependências necessárias estão identificadas (US06)

### DoD
- [ ] O gerente consegue consultar o valor total descartado pela empresa em um dia ou período
- [ ] O sistema apresenta o total geral em R$ e, quando solicitado, o valor de cada setor
- [ ] A soma dos valores por setor é igual ao total geral (verificação cruzada com a US06)
- [ ] A funcionalidade foi testada sem erros (casos 7.1 a 7.4 do Guia de Testes)
- [ ] Os critérios de aceite foram atendidos
- [ ] O resultado foi validado pelo gerente ou responsável

---

## US08 — Produtos mais lucrativos na empresa (gerente)
> *"Eu, como gerente, quero saber quais produtos me trazem mais lucro, a fim de orientar estrategicamente os setores."*

**Previsto em:** mesmo *service* de lucro da US05, sem filtro de setor e com agrupamento por setor. A confirmar no Planning.

### DoR
- [ ] Objetivo da User Story está claramente definido
- [ ] Usuário da funcionalidade está identificado (gerente)
- [ ] Está definido que o escopo é a empresa inteira e que o cálculo é o mesmo da US05
- [ ] Está definido se o ranking pode ser agrupado por setor e limitado a um número de itens (ex.: "os 5 mais lucrativos")
- [ ] Período de análise está definido (dia, semana ou mês)
- [ ] Serão utilizados os csv `produtos_mercado.csv` e `vendas_supermercado_<mês>_<ano>.csv`
- [ ] Critérios de aceite estão definidos
- [ ] Dependências necessárias estão identificadas (US05)

### DoD
- [ ] O gerente consegue consultar o ranking de lucro de todos os produtos da empresa
- [ ] O sistema indica o setor de cada produto e permite comparar os setores
- [ ] O lucro de cada produto é igual ao exibido na US05 para o setor correspondente (verificação cruzada)
- [ ] A funcionalidade foi testada sem erros (casos 8.1 a 8.4 do Guia de Testes)
- [ ] Os critérios de aceite foram atendidos
- [ ] O resultado foi validado pelo gerente ou responsável
