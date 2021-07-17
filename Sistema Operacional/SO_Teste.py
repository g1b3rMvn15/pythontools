import platform
from datetime import datetime
import getpass

print("Nome Maquina.....", platform.node())
print("Arquitetura.....", platform.architecture())
print("Sistema Operacional.....", platform.system())
print("Versão do SO.....", platform.release())
print("Processador.....", platform.processor())
print("Versão do Python.....", platform.python_version())

print(datetime.now())

usuario = getpass.getuser()
senha = getpass.getpass("Digite sua Senha...")

if usuario == "gmuniz" and senha == "hello":
    print ("Bem vindo")
else:
    print("Voce não tem acesso")