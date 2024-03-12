from cpf_generator import generateCPF
from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QGridLayout, QLayout, QLineEdit, QLabel,
                               QPushButton)
from variables import (MINIMUM_WIDTH, MINIMUM_HEIGHT, FONT_SIZE, PRIMARY_TEXT_SIZE, SECONDARY_TEXT_SIZE, BUTTON_WIDTH, 
                       BUTTON_HEIGHT, OP_BUTTON_WIDTH, OP_BUTTON_HEIGHT)

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
        
    def addLayoutToVLayout(self, layout: QLayout):
        self.vLayout.addLayout(layout)

class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()
        
    def configStyle(self):
        self.setMinimumSize(BUTTON_WIDTH, BUTTON_HEIGHT)
        self.setStyleSheet(f'font-size: {PRIMARY_TEXT_SIZE}px')
        
class OptionButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()
        
    def configStyle(self):
        self.setCheckable(True)
        self.setFixedSize(OP_BUTTON_WIDTH, OP_BUTTON_HEIGHT) 
        
class TextLine(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setReadOnly(True)
        self.configStyle()
        
    def configStyle(self):
        # Size
        self.setMinimumSize(MINIMUM_WIDTH, FONT_SIZE * 1.5)
        self.setStyleSheet(f'font-size: {SECONDARY_TEXT_SIZE}px')
        # Alignment
        self.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        

class GenerateCpfGrid(QGridLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._makeGrid()
    
    def _makeGrid(self):
        
        self.setVerticalSpacing(10)
        
        # Text 1
        genenereCpfText = QLabel('CPF Gerado:')
        genenereCpfText.setStyleSheet(f'font-size: {SECONDARY_TEXT_SIZE}px')
        self.addWidget(genenereCpfText, 0, 0)

        # Response
        self.generateCpfLine = TextLine()
        self.addWidget(self.generateCpfLine, 1, 0, 1, 4)
        
        # Option: Punctuation
        self.punctuationButton = OptionButton()
        self.addWidget(self.punctuationButton, 2, 1)
        
        # Text 2
        punctuationText = QLabel('Pontuação')
        punctuationText.setStyleSheet(f'font-size: {SECONDARY_TEXT_SIZE}px')
        punctuationText.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.addWidget(punctuationText, 2, 2)
        
        # Action Button
        genenereCpfButton = Button('GERAR CPF')
        self.addWidget(genenereCpfButton, 3, 1, 1, 2)
        self._connectButtonClicked(genenereCpfButton, self._makeSlot(self._generateCPF, self.punctuationButton))
        
    def _connectButtonClicked(self, button, slot):
        button.clicked.connect(slot)
        
    def _makeSlot(self, func, *args, **kwargs):
        @Slot()
        def slot():
            func(*args, **kwargs)
        return slot
    
    def _generateCPF(self, optionButton: OptionButton):
        
        punctuation = False
        if optionButton.isChecked():
            punctuation = True
            
        generated_cpf = generateCPF(punctuation)
        self.generateCpfLine.setText(generated_cpf)
