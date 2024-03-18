from cpf_generator import generateCPF
from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QGridLayout, QLayout, QLineEdit, QLabel,
                               QPushButton)
from variables import (MINIMUM_WIDTH, MINIMUM_HEIGHT, FONT_SIZE, PRIMARY_TEXT_SIZE, SECONDARY_TEXT_SIZE, BUTTON_WIDTH, 
                       BUTTON_HEIGHT, OP_BUTTON_WIDTH, OP_BUTTON_HEIGHT, PRIMARY_COLOR)

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Title
        self.setWindowTitle('Gerador e Validador de CPF')
        
        # Central Widget
        self.centralWid = QWidget()
        self.setCentralWidget(self.centralWid)
        
        # Layout
        self.vLayout = vLayout()
        self.centralWid.setLayout(self.vLayout)
        
        # Menu Bar
        self.menu = self.menuBar()
        self.menu.setStyleSheet(f'background: {PRIMARY_COLOR}')
        
        # Status Bar
        self.statusB = self.statusBar()
        self.statusB.setStyleSheet(f'background: {PRIMARY_COLOR}')
        
    def adjustWindowSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

class vLayout(QVBoxLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.setContentsMargins(20, 20, 20, 10)
        
        # Grid: Text + Text Line
        self.textResponse = TextTextLine()
        self.addLayout(self.textResponse)
        self.response = self.textResponse.generateCpfLine
        
        # Grid: Punctuations
        self.punctuationGrid = PunctuationGrid()
        self.addLayout(self.punctuationGrid)
        punctuationButton = self.punctuationGrid.punctuationButton
        
        # Action Button
        self.buttonGrid = ButtonGrid(punctuationButton, self.response)
        self.addLayout(self.buttonGrid)

class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()
        
    def configStyle(self):
        self.setFixedSize(BUTTON_WIDTH, BUTTON_HEIGHT)
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
        self.setTextMargins(5, 5, 5, 5)
        # Size
        self.setMinimumWidth(MINIMUM_WIDTH)
        self.setStyleSheet(f'font-size: {PRIMARY_TEXT_SIZE}px')
        # Alignment
        self.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        

class TextTextLine(QGridLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._makeGrid()
    
    def _makeGrid(self):
        
        self.setContentsMargins(0, 0, 0, 10)
        
        # Text 1
        genenereCpfText = QLabel('CPF Gerado:')
        genenereCpfText.setStyleSheet(f'font-size: {SECONDARY_TEXT_SIZE}px')
        self.addWidget(genenereCpfText, 0, 0)

        # Response
        self.generateCpfLine = TextLine()
        self.addWidget(self.generateCpfLine, 1, 0)
        
class PunctuationGrid(QGridLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._makeGrid()
    
    def _makeGrid(self):

        self.setContentsMargins(0, 0, 0, 10)
        
        # Option: Punctuation
        self.punctuationButton = OptionButton()
        self.addWidget(self.punctuationButton, 0, 0)
        
        # Text 2
        punctuationText = QLabel('Pontuação')
        punctuationText.setStyleSheet(f'font-size: {SECONDARY_TEXT_SIZE}px')
        self.addWidget(punctuationText, 0, 1)
        
        self.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
class ButtonGrid(QGridLayout):
    def __init__(self, button: QPushButton | None, response: TextLine | None):
        super().__init__()
        self._makeGrid(button, response)
    
    def _makeGrid(self, button, response):
        
        self.setContentsMargins(0, 0, 0, 30)
    
        self.response = response
        punctuationButton = button
        # Action Button
        self.genenereCpfButton = Button('GERAR CPF')
        self.addWidget(self.genenereCpfButton)
        self._connectButtonClicked(self.genenereCpfButton, self._makeSlot(self._generateCPF, punctuationButton, self.response))
        self.genenereCpfButton.setProperty('cssClass', 'actionButton')
    
    def _connectButtonClicked(self, button, slot):
        button.clicked.connect(slot)
        
    def _makeSlot(self, func, *args, **kwargs):
        @Slot()
        def slot():
            func(*args, **kwargs)
        return slot
    
    def _generateCPF(self, optionButton, response):
        
        punctuation = False
        if optionButton.isChecked():
            punctuation = True
            
        generated_cpf = generateCPF(punctuation)
        self.response.setText(generated_cpf)
        self.response.setFocus()
