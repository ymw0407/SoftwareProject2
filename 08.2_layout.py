import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        lbl1 = QLabel("Zetcode", self)
        lbl1.move(15, 10) # move를 통해 정확한 픽셀의 위치를 지정해주어 사용

        lbl2 = QLabel("tutorials", self)
        lbl2.move(35, 40)

        lbl3 = QLabel("for programmers", self)
        lbl3.move(55, 70)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("Absolute")
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Example()
    w.show()
    sys.exit(app.exec_())