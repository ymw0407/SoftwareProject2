import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)
label = QPushButton("Quit") # QLabel 대신, QPushButton을 사용하면 버튼으로 사용할 수 있다.
label.show()
app.exec_()