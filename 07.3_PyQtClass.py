import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self): # 생성자
        super().__init__() # QMainWindow 상속
        self.setWindowTitle("SWP2") # 윈도우의 타이틀 창의 제목을 바꾸는 기능을 수행하는 메서드 // default 값은 해당 파일의 이름
        self.setGeometry(300, 300, 300, 400) # 1,2번 인자들은 각각 윈도우가 시작되는 픽셀 위치이고, 3, 4번 인자들은 윈도우의 가로 세로 픽셀의 크기이다.


if __name__ == "__main__":
    app = QApplication(sys.argv)
    print(dir(MyWindow)) # 기존에 QMainWindow에 있는 메소드들과 속성값들이 굉장히 굉장히 많음, 그것들을 상속 받아서 사용하게 됨
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()
