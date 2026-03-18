with open ("teste.txt","w") as arquivo:
   arquivo.write("Boa noite principe")

arquivo = open("teste.txt")
print("o principe foi aberto com sucesso.")

arquivo = open("mateus.txt")
print("o principe foi aberto com sucesso.")

print("mateus.txt: o arquivo aberto é o mesmo aberto?", arquivo.name)
print("mateus.txt: qual o modo do arquivo?", arquivo.mode)
arquivo.close()
print("mateus.txt: o arquivo esta fechado?", arquivo.closed)


with open("mateus.txt", "a") as arquivo:
    arquivo.write("\nliga o PC cacete.")
    
    
with open("mateus.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
    print("READLINE")
    linha1 = arquivo.readline()
    linha2 = arquivo.readline()
    print(linha1)
    print(linha2)


