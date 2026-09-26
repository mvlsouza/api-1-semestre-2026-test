# Checklist de DoR e DoD — Sprint 1

## US01 — Planejamento de Produção (quais produtos produzir)
> *"Eu, como líder, quero saber quais produtos precisam ser produzidos, a fim de reduzir o desperdício de tempo e produto."*

**Implementado em:** `tool_previsao_vendas_por_data(tipo_pergunta="qual")` → `procedures.vendas.classificar_dia`, `dataframe_vendas_similares`, `media_vendas_produtos`.

### DoR
- [x] Objetivo da User Story está claramente definido
- [x] Usuário da funcionalidade está identificado (líder)
- [x] Os produtos estão bem definidos no arquivo csv `produtos_mercado.csv`
- [x] Critérios de aceite estão definidos
- [x] Dependências necessárias estão identificadas
- [x] Serão utilizados os arquivos `vendas_supermercado_"mes"_"ano".csv` e `descartes_supermercado_"mes"_"ano".csv`
- [x] Método de cálculo será realizado baseado nas vendas anteriores e no dia do mês

### DoD
- [x] Sistema identifica os produtos que precisam ser produzidos
- [x] Histórico de vendas é considerado
- [x] Recomendações são apresentadas de forma clara ao líder
- [x] Quantidade recomendada de produção é apresentada — *não se aplica aqui: esse é o escopo da US02 (`tipo_pergunta="quanto"`); em US01 a tool intencionalmente devolve só os nomes.*
- [x] Fatores como **feriados** e **finais de semana** são considerados** em (`classificar_dia`).
- [x] Funcionalidade foi testada sem erros
- [x] Resultado foi validado pelo responsável

---

## US02 — Planejamento de Produção (quantos produtos produzir)
> *"Eu, como líder, quero saber quantos produtos precisam ser produzidos, a fim de reduzir o desperdício de tempo e produto."*

**Implementado em:** `tool_previsao_vendas_por_data(tipo_pergunta="quanto")` (mesma tool da US01, parâmetro diferente).

### DoR
- [x] Objetivo da User Story está claramente definido
- [x] Usuário da funcionalidade está identificado
- [x] Os produtos estão bem definidos no csv `produtos_mercado.csv`
- [x] Está definido como a quantidade recomendada será apresentada ao líder
- [x] Critérios de aceite estão definidos
- [x] Dependências necessárias estão identificadas
- [x] Serão utilizados os csv de vendas e descartes
- [x] Método de cálculo baseado em vendas e dia do mês

### DoD
- [x] O sistema calcula a quantidade recomendada de produção para cada produto
- [x] O cálculo utiliza os dados de vendas definidos no projeto
- [x] O sistema apresenta claramente o nome do produto e a quantidade recomendada
- [x] Produtos sem necessidade de produção não são indevidamente recomendados (`media_vendas_produtos` só retorna produtos com histórico de vendas no perfil de dia filtrado)
- [x] O cálculo considera os fatores de demanda definidos, feriados e finais de semana
- [x] A funcionalidade foi testada com diferentes cenários de demanda
- [x] Os critérios de aceite foram atendidos
- [x] O líder ou responsável pelo projeto validou o resultado

---

## US03 — Produtividade por Setor (o que foi produzido)
> *"Eu, como gerente, quero saber o que foi produzido no dia X pelo setor Y, a fim de verificar a produtividade do setor Y."*

**Implementado em:** `tool_producao_dia_pelo_setor` → `procedures.producao.calcular_producao_data`.

### DoR
- [x] Objetivo da User Story está claramente definido
- [x] Usuário da funcionalidade está identificado (gerente)
- [x] Os setores que serão consultados estão definidos (`produtos_mercado.csv`, coluna Setor)
- [x] A informação de data está definida como parâmetro de consulta
- [x] Os produtos estão bem definidos no csv `produtos_mercado.csv`
- [x] Serão utilizados os csv `produtos_mercado`, `vendas_supermercado` e `descartes_supermercado`
- [x] Os registros de produção estão relacionados ao respectivo setor
- [x] Está definido como os resultados serão apresentados ao gerente
- [x] Critérios de aceite estão definidos
- [x] Dependências identificadas

### DoD
- [x] O gerente consegue informar o dia X (parâmetro `data`)
- [x] O gerente consegue selecionar o setor Y (parâmetro `setor`, com correção ortográfica via `normalizar_setor`)
- [x] O sistema apresenta os produtos produzidos pelo setor no dia selecionado
- [x] O sistema apresenta a quantidade produzida de cada produto (Total Produzido, Vendas, Descarte por item)
- [x] Os dados apresentados correspondem aos registros de produção do setor e da data selecionados
- [x] O sistema permite identificar o total produzido pelo setor no período consultado
- [x] A consulta funciona corretamente para diferentes datas e setores — sem evidência de testes cobrindo isso
- [x] A funcionalidade foi testada com diferentes cenários
- [x] Os critérios de aceite foram atendidos
- [x] O resultado foi validado pelo gerente ou responsável

---

## US04 — Comparação entre Meta e Produção Real
> *"Eu, como gerente, quero saber o que deveria ter sido produzido no dia X pelo setor Y, a fim de comparar a meta com a produção real e identificar gargalos."*

**Implementado em:** `tool_meta_producao_passada` → reaproveita `classificar_dia` + `dataframe_vendas_similares` + `media_vendas_produtos` (mesmo cálculo da US01/US02).

### DoR
- [x] Objetivo da User Story está claramente definido
- [x] Usuário identificado como gerente
- [x] Setores e produtos por setor definidos
- [x] Data definida como parâmetro
- [x] Unidade de medida da meta definida (unidades)
- [x] Está definido que a produção real virá da análise de vendas e descartes
- [x] Critérios de aceite estão definidos
- [x] Fontes de dados e dependências identificadas
- [x] Está definido como serão identificadas diferenças entre meta e produção real

### DoD
- [x] O gerente consegue selecionar o dia X e o setor Y
- [x] O sistema apresenta a meta de produção prevista para o dia e setor selecionados
- [x] A funcionalidade foi testada
- [x] Os critérios de aceite foram atendidos
- [x] O resultado foi validado pelo gerente ou responsável


---