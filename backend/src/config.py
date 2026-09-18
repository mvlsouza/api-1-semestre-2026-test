import os
import sys
import subprocess
import venv

def verificacao_ambiente():
    # Verifica se já estamos rodando dentro do .venv
    in_venv = sys.prefix != sys.base_prefix
    
    # Se já estivermos no .venv, a função encerra silenciosamente
    # e permite que o main.py continue e inicie o seu bot!
    if in_venv:
        return

    # Daqui para baixo, sabemos que rodaram 'py main.py' fora do .venv
    venv_dir = os.path.join(os.getcwd(), ".venv")
    req_file = "./requirements.txt"
    
    if os.name == 'nt':
        venv_python = os.path.join(venv_dir, "Scripts", "python.exe")
    else:
        venv_python = os.path.join(venv_dir, "bin", "python")
    
    # Se o .venv não existir, cria e faz a instalação inicial
    if not os.path.exists(venv_dir):
        print("⚠️ Criando ambiente virtual '.venv'...")
        venv.create(venv_dir, with_pip=True)
        
        if not os.path.exists(req_file):
            with open(req_file, "w") as f:
                f.write("pandas\nnumpy\n")

        print("⏳ Instalando bibliotecas iniciais...")
        subprocess.run([venv_python, "-m", "pip", "install", "--upgrade", "pip"], check=True)
        subprocess.run([venv_python, "-m", "pip", "install", "-r", req_file], check=True)
        
        with open(req_file, "w") as f:
            subprocess.run([venv_python, "-m", "pip", "freeze"], stdout=f, check=True)
        print("✅ Ambiente configurado!")

    # O TRUQUE MÁGICO: Re-executa o script usando o Python do .venv e encerra o processo atual
    try:
        sys.exit(subprocess.call([venv_python] + sys.argv))
    except KeyboardInterrupt:
        sys.exit(1)