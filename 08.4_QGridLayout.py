import sys
from PyQt5.QtWidgets import *

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

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
            grid.addWidget(button, *position)

        self.move(300, 150)
        self.setWindowTitle("Calculator")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Example()
    # w.show() # 자동으로 show가 되는 듯...?
    sys.exit(app.exec_())