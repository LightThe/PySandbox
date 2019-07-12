import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon

class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.setWindowTitle("Uma Janela")
        lbl = QLabel("agora tem texto")
        #self.resize(800, 600)  não funciona no i3 por motivos
        #self.setWindowIcon(QIcon("/static/logo.ico")) ainda nao tem
        
        
root = QApplication(sys.argv)
app = Window()
app.show()
sys.exit(root.exec_())
