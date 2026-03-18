linha = []

while True:
    texto = input("Digite textos ou digite a palavra 'sair'para encerrar:")
    if texto.lower()=="sair":
        break
    linha.append(texto)
    
print(linha)
