# SoftwareProject2

## 02 - 코드 리뷰
- 코드 리뷰란 개발자가 작성한 코드를 다른 개발자가 정해진 방법을 통하여 검토하는 일
- 형태: 상급자 검토, 집단 검토, 동료 검토
- 종류: 코드 규칙 검사, 실패 검출, 워크 스루(work through)

### 좋은 코드란
- 의도된 기능을 올바르게 수행한다고 해서 좋은 코드가 아니다.
- 코드의 기능적 역할과 외관 모두 중요하다.

### 클린코드의 구성
planning -> analysis -> design -> implementation -> maintenance

### 코딩 규칙
같은 코드를 작성하고 유지보수하는 개발자들 사이에 규정된, 코드가 지켜야 할 규약
- 형태적 측면
    - 변수와 합수의 이름 붙이기
    - 띄어쓰기, 들여쓰기와 블록 구조 등
- 구조적 측면
    - 권장되는 논리적 구조(하나의 함수 내에 리턴 문장은 하나만)
    - 금지되는 논리적 구조(무한 루프 + 조건부 break)

### python 코딩 규칙
PEP8 - Sytle Guide for Python Code <br>
Google Python Sytle Guide

### github commit 순서
1. 파일 작성
2. git status
3. git add
4. git commit
5. git push

## 04 - 파일 입출력

### open

```python
file = open("파일명", "열기모드")
```
- 열기 모드
    - r: 읽기 모드(기본)
    - w: 쓰기 모드
    - a: 추가 모드
    ---
    - b: 이진 모드
    - t: 텍스트 모드(기본)
    ---
    - x: 열고자 하는 파일이 이미 존재하면 파일 개방에 실패
    - +: 파일을 읽을 수도 있고 쓸 수도 있도록 개방함(+)

### read

```python
with open("text.txt", "rt") as file:
    line1 = file.readline()
    line2 = file.readline()
    line3 = file.readline()
    line4 = file.readline()
    print(line1) # "1번 줄\n"
    print(line2) # "2번 줄\n"
    print(line3) # "3번 줄"
    print(line4) # ""

with open("text.txt", "rt") as file:
    lines = file.readlines()
    print(lines) # ["1번 줄\n", "2번 줄\n", "3번 줄"]
    
with open("text.txt", "rt") as file:
    allLines = file.read()
    print(allLines) # "1번 줄\n2번 줄\n3번 줄\n"

```

### dictionary

```python

dict = {"key1" : 1, "key2": 2, "key3": 3}
print(dict["key1"]) # 1

for k in dict.keys(): # ["key1", "key2", "key3"]
    print(k) 
for v in dict.values(): # [1, 2, 3]
    print(v)
for k, v in dict.items(): # [('key1', 1), ('key2', 2), ('key3', 3)]
    print(k, v)

dict.update("key4" : 4)
print(dict["key4"]) # 4

```
### file exceptions
- FileExistsError
    - 이미 존재하는 파일이나 디렉터리를 만들려고 할 때 발생한다.(errno EEXIST)
- FileNotFoundError
    - 파일이나 디렉터리가 요청되었지만 존재하지 않을 때 발생한다.(errno ENOENT)

### Pickle
- 다양한 데이터 타입이 혼재되어 있는 리스트, 튜플, 객체 등을 파일로 저장하고 싶을 때 사용
- 피클을 사용하면 저장된 파일을 원래 데이터 타입으로 자동으로 변환이 가능함(open에서 eval을 사용하는 것과 유사하지만, 훨씬 안전하다)<br><br>

- 피클링(pickling): 객체를 파일로 저장
    - dump()를 통해 write
- 언피클링(unpickling): 파일로부터 읽어들인 내용을 객체로 변환
    - load()를 통해 read<br><br>

