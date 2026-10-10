import dspy
from ia.tools import obter_ferramentas_por_categoria

class ClassificadorDeIntencao(dspy.Signature):
    """Você é um roteador lógico do sistema da MIA, a assistente virtual amigavel da produçao do supermercado.
    Sua ÚNICA função é categorizar a mensagem do usuário em rotas específicas.
    
    ROTAS VÁLIDAS:
    - SAUDACAO: Mensagens de oi, olá, tchau, bom dia, agradecimentos (obrigado, valeu), qual seu nome.
    - PRODUCAO: Assuntos sobre quantidade a produzir, metas, descartes e fabricação.
    - PRODUTOS: Assuntos sobre ingredientes, estoque de produtos, receitas ou categorias dos produtos.
    - VENDAS: Assuntos sobre lucros, preços, histórico de vendas e faturamento.
    - INVALIDO: Qualquer outro assunto que não se encaixe nas acima.
    """
    pergunta = dspy.InputField(desc="Mensagem do usuário.")
    categoria = dspy.OutputField(desc="Responda ESTRITAMENTE com 'SAUDACAO', 'PRODUCAO', 'PRODUTOS', 'VENDAS' ou 'INVALIDO'.")

class RespostaSocial(dspy.Signature):
    """Você é a MIA, a assistente virtual amigável da produçao do supermercado.
    Sua função é responder de forma rápida e natural a saudações, despedidas ou agradecimentos.
    
    REGRAS:
    1. Sempre assuma sua identidade como MIA.
    2. Seja curta, simpática e vá direto ao ponto.
    3. Se for um oi/olá, pergunte como pode ajudar na produção do supermercado hoje.
    """
    mensagem = dspy.InputField(desc="Mensagem do usuário (saudação, despedida ou agradecimento).")
    resposta = dspy.OutputField(desc="Sua resposta rápida como MIA.")

class FormatadorDeResposta(dspy.Signature):
    """Você é a MIA, assistente virtual focada na análise de produção do supermercado.
    
    REGRAS ABSOLUTAS:
    1. Responda SEMPRE em Português do Brasil.
    2. Responda APENAS com base no Dado Bruto fornecido.
    3. Se o Dado Bruto estiver vazio ou disser erro, informe que não encontrou a informação.
    4. Seja amigável e conversacional. Construa uma frase natural para apresentar os dados (ex: "Aqui estão os produtos disponíveis na padaria:"), mas É ESTRITAMENTE PROIBIDO iniciar o texto com palavras de saudação (como "Olá", "Oi", "Bom dia", "Tudo bem").
    5. OBRIGATÓRIO: Para criar listas, use EXCLUSIVAMENTE o caractere especial '•' (bullet). É ESTRITAMENTE PROIBIDO usar asteriscos (*) no início das linhas.
    6. RETENÇÃO DE DADOS: É estritamente proibido ocultar ou resumir números. Se o Dado Bruto contiver métricas extras (como vendas e descartes entre parênteses), você DEVE transcrever esses valores na resposta final. Exemplo de formato: "• [Produto]: [X] produzidos (Vendas: [Y], Descarte: [Z])".
    7. OBRIGATÓRIO: Preço deve retornar como R$ X,XX.
    """
    pergunta_original = dspy.InputField()
    dado_bruto = dspy.InputField(desc="Resultado numérico ou extração da ferramenta. Mantenha todas as métricas originais, sem resumir.")
    resposta_final = dspy.OutputField(desc="A resposta final estruturada e preenchida estritamente com base no dado bruto.")
    
agente_classificador = dspy.Predict(ClassificadorDeIntencao)
agente_social = dspy.Predict(RespostaSocial)
agente_comunicador = dspy.Predict(FormatadorDeResposta)

class TrabalhadorEspecialista(dspy.Module):
    def __init__(self, categoria: str):
        super().__init__()
        ferramentas_da_categoria = obter_ferramentas_por_categoria(categoria)
        
        nomes_ferramentas = [f.name for f in ferramentas_da_categoria]
        print(f"\n[DEBUG ROTEAMENTO] Categoria escolhida: {categoria}")
        print(f"[DEBUG ROTEAMENTO] Ferramentas ativas: {nomes_ferramentas}\n")
        
        self.agente_react = dspy.ReAct(
            "pergunta: str -> dado_bruto_da_ferramenta: str", 
            tools=ferramentas_da_categoria
        )
        
    def forward(self, pergunta):
        return self.agente_react(pergunta=pergunta)