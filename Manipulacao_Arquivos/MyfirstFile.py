arquivo = open("primeiro_arquivo.txt", "a")

arquivo.write("Meu primeiro arquivo")

arquivo.close()

with open("primeiro_arquivo.txt", "a") as arquivo:
    arquivo.write("\nHakuna matata!!")