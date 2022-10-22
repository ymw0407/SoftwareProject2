import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(100, 550) # 사이즈 결정
    w.move(100, 900) # 위치 결정
    w.setWindowTitle("Simple1")
    w.show()

    sys.exit(app.exec_()) # app 객체를 실행시키고, system의 x버튼을 누르면 실행되고 있는 App을 종료시킨다. / sys.exit()은 깨끗한 종료를 보장한다. / 응용 프로그램이 어떻게 종료되었는지를 알리기 위해 sys.exit()을 사용한다. exec는 파이썬의 키워드이기 때문에 이를 피하기 위해 exec_를 사용한다