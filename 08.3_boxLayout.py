import sys
from PyQt5.QtWidgets import *

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        okButton = QPushButton("OK")
        cancelButton = QPushButton("cancel")

        okButton1 = QPushButton("OK")
        cancelButton1 = QPushButton("cancel")

        hbox = QHBoxLayout() # 위젯을 가로로 정렬하는 기본 레이아웃 클래스
        hbox.addStretch(1) # 필요한 공간을 만들기 위해 스트레치 요소를 추가한다.
        hbox.addWidget(okButton)
        hbox.addStretch(2) # 필요한 공간을 stretch의 비율에 따라서 배정을 한다.
        hbox.addWidget(cancelButton)
        hbox.addStretch(1)

        hbox1 = QHBoxLayout() # 위젯을 가로로 정렬하는 기본 레이아웃 클래스
        hbox1.addStretch(1) # 필요한 공간을 만들기 위해 스트레치 요소를 추가한다.
        hbox1.addWidget(okButton1)
        hbox1.addStretch(2) # 필요한 공간을 stretch의 비율에 따라서 배정을 한다.
        hbox1.addWidget(cancelButton1)
        hbox1.addStretch(1)

        vbox = QVBoxLayout() # 위젯을 세로로 정렬하는 기본 레이아웃 클래스
        vbox.addStretch(1)
        vbox.addLayout(hbox) # 가로 상자 레이아웃은 세로 상자 레이아웃 안으로 배치된다.
        vbox.addStretch(1)
        vbox.addLayout(hbox1)
        vbox.addStretch(1)

        # hbox.addLayout(vbox)

        # 이러한 레이아웃을 생성하기 위해 하나의 수평 상자와 하나의 수직 상자를 사용한다.
        # 응용 프로그램 창 크기를 조정해도 박스 레이아웃 내의 위젯들은 해당 위치에 그대로 있다.

        self.setLayout(vbox) # setLayout을 통해 메인 레이아웃을 통해 설정한다
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Example()
    w.show()
    sys.exit(app.exec_())