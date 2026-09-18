import sys
import os
import subprocess

if len(sys.argv) < 2:
    print("Uso correto: py add_lib.py <nome_da_biblioteca>")
    sys.exit(1)

lib_name = sys.argv[1]
venv_dir = os.path.join(os.getcwd(), ".venv")

if os.name == 'nt':
    venv_python = os.path.join(venv_dir, "Scripts", "python.exe")
else:
    venv_python = os.path.join(venv_dir, "bin", "python")

if not os.path.exists(venv_python):
    print("❌ Ambiente virtual não encontrado. Rode o seu main.py primeiro!")
    sys.exit(1)

print(f"⏳ Instalando '{lib_name}' no ambiente virtual...")
try:
    # Instala a biblioteca
    subprocess.run([venv_python, "-m", "pip", "install", lib_name], check=True)
    
    # Atualiza o requirements.txt com as versões exatas
    print("🔒 Salvando versão no requirements.txt...")
    with open("./requirements.txt", "w") as f:
        subprocess.run([venv_python, "-m", "pip", "freeze"], stdout=f, check=True)
        
    print(f"✅ Sucesso! '{lib_name}' instalada e pronta para uso.")
except subprocess.CalledProcessError:
    print(f"❌ Erro ao tentar instalar '{lib_name}'. Verifique se o nome está correto.")