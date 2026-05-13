from PyQt5 import uic,QtWidgets
import pymysql.connections

banco = pymysql.connections.Connetion(
    host = "localhost:8080",
    user = "root",
    passwd = "",
    database = "sistemacadastro"
)

def funcao_pincipal():
    nome = formulario.lineEdit.text()
    telefone = formulario.lineEdit_2.text()
    cidade = formulario.lineEdit_3.text()

    cursor = banco.cursor()
    sql = "INSERT INTO usuario(nome,telefone.cidade) VALUES (%s,%s,%s)"
    dados = (str(nome), str(telefone), str(cidade))
    cursor.execute(sql,dados)
    banco.commit()

app = QtWidgets.QApplication([])
formulario = uic.loadUi("TelaDeCadastro.ui")

formulario.show()
app.exec()
formulario.pushButton.clicked.connect(funcao_principal)