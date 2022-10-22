# SoftwareProject2

## 07 - 사용자 인터페이스 1

### TUI(Text-based User Interface)
지금까지 Python을 이용해서 만든 모든 프로그램은 TUI 기반에서 동작<br>
한 마디로, 문자를 이용한 그래픽 사용자 인터페이스라고도 할 수 있다.

### GUI(Graphical User Interface)
버튼이나 윈도우와 같은 그래픽 요소를 통해 사용자와 컴퓨터 간의 인터페이스를 구현한 방식
<br>
파이썬 GUI 프로그래밍
- wxPython
- __PyQt__
- TkInter
<br><br>

### Tkinter vs PyQt vs wxPython
Tkinter
- 파이썬의 공식적인 패키지이기 때문에 추가로 패키지를 설치할 필요가 없음
- 간단하여 배우기 쉬움
- 인터페이스가 좀 구식이고 복잡한 프로그램을 개발하기에는 부족함

PyQt나 wxPython
- 위와 같은 이유로 PyQt나 wxPython을 많이 사용
- PyQt는 Qt(C++)라고 불리는 GUI 크로스 플랫폼 프레임워크(운영체제에 상관없이 같은 코드로 동작하는 프로그램 개발을 지원함)의 파이썬 바인딩이다.

<br><br>

## 07.1_HelloPyQt
TUI 프로그램들은 프로그램이 실행된 후 바로 종료되지만, GUI 프로그램들은 사용자가 윈도우를 닫기 전까지는 계속 실행되어야 한다. 따라서 이벤트 루프를 통해서 무한 루프를 돌려야 하며, 해당 상태에서 사용자에 의하여 발생한 이벤트를 처리하게 된다.

```python
import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)
label = QLabel("Quit")
label.show()
app.exec_()
```

## 07.3_PyQtClass
### Python과 OOP
- Python은 쉽게 접근할 수 있는 스크립팅 언어라는 점이 매력적이기 때문에 OOP까지 신경 쓸 필요는 없다. 하지만 필요에 따라 작은 모듀들을 개발함으로써 쉽게 소프트웨어를 생성할 수 있다.
- 공개 도메인에 존재하는 많은 라이브러리들이 OOP로 만들어져 있다.
- 프로그램의 규모가 커질수록 OOP로 얻을 수 있는 이득이 커진다.
- GUI는 대표적으로 OOP 기법을 이용하여 만들어진 라이브러리로, 이미 만들어진 클래스들을 활용하여 유연한 프로그래밍이 가능하다.
<br><br>
- 파이썬은 오버로딩이 안된다. 하지만 가변 인자를 사용할 수 있으며, 어떤 자료형태든 받을 수 있다. <br>
단, 연산자 오버로딩은 된다.(파이썬의 매직 메소드들을 이야기하는 것! ex) \_\_str__, \_\_add__, \_\_sub__)
<br><br>
- 각 클래스 모듈에 단위 테스트를  포함하는 것이 좋은 코딩 습관이다.

```python
if __name__ == "__main__":
    print("unit test")
```

## PyQt의 widget
- 유저 인터페이스를 구성하는 가장 기본적인 부품 역할.
- QGroupBox, QLabel, QTextEdit, QDateEdit, QTimeEdit, QLineEdit와 같은 다양한 위젯들이 사용됨
- 한 위젯은 다양한 위젯에 포함될 수 있고, PyQt에서는 다른 위젯에 포함되지 않은 최상위 위젯을 window라고 부름
- 위의 예제에서는 QMainWindow 클래스로 윈도우 창을 생성하였다.