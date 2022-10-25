import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Event handler')
        self.show()

    def keyPressEvent(self, e): # 기존에 QWidget에는 KeyPressEvent라는 메소드가 존재 --> 따라서 해당 메소드를 override하여 사용한 것
        print(e.key()) # e.key()라는 메소드는 키보드의 입력을 아스키코드로 받아온다. 단, 대문자 알파벳으로... 65...
        #print(Qt.key_Escape) # 여기서 Qt.Key_Escape라는 필드는 키보드의 입력 중, ESC 키의 숫자를 리턴한다.
        if e.key() == Qt.Key_Escape: # 여기서 e는 이벤트를 캡슐화한 이벤트 객체
            self.close() # close라는 이미 QWidget을 통해 구현된, 윈도우를 닫는 메서드 호출

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
