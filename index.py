from PySide6.QtWidgets import QApplication,QWidget,QHBoxLayout,QVBoxLayout,QLabel;
from PySide6.QtCore import Qt,Signal
import sys;
current = 'resource'
app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('Resource Manager')
window.setStyleSheet('''
 #sidebar{
 background-color:#e66a4083;
 
 }
 #main{
 background-color:#d5e6408b;
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
sidebar.setStyleSheet('''
#resourceText:hover{
background-color:green;
opacity:0.3;
}
#portText:hover{
background-color:green;
}
''')
rowLayout.addWidget(sidebar,1)
main = QWidget(window)
main.setObjectName('main')
rowLayout.addWidget(main,3)




# Side Bar
sideContent = QVBoxLayout(sidebar)
sideContent.setContentsMargins(0,30,0,0)
sideContent.setSpacing(30)
class SideText (QLabel):
    def __init__(self,text):
        super().__init__(text)
        self.setStyleSheet('''
padding-left:20px;
''') 
    clicked = Signal()
    def enterEvent(self, event):
        self.setCursor(Qt.CursorShape.PointingHandCursor)
    def leaveEvent(self, event):
        self.unsetCursor()
     

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit()

        super().mousePressEvent(event)

resourceText = SideText('Resources')
resourceText.setObjectName('resourceText')
resourceText.setStyleSheet('font-size:30px;')
portText = SideText('Ports')
sideContent.addWidget(resourceText)
portText.setObjectName('portText')
portText.setStyleSheet('font-size:30px;')
sideContent.addWidget(portText)
sideContent.addStretch()


# Resources


window.show()
app.exec()
