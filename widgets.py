from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel
from variables import MINIMUM_WIDTH, MINIMUM_HEIGHT, LOGO_FONT_SIZE

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Title
        self.setWindowTitle('Gerador e Validador de CPF')
        
        # Central Widget
        self.centralWid = QWidget()
        self.setCentralWidget(self.centralWid)
        
        # Layout
        self.vLayout = QVBoxLayout()
        self.centralWid.setLayout(self.vLayout)
        
        # Menu Bar
        self.menu = self.menuBar()
        
        # Status Bar
        self.statusB = self.statusBar()
        
    def adjustWindowSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())
        
    def addWidgetToVLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)
        
class Logo(QLabel):
    def __init__(self, text: str) -> None:
        super().__init__(text)
        self.configStyle()
        
    def configStyle(self):
        # Size
        self.setFixedSize(MINIMUM_WIDTH, MINIMUM_HEIGHT)
        
        # Alignment
        self.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        # Font
        font = self.font()
        font.setPixelSize(LOGO_FONT_SIZE)
        self.setFont(font)
        