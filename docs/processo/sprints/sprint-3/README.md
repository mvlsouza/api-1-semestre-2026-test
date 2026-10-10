# Documentação - Sprint 3

<div align="center">
  <!-- Imagem que aparece apenas no Modo Escuro -->
  <img src="../../../img/logo-mclorem-dark.png#gh-dark-mode-only" alt="logo da McLorem Tecnologia" width="200">
  
  <!-- Imagem que aparece apenas no Modo Claro -->
  <img src="../../../img/logo-mclorem-light.png#gh-light-mode-only" alt="logo da McLorem Tecnologia" width="200">
  
  <h3>MIA - Assistente de Análise de Dados</h3>
</div>

<br>

<p align="center">
  <a href ="#desafio"> Desafio</a> &nbsp;&bull;&nbsp;
  <a href ="#us"> User Stories</a> &nbsp;&bull;&nbsp;  
  <a href ="#dor">DoR</a> &nbsp;&bull;&nbsp;
  <a href ="#dod">DoD</a> &nbsp;&bull;&nbsp;
  <a href ="#burndown"> Burndown</a> &nbsp;&bull;&nbsp;
  <a href ="#equipe"> Equipe</a>
</p>

---

> [!IMPORTANT]
> **Status da Sprint:**  Não iniciada 🔜

## 🏅 Desafio <a id="desafio"></a>

Ampliar a MIA em duas frentes: uma **nova forma de interação por voz** e a **gestão de matéria-prima**. Na primeira, o gestor passa a enviar perguntas por áudio no Telegram e a receber a resposta sem contato manual, como em um assistente de voz. O desafio é converter fala em texto e devolvê-la ao mesmo fluxo de agentes já existente, sem ferramentas de terceiros: a restrição de não utilizar APIs externas exige uma solução de transcrição executada localmente, com tratamento de áudios ruins, vazios ou longos demais. Na segunda frente, é preciso modelar em CSV a relação entre produtos e matérias-primas (consumo por unidade produzida), o estoque por setor e o histórico de transferências entre setores com seu motivo, para responder quanta matéria-prima preparar para o dia seguinte (reaproveitando a previsão de produção da Sprint 1), o que está disponível para transferir e por que um produto foi transferido. Esses dados ainda não existem na base atual e precisam ser definidos no planejamento, e as respostas nunca devem inventar informações quando não houver registro.

## 📋 User Stories <a id="us"></a>

