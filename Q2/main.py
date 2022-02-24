import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class SimplePaintProgram(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Paint Program")
        self.setGeometry(0,0,360,220)

        self.show()

def main():
    app = QApplication(sys.argv)
    
    w = SimplePaintProgram()
    w.show()

    return app.exec()

if __name__ == "__main__":
    sys.exit(main())