- pickle을 사용하면 DB 파일의 입출력이 단순화될 뿐만 아니라, 파일 크기가 감소한다

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
app.exec_() # exec와 같은 경우에는 파이썬의 키워드이기 때문에, exec_를 사용하게 된다. -> 이벤트 루프를 통해서 무한 루프를 돌려, 사용자가 창을 닫기 전까지 계속 실행되게 된다.
```

## 07.3_PyQtClass
### Python과 OOP
- Python은 쉽게 접근할 수 있는 스크립팅 언어라는 점이 매력적이기 때문에 OOP까지 신경 쓸 필요는 없다. 하지만 필요에 따라 작은 모듈들을 개발함으로써 쉽게 소프트웨어를 생성할 수 있다.
- 공개 도메인에 존재하는 많은 라이브러리들이 OOP로 만들어져 있다.
- 프로그램의 규모가 커질수록 OOP로 얻을 수 있는 이득이 커진다.
- GUI는 대표적으로 OOP 기법을 이용하여 만들어진 라이브러리로, 이미 만들어진 클래스들을 활용하여 유연한 프로그래밍이 가능하다.
<br><br>

- 파이썬은 오버로딩이 안된다. 하지만 가변 인자를 사용할 수 있으며, 어떤 자료형태든 받을 수 있다. <br>
단, 연산자 오버로딩은 된다.(파이썬의 매직 메소드들을 이야기하는 것! ex) \_\_str__, \_\_add__, \_\_sub__)
<br><br>

- 각 클래스 모듈에 단위 테스트를  포함하는 것이 좋은 코딩 습관이다.<br><br>

- 하위 클래스(Subclassing)을 통해서 상위 클래스위 속성과 메소드를 물려받지만, 하위클래스는 메소드를 새롭개 작성함으로써 그와는 다른 동작을 하도록 개성화할 수 있다.


```python
if __name__ == "__main__":
    print("unit test")
```

## PyQt의 widget
- 유저 인터페이스를 구성하는 가장 기본적인 부품 역할.
- QGroupBox, QLabel, QTextEdit, QDateEdit, QTimeEdit, QLineEdit와 같은 다양한 위젯들이 사용됨
- 한 위젯은 다양한 위젯에 포함될 수 있고, PyQt에서는 다른 위젯에 포함되지 않은 최상위 위젯을 window라고 부름
- 위의 예제에서는 QMainWindow 클래스(Qwidget보다 상위 클래스, 즉 위젯을 담고 있는 프레임이 QMainWindow)로 윈도우 창을 생성하였다.<br>
<a href="https://coding-kindergarten.tistory.com/171">참고 링크</a>
<br><br>

## 08.3_layout
### 절대 위치
- 각 위젯의 위치와 크기를 픽셀 단위로 지정한다.(move 메소드를 사용한다.)
- 창 크기를 조정하여도, 위치가 변하지 않는다.(반응형 x)
- 플랫폼에 따라 다르게 보일 수 있다.
- 응용 프로그램에서 글꼴을 변경하면, 레이아웃이 손상될 수 있다.
<br><br>
- 레이아웃을 변경하기로 결정하면, 레이아웃을 완전히 다시 만들어야 한다.
<br><br>

## Event
### 이벤트 소스
- 이벤트 소스는 상태가 변경되는 객체이다.
- 이벤트를 생성하는 역할을 한다.
- --> 이벤트를 작동시키는 것(버튼 클릭하기)

### 이벤트 객체
- 이벤트 객체는 이벤트 소스의 상태 변경을 캡슐화한다.

### 이벤트 타겟
- 이벤트 타겟은 통지 받기를 원하는 객체이다.
- 이벤트 소스 객체는 이벤트를 처리하는 작업을 이벤트 타겟에 위임한다.
- 이벤트가 값을 변화시키는 물체(labeltext 등등)<br>

Event object가 Signal을 보내면서 Sender가 되고, Event Target이 Signal을 받으면서 Receiver가 된다.

## Signals and Slots(신호와 슬롯)
- 이벤트를 신호라고 할 수 있으며 이벤트 핸들러 함수를 슬롯이라고 할 수 있다.
- 신호와 슬롯은 객체 간의 통신에 사용된다.
- 특정 이벤트가 발생할 때 신호가 방출된다.(이벤트와 신호는 같은 수준)
- 슬롯은 파이썬으로 호출 가능한 모든 것이다.(slot은 이벤트를 처리하는 이벤트 핸들러의 개념을 가지고 있다.)
- PyQt5에 신호가 방출되면 그 신호와 연결된 슬롯이 호출된다.

## 11 - 계산기 알고리즘 추가 구현
```python
n = xxx
result = ""
for value in sorted(romans.keys(), reverse=True):
    while n >= value:
        result += romans[value]
        n -= value
return result
```
