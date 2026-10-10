TOOLS_DISPONIVEIS = []

def dspy_tool(func):
    """Decorador: adiciona a função à lista de ferramentas do DSPy."""
    TOOLS_DISPONIVEIS.append(func)
    return func

# --- REGISTRO DE ARQUIVOS DE FERRAMENTAS ---
# O Python precisa ler esses arquivos uma única vez para ativar os decoradores.
# Estes imports DEVEM ficar no final do ficheiro para evitar erros de importação circular.
import ia.tools.produtos_tools
import ia.tools.producao_tool
# import ia.tools.vendas_tools
# import ia.tools.descartes_tools