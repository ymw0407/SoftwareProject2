# import sys
# from PyQt5.QtWidgets import *

# app = QApplication(sys.argv)
# label = QLabel("test")
# label.show()
# app.exec_()
# print(sys.argv)

#------------------------------------

# import sys
# from PyQt5.QtWidgets import *

# class MyWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("title")
#         self.setGeometry(0, 0, 100, 200)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     w = MyWindow()
#     w.show()
#     app.exec_()

#------------------------------------

# class Parent:
#     house = "Korea"
#     def __init__(self):
#         self.money = 10000

# class Child1(Parent):
#     def __init__(self):
#         super().__init__()
        
# class Child2(Parent):
#     def __init__(self):
#         pass

# child1 = Child1()
# child2 = Child2()

# print(dir(child1)) # house와 money를 포함
# print(dir(child2)) # house만 포함

#------------------------------------

import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.InitUI()
    def InitUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        groupbox = QGroupBox("text")
        groupbox.setLayout(QVBoxLayout().addWidget(QLabel("123")))
        grid.addWidget(groupbox, 0, 0, 1, 1)

        self.move(0,0)
        self.setWindowTitle("title")
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    sys.exit(app.exec_())

#------------------------------------

#------------------------------------

#------------------------------------