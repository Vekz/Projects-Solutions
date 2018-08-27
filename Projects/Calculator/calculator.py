import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QDesktopWidget,
                             QPushButton, QGridLayout, QLineEdit, QSizePolicy)


class Calculator(QWidget):
    '''Calculator window class'''
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        minHeight = 0.53*QDesktopWidget().availableGeometry().height()
        self.setMinimumHeight(minHeight)

        grid = QGridLayout()
        grid.setSpacing(1)
        grid.setContentsMargins(0, 0, 0, 0)

        calcScreen = QLineEdit(self)
        calcScreen.setFrame(False)
        calcScreen.setReadOnly(True)
        font = calcScreen.font()
        font.setLetterSpacing(1, 2)
        font.setWeight(59)
        font.setPixelSize(27)
        calcScreen.setFont(font)
        calcScreen.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid.addWidget(calcScreen, 0, 0, 1, 5)

        clrBtn = QPushButton("Clr", self)
        clrBtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid.addWidget(clrBtn, 1, 0, 1, 2)
        addBtn = QPushButton("+", self)
        addBtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid.addWidget(addBtn, 1, 2, 1, 1)
        subBtn = QPushButton("-", self)
        subBtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid.addWidget(subBtn, 1, 3, 1, 1)
        multBtn = QPushButton("*", self)
        multBtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid.addWidget(multBtn, 1, 4, 1, 1)

        delBtn = QPushButton("Del", self)
        delBtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid.addWidget(delBtn, 2, 0, 3, 1)
        SevBtn = QPushButton("7", self)
        SevBtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid.addWidget(SevBtn, 2, 1, 1, 1)
        EigBtn = QPushButton("8", self)
        EigBtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid.addWidget(EigBtn, 2, 2, 1, 1)
        NinBtn = QPushButton("9", self)
        NinBtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid.addWidget(NinBtn, 2, 3, 1, 1)
        divBtn = QPushButton("/", self)
        divBtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid.addWidget(divBtn, 2, 4, 1, 1)

        FoBtn = QPushButton("4", self)
        FoBtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid.addWidget(FoBtn, 3, 1, 1, 1)
        FivBtn = QPushButton("5", self)
        FivBtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid.addWidget(FivBtn, 3, 2, 1, 1)
        SixBtn = QPushButton("6", self)
        SixBtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid.addWidget(SixBtn, 3, 3, 1, 1)
        powBtn = QPushButton("**", self)
        powBtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid.addWidget(powBtn, 3, 4, 1, 1)

        OnBtn = QPushButton("1", self)
        OnBtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid.addWidget(OnBtn, 4, 1, 1, 1)
        TwBtn = QPushButton("2", self)
        TwBtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid.addWidget(TwBtn, 4, 2, 1, 1)
        ThrBtn = QPushButton("3", self)
        ThrBtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid.addWidget(ThrBtn, 4, 3, 1, 1)
        EqBtn = QPushButton("=", self)
        EqBtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid.addWidget(EqBtn, 4, 4, 2, 1)

        HistBtn = QPushButton("Hist.", self)
        HistBtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid.addWidget(HistBtn, 5, 0, 1, 1)
        ZerBtn = QPushButton("0", self)
        ZerBtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid.addWidget(ZerBtn, 5, 1, 1, 3)

        self.setLayout(grid)

        self.setWindowTitle("Calculator")
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


class Calculation():
    '''Stores calculation, checks it validity and calculates it'''
    def __init__(self, calc):
        self.calc = calc
        self.result = self.calculate()

    def IsValid(self):
        last = self.calc[len(self.calc)-1]
        first = self.calc[0]
        if (last not in "+-=*/") and (first not in "+-=*/"):
            return True
        else:
            return False

    def calculate(self):
        if self.IsValid():
            return eval(self.calc)
        else:
            raise ValueError


if __name__ == '__main__':

    app = QApplication(sys.argv)

    cal = Calculator()

    sys.exit(app.exec_())
