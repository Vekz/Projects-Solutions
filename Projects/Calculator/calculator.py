import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QDesktopWidget,
                             QPushButton, QGridLayout, QLineEdit, QSizePolicy,
                             QMessageBox, QVBoxLayout)


class Calculator(QWidget):
    """Calculator window class"""
    def __init__(self):
        super().__init__()

        self.history = []
        self.haveCalculationBeenDone = False
        self.initUI()

    def initUI(self):
        """ Initialises GUI for the calculator """
        minHeight = 0.53*QDesktopWidget().availableGeometry().height()
        self.setMinimumHeight(minHeight)

        grid = QGridLayout()  # setuping the grid for the buttons and screen
        grid.setSpacing(1)
        grid.setContentsMargins(0, 0, 0, 0)

        ''' Setup of QLineEdit that is used as a screen for calculations and
        inputs in the calculator '''
        self.calcScreen = QLineEdit(self)
        self.calcScreen.setFrame(False)
        self.calcScreen.setReadOnly(True)
        font = self.calcScreen.font()
        font.setLetterSpacing(1, 2)
        font.setWeight(59)
        font.setPixelSize(27)
        self.calcScreen.setFont(font)
        self.calcScreen.setSizePolicy(QSizePolicy.Expanding,
                                      QSizePolicy.Expanding)
        grid.addWidget(self.calcScreen, 0, 0, 1, 5)

        ''' Initialisation of buttons, adding them to the grid and setuping of
        the signals for the buttons '''
        clrBtn = QPushButton("Clr", self)
        clrBtn.setShortcut("Ctrl+C")
        clrBtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        clrBtn.clicked.connect(self.calcScreen.clear)
        grid.addWidget(clrBtn, 1, 0, 1, 2)
        addBtn = QPushButton("+", self)
        addBtn.setShortcut("+")
        addBtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        addBtn.clicked.connect(lambda: self.changeText())
        grid.addWidget(addBtn, 1, 2, 1, 1)
        subBtn = QPushButton("-", self)
        subBtn.setShortcut("-")
        subBtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        subBtn.clicked.connect(lambda: self.changeText())
        grid.addWidget(subBtn, 1, 3, 1, 1)
        multBtn = QPushButton("*", self)
        multBtn.setShortcut("*")
        multBtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        multBtn.clicked.connect(lambda: self.changeText())
        grid.addWidget(multBtn, 1, 4, 1, 1)

        bckSpaceBtn = QPushButton("Backspace", self)
        bckSpaceBtn.setShortcut("Backspace")
        bckSpaceBtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        bckSpaceBtn.clicked.connect(lambda: self.calcScreen.backspace())
        grid.addWidget(bckSpaceBtn, 2, 0, 1, 1)
        SevBtn = QPushButton("7", self)
        SevBtn.setShortcut("7")
        SevBtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        SevBtn.clicked.connect(lambda: self.changeText())
        grid.addWidget(SevBtn, 2, 1, 1, 1)
        EigBtn = QPushButton("8", self)
        EigBtn.setShortcut("8")
        EigBtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        EigBtn.clicked.connect(lambda: self.changeText())
        grid.addWidget(EigBtn, 2, 2, 1, 1)
        NinBtn = QPushButton("9", self)
        NinBtn.setShortcut("9")
        NinBtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        NinBtn.clicked.connect(lambda: self.changeText())
        grid.addWidget(NinBtn, 2, 3, 1, 1)
        divBtn = QPushButton("/", self)
        divBtn.setShortcut("/")
        divBtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        divBtn.clicked.connect(lambda: self.changeText())
        grid.addWidget(divBtn, 2, 4, 1, 1)

        ParnthBtn = QPushButton("(", self)
        ParnthBtn.setShortcut("(")
        ParnthBtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        ParnthBtn.clicked.connect(lambda: self.changeText())
        grid.addWidget(ParnthBtn, 3, 0, 1, 1)
        FoBtn = QPushButton("4", self)
        FoBtn.setShortcut("4")
        FoBtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        FoBtn.clicked.connect(lambda: self.changeText())
        grid.addWidget(FoBtn, 3, 1, 1, 1)
        FivBtn = QPushButton("5", self)
        FivBtn.setShortcut("5")
        FivBtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        FivBtn.clicked.connect(lambda: self.changeText())
        grid.addWidget(FivBtn, 3, 2, 1, 1)
        SixBtn = QPushButton("6", self)
        SixBtn.setShortcut("6")
        SixBtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        SixBtn.clicked.connect(lambda: self.changeText())
        grid.addWidget(SixBtn, 3, 3, 1, 1)
        powBtn = QPushButton("**", self)
        powBtn.setShortcut("^")
        powBtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        powBtn.clicked.connect(lambda: self.changeText())
        grid.addWidget(powBtn, 3, 4, 1, 1)

        ClsdPrntBtn = QPushButton(")", self)
        ClsdPrntBtn.setShortcut(")")
        ClsdPrntBtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        ClsdPrntBtn.clicked.connect(lambda: self.changeText())
        grid.addWidget(ClsdPrntBtn, 4, 0, 1, 1)
        OnBtn = QPushButton("1", self)
        OnBtn.setShortcut("1")
        OnBtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        OnBtn.clicked.connect(lambda: self.changeText())
        grid.addWidget(OnBtn, 4, 1, 1, 1)
        TwBtn = QPushButton("2", self)
        TwBtn.setShortcut("2")
        TwBtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        TwBtn.clicked.connect(lambda: self.changeText())
        grid.addWidget(TwBtn, 4, 2, 1, 1)
        ThrBtn = QPushButton("3", self)
        ThrBtn.setShortcut("3")
        ThrBtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        ThrBtn.clicked.connect(lambda: self.changeText())
        grid.addWidget(ThrBtn, 4, 3, 1, 1)
        EqBtn = QPushButton("=", self)
        EqBtn.setShortcut("Enter")
        EqBtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        EqBtn.clicked.connect(lambda: self.calculate())
        grid.addWidget(EqBtn, 4, 4, 2, 1)

        HistBtn = QPushButton("Hist.", self)
        HistBtn.setShortcut("Ctrl+H")
        HistBtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        HistBtn.clicked.connect(lambda: self.showHistory(font))
        grid.addWidget(HistBtn, 5, 0, 1, 1)
        ZerBtn = QPushButton("0", self)
        ZerBtn.setShortcut("0")
        ZerBtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        ZerBtn.clicked.connect(lambda: self.changeText())
        grid.addWidget(ZerBtn, 5, 1, 1, 3)

        self.setLayout(grid)

        self.setWindowTitle("Calculator")
        self.show()

    def center(self):
        """ Finds center of the screen and moves main window there"""
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def changeText(self):
        """ Adds digit or symbol for calculation in to the QLineEdit widget """
        sender = self.sender()
        if not self.haveCalculationBeenDone:
            self.calcScreen.setText(self.calcScreen.text() + sender.text())
        else:
            self.calcScreen.clear()
            self.haveCalculationBeenDone = False
            lastCalculationResult = self.history[len(self.history)-1].result
            self.calcScreen.setText(str(lastCalculationResult)
                                    + self.calcScreen.text() + sender.text())

    def calculate(self):
        """ Takes string from QLineEdit widget and uses Calculation class to
        evaluate calculations, also grabs exceptions thrown by Calculation
        class """
        try:
            calc = Calculation(self.calcScreen.text())
            self.haveCalculationBeenDone = True
            self.history.append(calc)
            self.calcScreen.setText(calc.calc + "=" + str(calc.result))
        except ValueError:
            QMessageBox.question(self, "Message",
                                 "Check if your calculations don't"
                                 + " start and end with <b>'+ - / * **'</b> "
                                 + "or are there factors to every calculation",
                                 QMessageBox.Ok, QMessageBox.Ok)
        except ZeroDivisionError:
            QMessageBox.question(self, "Message",
                                 "Check if your calculations don't"
                                 + " include <b>division by ZERO</b>!",
                                 QMessageBox.Ok, QMessageBox.Ok)

    def showHistory(self, font):
        """ Shows the window with the previous calculations """
        pos = self.frameGeometry().topRight()
        self.History = History(self.history, font, pos)
        self.History.show()


class Calculation():
    """ Stores calculation, checks it validity and calculates it """
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


class History(QWidget):
    """ Previous calculation history window class """
    def __init__(self, history, font, pos):
        super().__init__()

        self.cornerPos = pos
        self.font = font
        self.history = history
        self.lineEdits = []
        self.initUI()

    def initUI(self):
        """ Initialises GUI for the history window """
        vertBox = QVBoxLayout()
        vertBox.setSpacing(1)
        vertBox.setContentsMargins(0, 0, 0, 0)

        pos = [i for i in range(len(self.history))]
        for calc, i in zip(self.history, pos):
            self.lineEdits.append(QLineEdit(self))
            self.lineEdits[i].setFrame(False)
            self.lineEdits[i].setReadOnly(True)
            self.lineEdits[i].setFont(self.font)
            self.lineEdits[i].setSizePolicy(QSizePolicy.Expanding,
                                            QSizePolicy.Expanding)
            self.lineEdits[i].setText(calc.calc + "=" + str(calc.result))
            vertBox.addWidget(self.lineEdits[i])

        self.setLayout(vertBox)
        self.setWindowTitle("Calculations history")
        self.move(self.cornerPos)
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)

    cal = Calculator()

    sys.exit(app.exec_())
