from PySide6.QtWidgets import QApplication, QLabel
from widgets import MainWindow, TextTextLine
from styles import setupTheme

if __name__ == '__main__':
    
    app = QApplication()
    mainWindow = MainWindow()
    
    # Theme
    setupTheme()
    
    mainWindow.adjustWindowSize()
    mainWindow.show()
    app.exec()