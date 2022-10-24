import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication, QLabel, QComboBox, QTextEdit, QLineEdit)

class ScoreDB(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.showScoreDB()
        self.readScoreDB()


    def initUI(self):
        self.setWindowTitle('assignment 6')
        self.setGeometry(400, 400, 800, 300)

        self.name = QLabel("Name:")
        self.age = QLabel("Age:")
        self.score = QLabel("Score:")
        self.amount = QLabel("Amount:")
        self.key = QLabel("Key:")
        self.result = QLabel("Result:")

        self.showKeyCombo = QComboBox()
        self.showKeyCombo.addItem("Name")
        self.showKeyCombo.addItem("Age")
        self.showKeyCombo.addItem("Score")

        self.nameEdit = QLineEdit()
        self.ageEdit = QLineEdit()
        self.scoreEdit = QLineEdit()
        self.amountEdit = QLineEdit()

        self.Addbut = QPushButton("Add")
        self.Addbut.clicked.connect(self.buttonClicked)
        self.Delbut = QPushButton("Del")
        self.Delbut.clicked.connect(self.buttonClicked)
        self.Findbut = QPushButton("Find")
        self.Findbut.clicked.connect(self.buttonClicked)
        self.Incbut = QPushButton("Inc")
        self.Incbut.clicked.connect(self.buttonClicked)
        self.Showbut = QPushButton("Show")
        self.Showbut.clicked.connect(self.buttonClicked)

        self.showRes = QTextEdit()

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.name)
        hbox1.addWidget(self.nameEdit)
        hbox1.addWidget(self.age)
        hbox1.addWidget(self.ageEdit)
        hbox1.addWidget(self.score)
        hbox1.addWidget(self.scoreEdit)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(self.amount)
        hbox2.addWidget(self.amountEdit)
        hbox2.addWidget(self.key)
        hbox2.addWidget(self.showKeyCombo)

        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(self.Addbut)
        hbox3.addWidget(self.Delbut)
        hbox3.addWidget(self.Findbut)
        hbox3.addWidget(self.Incbut)
        hbox3.addWidget(self.Showbut)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addWidget(self.result)
        vbox.addWidget(self.showRes)
        self.setLayout(vbox)

        self.show()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb = pickle.load(fH)
        except:
            pass
        fH.close()

    def closeEvent(self, event):
        self.writeScoreDB()

    def showScoreDB(self):
        keyname = str(self.showKeyCombo.currentText())
        msg = ""
        keyname = "Name" if not keyname else keyname

        for p in sorted(self.scoredb, key=lambda person: person[keyname] if keyname == "Name" else int(person[keyname])):
            for attr in sorted(p):
                msg += attr + "=" + str(p[attr]) + "     \t"
            msg += "\n"
        self.showRes.setText(msg)

    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def buttonClicked(self):
        sender = self.sender()
        choice = sender.text()

        name = self.nameEdit.text()
        age = self.ageEdit.text()
        amount = self.amountEdit.text()
        score = self.scoreEdit.text()


        if choice == "Add":
            info = dict()
            info["Name"] = name
            info["Age"] = int(age)
            info["Score"] = int(score)
            self.scoredb.append(info)
            self.showRes.clear()
            self.showScoreDB()
        elif choice == "Find":
            msg = ""
            for p in filter(lambda person: person['Name'] == name, self.scoredb):
                for attr in sorted(p):
                    msg += attr + "=" + str(p[attr]) + "     \t"
                msg += "\n"
            self.showRes.clear()
            self.showRes.setText(msg)
        elif choice == "Del":
            cnt = list(p['Name'] for p in self.scoredb).count(name)
            for i in range(cnt):
                for p in self.scoredb:
                    if p['Name'] == name:
                        self.scoredb.remove(p)
                        break
            self.showRes.clear()
            self.showScoreDB()
        elif choice == "Show":
            self.showRes.clear()
            self.showScoreDB()
        elif choice == "Inc":
            for p in filter(lambda person: person['Name'] == name, self.scoredb):
                p['Score'] += int(amount)
            self.showRes.clear()
            self.showScoreDB()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())