import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class SimplePaintProgram(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Paint Program")
        self.setGeometry(0,0,360,220)
        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)

        self.clear_button = QPushButton("Clear", self)
        self.clear_button.setGeometry(10, 170, 340, 40)
        

        self.show()

def main():
    app = QApplication(sys.argv)
    
    w = SimplePaintProgram()
    w.show()

    return app.exec()

if __name__ == "__main__":
    sys.exit(main())