from PySide6.QtWidgets import QApplication,QWidget,QHBoxLayout,QVBoxLayout,QLabel,QProgressBar;
from PySide6.QtCore import Qt,Signal,QTimer
import sys;
import psutil;
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

rowLayout.addWidget(sidebar,1)
main = QHBoxLayout(window)
main.setObjectName('main')
rowLayout.addLayout(main,3)




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
portText = SideText('Ports')
resourceText.setObjectName('resourceText')

resourceText.setAlignment(Qt.AlignmentFlag.AlignCenter)
resourceText.setStyleSheet('font-size:30px;background-color:green')

portText.setAlignment(Qt.AlignmentFlag.AlignCenter)
sideContent.addWidget(resourceText)
portText.setObjectName('portText')

portText.setStyleSheet('font-size:30px;')
sideContent.addWidget(portText)
sideContent.addStretch()


# Resources
resourcePage = QWidget()
main.addWidget(resourcePage)
resourceContainer = QVBoxLayout(resourcePage)
ram_block = QHBoxLayout()
resourceContainer.setContentsMargins(0,30,0,0)
resourceContainer.addLayout(ram_block)
ram_ui = QProgressBar()
ram_text = QLabel('RAM')
ram_block.setContentsMargins(20,0,20,0)
resourceContainer.addStretch()
ram_text.setStyleSheet('''
 font-size:25px;
 font-weight:800;
 
''')
ram_block.setSpacing(5)
ram_block.addWidget(ram_text,1)
ram_block.addWidget(ram_ui,6)
ram_ui.setStyleSheet('''
 QProgressBar::chunk{
 background-color:red;
 }
 QProgressBar{
 color:black;
 border:none;
 background-color:white;
 text-align:center;
 font-size:20px;
 font-weight:500;
 }
''')
ram_ui.setRange(0,100)
ram_ui.setValue(50)
ram = psutil.virtual_memory().percent
cores = psutil.cpu_count
cpu_per_core = psutil.cpu_percent()
def resource():
    pass


# port

portPage = QWidget()
main.addWidget(portPage)
portPage.hide()

def resourceBg():
    global current;
    current = "resource"
    portPage.hide()
    resourcePage.show()
    resourceText.setStyleSheet('font-size:30px;background-color:green')
    portText.setStyleSheet('font-size:30px;background-color:none')

def portBg():
    global current
    current = "port"
    resourcePage.hide()
    portPage.show()
    portText.setStyleSheet('font-size:30px;background-color:green')
    resourceText.setStyleSheet('font-size:30px;background-color:none')

resourceText.clicked.connect(resourceBg)
portText.clicked.connect(portBg)
window.show()
app.exec()
