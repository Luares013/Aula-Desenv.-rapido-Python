from PyQt5 import uic,QtWidgets
import pymysql.connections

banco = pymysql.connections.Connection(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "sistemacadastro"
)

def funcao_principal():
    nome = formulario.lineEdit.text()
    telefone = formulario.lineEdit_2.text()
    cidade = formulario.lineEdit_3.text()

    cursor = banco.cursor()
    sql = "INSERT INTO usuario(nome,telefone,cidade) VALUES (%s,%s,%s)"
    dados = (str(nome), str(telefone), str(cidade))
    cursor.execute(sql,dados)
    banco.commit()
    formulario.lineEdit.setText("")
    formulario.lineEdit_2.setText("")
    formulario.lineEdit_3.setText("")

def listarDados():
    mostrarDados.show()

    cursor = banco.cursor()

    sql = "SELECT * FROM usuario"
    cursor.execute(sql)
    dados_lidos = cursor.fetchall()

    mostrarDados.tableWidget.setRowCount(len(dados_lidos))
    mostrarDados.tableWidget.setColumnCount(4)

    for linha in range(0, len(dados_lidos)):
        for coluna in range(0, 4):
            mostrarDados.tableWidget.setItem(linha, coluna, QtWidgets.QTableWidgetItem(str(dados_lidos[linha][coluna])))

def excluirUsuario():
    linha = mostrarDados.tableWidget.currentRow()
    id_usuario = mostrarDados.tableWidget.item(linha,0).text()

    cursor = banco.cursor()
    sql = "DELETE FROM usuario WHERE id_usuario = %s"

    cursor.execute(sql, (id_usuario,))
    banco.commit()

    print("Usuário excluído com sucesso!")

    listarDados()

    cursor.execute(sql, (id_usuario,))

    
app = QtWidgets.QApplication([])

formulario = uic.loadUi("TelaDeCadastro.ui")
mostrarDados = uic.loadUi("listar.ui")

formulario.pushButton.clicked.connect(funcao_principal)
formulario.pushButton_2.clicked.connect(listarDados)

formulario.show()
app.exec()
