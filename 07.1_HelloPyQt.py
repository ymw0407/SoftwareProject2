import sys
from PyQt5.QtWidgets import *

# label = QLabel("test") // QLabel을 QApplication 전에 실행시키면 에러가 뜨게 된다!!!
print(sys.argv) # 파이썬을 실행할때 사용된 argument, 즉 인자 값을 가져온다. 만약 "python 07_HelloPyQt.py 123"으로 실행시켰다면 ["07_HelloPyQt.py", "123"]을 리턴하게 된다.
app = QApplication(sys.argv) # QApplication으로 클래스에 대한 인스턴스를 생성하여 app이라는 변수로 바인딩한다. 생성자로 sys.argv 값을 필요로 한다.
label = QLabel("Hello PyQt") # QLabel 클래스에 대한 인스턴스를 만들고 해당 인스턴스를 show()하여 화면에 QLabel 위젯을 출력한다.
label.show() # label show가 하나도 없다면 보여줄게 없다고 판단하여 화면을 아무것도 안띄어주는 것 같다.
print("test")
app.exec_() # exec_()를 통해서 프로그램은 이벤트 루프(무한 반복하면서 이벤트를 처리하는 상태)에 진입함 // 이벤트 루프는 무한 루프 구조를 띄고 있다.
# label.show() // 이 녀석은 여기 있어도 에러가 나지 않는다. 아무 영향을 미치지 못할뿐
print("end") # 위에서 실행된 이벤트 루프에 의하여, 창이 닫힌 뒤에 터미널에 프린트 됨을 확인할 수 있음