| $\textsf{\textbf{Capacidade estimada da Equipe por Sprint:}}$ | $\textsf{55 Story Points}$ |
|---|---|
| $\color{#2e8b57}{\textsf{\textbf{Meta da Sprint:}}}$ | $\textsf{User Stories de rank 9 e rank 10 (\textit{Story Points a estimar no Planning})}$ |
| $\textsf{\textbf{Previsão da Sprint} (\textit{extras, sem compromisso de entrega}):}$ | $\textsf{User Stories de rank 11 e rank 12 (\textit{Story Points a estimar no Planning})}$ |

| Rank | Prioridade | User Story | Story Points | Sprint | Status |
| :--: | :--------: | :--- | :----------: | :----: | :----: |
| $\color{#2e8b57}{\textsf{\textbf{9}}}$ | $\color{#2e8b57}{\textsf{\textbf{Baixa}}}$ | $\color{#2e8b57}{\textsf{\textbf{Eu, como gestor, quero interagir com o assistente de análise de dados enviando perguntas por áudio, a fim de obter insights das planilhas de forma fluida e sem contato manual (semelhante a uma Alexa).}}}$ | $\color{#2e8b57}{\textsf{\textbf{A estimar}}}$ | $\color{#2e8b57}{\textsf{\textbf{3}}}$ | ⏳ |
| $\color{#2e8b57}{\textsf{\textbf{10}}}$ | $\color{#2e8b57}{\textsf{\textbf{Baixa}}}$ | $\color{#2e8b57}{\textsf{\textbf{Eu, como líder, quero saber quanta matéria-prima eu preciso deixar preparada para o dia seguinte, a fim de otimizar o tempo e reduzir o desperdício de matéria-prima.}}}$ | $\color{#2e8b57}{\textsf{\textbf{A estimar}}}$ | $\color{#2e8b57}{\textsf{\textbf{3}}}$ | ⏳ |
| $\textsf{11}$ | $\textsf{Baixa}$ | $\textsf{Eu, como líder, quero saber quais matérias-primas estão disponíveis para transferir a outros setores, a fim de reaproveitar recursos parados e evitar compras desnecessárias.}$ | $\textsf{\textit{A estimar}}$ | $\textsf{3}$ | ⏳ |
| $\textsf{12}$ | $\textsf{Baixa}$ | $\textsf{Eu, como gerente, quero saber por que o produto X está sendo transferido de setor, a fim de identificar falhas no planejamento original da produção.}$ | $\textsf{\textit{A estimar}}$ | $\textsf{3}$ | ⏳ |

---

## 🏅 DoR - Definition of Ready <a id="dor"></a>

A avaliação detalhada de DoR e DoD, User Story por User Story, está em [`Checklist - Sprint 3`](./Checklist%20-%20Sprint%203.md).

| Critério | Descrição |
| :--- | :--- |
| **Clareza na Descrição** | A User Story está escrita no formato: "Eu, como [papel], quero [ação], a fim de [objetivo/valor]". |
| **Critérios de Aceitação** | A história possui critérios claros e pelo menos um cenário de teste básico (BDD) mapeado (Dado que... Quando... Então...). |
| **Independente** | A história pode ser desenvolvida sem depender de tarefas bloqueantes dentro da mesma Sprint. |
| **Compreensão Compartilhada** | A equipe entende o propósito e estimou o esforço da tarefa (Story Points definidos). |
| **Mapeamento de Intenções** | Estão documentados exemplos reais de frases em linguagem natural que o usuário pode enviar (ex: "o que eu devo fazer hoje?", "tem produto pra agora?"). |
| **Critérios Técnicos** | Está definido o que o modelo via **DSPy** precisará extrair da frase (parâmetros) e qual arquivo/coluna estática o **Pandas** deverá ler. |

## 🏅 DoD - Definition of Done <a id="dod"></a>

| Critério | Descrição |
| :--- | :--- |
| **Critérios Atendidos** | Todos os critérios de aceitação e cenários de teste da User Story foram cumpridos e validados com sucesso. |
| **Interpretação Validada (NLP)** | A IA interpretou corretamente diferentes variações da mesma pergunta em texto livre, acionando a filtragem correta no Pandas. |
| **Código Revisado** | O código passou por Code Review (Pull Request revisado e aprovado por pelo menos um outro membro da equipe). |
| **Documentação Atualizada** | As novas capacidades de interpretação do bot, a estrutura dos módulos DSPy e os mapeamentos dos CSVs estáticos foram atualizados no README.md. |
| **Integração Validada** | A nova capacidade de resposta não confunde a IA em relação a outras perguntas já suportadas e o bot lida bem com frases fora de contexto. |
| **Validação do PO** | O Product Owner conversou de forma natural com o bot no Telegram e confirmou que o retorno atende à regra de negócio. |
| **Pronto para Deploy** | O código está limpo, mergeado na branch principal e pronto para ser executado. |

## 🏅 Sprint Burndown <a id="burndown"></a>

> [!NOTE]
> O gráfico de Burndown será publicado ao final da Sprint.

## 🎓 Equipe <a id="equipe"></a>

<div align="center">
  <table>
    <tr>
      <td align="center">
        <a href="https://github.com/hcastrosilva96">
          <img src="https://github.com/hcastrosilva96.png" width="115px;" alt="Foto de Henrique de Castro"/>
        </a><br>
        <sub><b>Henrique de Castro</b></sub><br>
        <sub>Product Owner</sub><br>
        <a href="https://github.com/hcastrosilva96"><img src="https://img.shields.io/badge/-GitHub-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub"/></a> <a href="https://www.linkedin.com/in/henrique-castro-silva-6568a012b/"><img src="https://img.shields.io/badge/-LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
      </td>
      <td align="center">
        <a href="https://github.com/FelipeMoraisOC">
          <img src="https://github.com/FelipeMoraisOC.png" width="115px;" alt="Foto de Felipe Morais"/>
        </a><br>
        <sub><b>Felipe Morais</b></sub><br>
        <sub>Scrum Master</sub><br>
        <a href="https://github.com/FelipeMoraisOC"><img src="https://img.shields.io/badge/-GitHub-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub"/></a> <a href="https://www.linkedin.com/in/felipemoraisoc/"><img src="https://img.shields.io/badge/-LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
      </td>
    </tr>
  </table>
  <table>
    <tr>
      <td align="center">
        <a href="https://github.com/mirelacristina">
          <img src="https://github.com/mirelacristina.png" width="100px;" alt="Foto de Mirela Cristina"/>
        </a><br>
        <sub><b>Mirela Cristina</b></sub><br>
        <sub>Dev Team</sub><br>
        <a href="https://github.com/mirelacristina"><img src="https://img.shields.io/badge/-GitHub-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub"/></a> <a href="https://www.linkedin.com/in/mirela-cristina-4325723a6/"><img src="https://img.shields.io/badge/-LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
      </td>
      <td align="center">
        <a href="https://github.com/eduardogranja">
          <img src="https://github.com/eduardogranja.png" width="100px;" alt="Foto de Eduardo Granja"/>
        </a><br>
        <sub><b>Eduardo Granja</b></sub><br>
        <sub>Dev Team</sub><br>
        <a href="https://github.com/eduardogranja"><img src="https://img.shields.io/badge/-GitHub-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub"/></a> <a href="https://www.linkedin.com/in/eduardo-granja-95273739a/"><img src="https://img.shields.io/badge/-LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
      </td>
      <td align="center">
        <a href="https://github.com/IanVRV">
          <img src="https://github.com/IanVRV.png" width="100px;" alt="Foto de Ian Victor"/>
        </a><br>
        <sub><b>Ian Victor</b></sub><br>
        <sub>Dev Team</sub><br>
        <a href="https://github.com/IanVRV"><img src="https://img.shields.io/badge/-GitHub-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub"/></a> <a href="https://www.linkedin.com/in/ian-victor-ribeiro-vieira-3147121ba/"><img src="https://img.shields.io/badge/-LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
      </td>
      <td align="center">
        <a href="https://github.com/mvlsouza">
          <img src="https://github.com/mvlsouza.png" width="100px;" alt="Foto de Marcus Vinicius"/>
        </a><br>
        <sub><b>Marcus Vinicius</b></sub><br>
        <sub>Dev Team</sub><br>
        <a href="https://github.com/mvlsouza"><img src="https://img.shields.io/badge/-GitHub-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub"/></a> <a href="https://www.linkedin.com/in/mvlsouza/"><img src="https://img.shields.io/badge/-LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
      </td>
    </tr>
  </table>
  <table>
    <tr>
      <td align="center">
        <a href="https://github.com/leandrotc013-lab">
          <img src="https://github.com/leandrotc013-lab.png" width="100px;" alt="Foto de Leandro Silva"/>
        </a><br>
        <sub><b>Leandro Silva</b></sub><br>
        <sub>Dev Team</sub><br>
        <a href="https://github.com/leandrotc013-lab"><img src="https://img.shields.io/badge/-GitHub-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub"/></a> <a href="https://www.linkedin.com/in/leandro-silva-a54ab4a2/"><img src="https://img.shields.io/badge/-LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
      </td>
      <td align="center">
        <a href="https://github.com/ag0ulart-dev">
          <img src="https://github.com/ag0ulart-dev.png" width="100px;" alt="Foto de Adham Goulart"/>
        </a><br>
        <sub><b>Adham Goulart</b></sub><br>
        <sub>Dev Team</sub><br>
        <a href="https://github.com/ag0ulart-dev"><img src="https://img.shields.io/badge/-GitHub-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub"/></a> <a href="https://www.linkedin.com/in/adham-goulart-4a7320394/"><img src="https://img.shields.io/badge/-LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
      </td>
      <td align="center">
        <a href="https://github.com/MATHEUSORTEGA">
          <img src="https://github.com/MATHEUSORTEGA.png" width="100px;" alt="Foto de Matheus Correia"/>
        </a><br>
        <sub><b>Matheus Correia</b></sub><br>
        <sub>Dev Team</sub><br>
        <a href="https://github.com/MATHEUSORTEGA"><img src="https://img.shields.io/badge/-GitHub-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub"/></a> <a href="https://www.linkedin.com/in/matheus-ortega-74049943b"><img src="https://img.shields.io/badge/-LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
      </td>
    </tr>
  </table>
</div>

---

# 🎓 Contexto acadêmico

A **MIA**, desenvolvida pela **McLorem Tecnologia**, faz parte da **Aprendizagem por Projetos Integrados (API)** do 1º semestre do curso de **Análise e Desenvolvimento de Sistemas da Fatec São José dos Campos**.

<br>

<div align="center">

### MIA - Assistente de Análise de Dados

**McLorem Tecnologia · Fatec São José dos Campos · 2026**

</div>