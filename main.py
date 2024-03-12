from PySide6.QtWidgets import QApplication, QLabel
from widgets import MainWindow, GenerateCpfGrid

if __name__ == '__main__':
    
    app = QApplication()
    mainWindow = MainWindow()
    
    # Grid
    generateCpfGrid = GenerateCpfGrid()
    mainWindow.addLayoutToVLayout(generateCpfGrid)
    
    mainWindow.adjustWindowSize()
    mainWindow.show()
    app.exec()