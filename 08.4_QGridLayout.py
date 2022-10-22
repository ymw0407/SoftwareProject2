import sys
from PyQt5.QtWidgets import *

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout() # QGridLayout을 통해서 인스턴스를 생성한다.
        self.setLayout(grid) # setLayout을 통해서 grid를 응용 프로그램 창의 레이아웃으로 설정한다.

        names = ["Cls", "Back", "", "Close",
                 "7", "8", "9", "/",
                 "4", "5", "6", "*",
                 "1", "2", "3", "-",
                 "0", ".", "=", "+"]
        positions = [(i, j) for i in range(5) for j in range(4)]
        # print(positions)
        for position, name in zip(positions, names):
            if name == "":
                continue
            button = QPushButton(name)
            print(position)
            grid.addWidget(button, *position) # 데이터 Unpacking --> grid.addWidget(button, position[0], position[1]) 
            # button을 Grid 위치에 맞게 설정한다.
        self.move(300, 150)
        self.setWindowTitle("Calculator")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Example()
    # w.show() # 자동으로 show가 되는 듯...?
    sys.exit(app.exec_())