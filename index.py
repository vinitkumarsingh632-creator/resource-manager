from PySide6.QtWidgets import QApplication,QWidget,QHBoxLayout,QVBoxLayout;
import sys;

app = QApplication(sys.argv)
window = QWidget()
window.setStyleSheet('''
 #sidebar{
 background-color:red;
 }
 #main{
 background-color:green;
 }
 #main:hover{
 cursor:grab;
 }
''')
rowLayout = QHBoxLayout(window)
rowLayout.setSpacing(0)
rowLayout.setContentsMargins(0,0,0,0)
window.resize(1000,500)
sidebar = QWidget(window)
sidebar.setObjectName('sidebar')
rowLayout.addWidget(sidebar,1)
main = QWidget(window)
main.setObjectName('main')
rowLayout.addWidget(main,3)
sideContent = QVBoxLayout(sidebar)

window.show()
app.exec()
