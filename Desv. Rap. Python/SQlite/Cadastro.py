import sqlite3 as conector #conector abre uma conexao com o banco de dados.
conexao = conector.connect("Estacio26.db")
cursor  = conexao.cursor()
cursor.execute(''' CREATE TABLE IF NOT EXISTS aluno ( 
    id_aluno INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome varchar(50),
    curso varchar(50)
    )''')
# cursor.execute("""INSERT INTO aluno(nome,curso)
# VALUES('LUCAS', 'ADS')""")

nomeAluno = input("Digite o nome do aluno:\n")
cursoAluno = input("Digite seu curso:\n")

cursor.execute("""INSERT INTO aluno (nome,curso)
               VALUES(?,?)""", (nomeAluno,cursoAluno))

cursor.execute("""  SELECT * FROM aluno""")
dados = cursor.fetchall()

for aluno in dados:
 print(aluno)



conexao.commit()
