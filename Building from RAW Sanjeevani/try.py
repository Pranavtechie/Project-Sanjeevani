from PyQt5 import QtWidgets,uic

app = QtWidgets.QApplication([])
dlg = uic.loadUi("test.ui")

dlg.lineEdit1.setPlaceholderText("anoop")
dlg.lineEdit2.setPlaceholderText("vs")

dlg.show()
app.exec()