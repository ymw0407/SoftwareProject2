import sys
from PyQt5.QtWidgets import *

class Review(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        
        grid.setSpacing(10) # 그리드 사이의 간격을 결정한다

        titleLabel = QLabel("Title", self)
        authorLabel = QLabel("Author", self)
        reviewLabel = QLabel("Review", self)

        grid.addWidget(titleLabel, 0, 0)
        grid.addWidget(authorLabel, 1, 0)
        grid.addWidget(reviewLabel, 2, 0)

        self.title = QLineEdit(self)
        self.author = QLineEdit(self)
        
        grid.addWidget(self.title, 0, 1, 1, 4)
        grid.addWidget(self.author, 1, 1, 1, 4)
        
        self.text = QTextEdit(self)

        grid.addWidget(self.text, 2, 1, 5, 4)

        btn = QPushButton("제출", self)
        btn.clicked.connect(self.submit)

        grid.addWidget(btn, 7, 4)

        self.move(300, 150)
        self.setWindowTitle("Review")
        self.show()

    def submit(self):
        print("title : " + self.title.text())
        print("author : " + self.author.text())
        print("text : " + self.text.toPlainText())

        self.title.setText("")
        self.author.setText("")
        self.text.setText("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Review()
    sys.exit(app.exec_())