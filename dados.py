linha = []

while True:
    texto = input("Digite textos ou digite a palavra 'sair'para encerrar:")
    if texto.lower()=="sair":
        break
    linha.append(texto)
    
with open("meu_arquivos.txt", "w") as dados:
    for conteudos in linha:
        dados.write(conteudos + "\n")
        

with open("meu_arquivos.txt", "r") as dados:
    conteudo_linha = dados.read()
    print(conteudo_linha)