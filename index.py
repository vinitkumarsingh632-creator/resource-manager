from PySide6.QtWidgets import QApplication,QWidget;
import sys;

app = QApplication(sys.argv)
window = QWidget()
window.resize(1000,500)
sidebar = QWidget(window)
sidebar.resize(200,500)
window.show()
app.exec()
