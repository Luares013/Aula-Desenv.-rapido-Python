import sqlite3 as conector
conexao = conector.connect("Estacio26.db")
cursor = conexao.cursor()

while True:
    print("---------- Menu ----------")
    print("\n1 - Cadastrar Aluno")
    print("\n2 - Listar Alunos")
    print("\n3 - Sair")
    

    opcao = input("\nEscolha: \n")
    
    if opcao == "1":
     nomeAluno = input(" Digite o nome do aluno: \n")
     cursoAluno = input(" Digite o curso do aluno: \n")
     cursor.execute("""INSERT INTO aluno (nome,curso) 
     VALUES (?,?) """, (nomeAluno,cursoAluno))
     conexao.commit()
     
    elif opcao == "2":
        cursor.execute("SELECT * FROM aluno")
        dados = cursor.fetchall()
        for aluno in dados:
            print(aluno)
    
    elif opcao == "3":
        break
