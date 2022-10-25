import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
                             QVBoxLayout, QApplication)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self) # valueChanged라는 이벤트로 인해 값이 변하는 객체
        sld = QSlider(Qt.Horizontal, self) # signal을 보내는 송신 객체

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        lcd.display(16)
        sld.valueChanged.connect(lcd.display) # valueChanged라는 값이 변하는 신호를 받고, display라는 이벤트 핸들러, 즉 Slot과 연결하는 코드이다

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Signal and slot')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
