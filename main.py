from PySide6.QtWidgets import QApplication, QLabel
from widgets import MainWindow, Logo

if __name__ == '__main__':
    
    app = QApplication()
    mainWindow = MainWindow()
    
    # Text
    cpfLogo = Logo('GERADOR E VALIDADOR\n DE CPF')
    mainWindow.addWidgetToVLayout(cpfLogo)
    
    mainWindow.adjustWindowSize()
    mainWindow.show()
    app.exec()