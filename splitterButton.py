
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5 import QtWidgets

class HoverButton(QtWidgets.QFrame):
    mouseHover = QtCore.pyqtSignal(bool)

    def __init__(self, parent=None):
        QtWidgets.QFrame.__init__(self, parent)
        self.setMouseTracking(True)

    def enterEvent(self, event):
        self.mouseHover.emit(False)

    def leaveEvent(self, event):
        self.mouseHover.emit(True)


class Window(QtWidgets.QWidget):
    def __init__(self):

        QtWidgets.QWidget.__init__(self)
        global splitter
        splitter = QtWidgets.QSplitter()
        handle = splitter.handle(1)
        style = "QSplitter::handle{background: rgb(53, 53, 53); width: 2px; height: 2px;}"
        splitter.setStyleSheet(style)
        splitter.setHandleWidth(5)
        label = QtWidgets.QFrame(self)
        label2 = QtWidgets.QFrame(self)
        style1 = """
                    background: rgb(70,70,70)
                """
        style2 = "background: rgb(53,53,53)"
        label.setStyleSheet(style1)
        label2.setStyleSheet(style1)
        # label.setFrameStyle(QtWidgets.QFrame.Panel)
        self.new = QtWidgets.QFrame(label)
        new = self.new
        new.setFixedSize(30,300)
        new2 = HoverButton(label)
        lay = QtWidgets.QHBoxLayout(label)
        lay.addWidget(new)
        lay.addWidget(new2)
        lay.setContentsMargins(0,0,0,0)

        splitter.addWidget(label2)
        splitter.addWidget(label)
        layout = QtWidgets.QStackedLayout(self)
        layout.addWidget(splitter)

        self.button = QtWidgets.QToolButton(new)
        self.button2 = QtWidgets.QToolButton(new)
        button = self.button
        button2 = self.button2
        button.move(-25,130)
        button2.move(-25,130)

        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        buttonstyle =  """

                            background-image: url(LeftArrow.png);
                            width: 40px;
                            height: 40px;
                            border-radius: 22px;
                            border-color: black;
                            border-style: outset;
                            border-width: 1px;

                            """

        buttonstyle2 =  """

                            background-image: url(RightArrow.png);
                            width: 40px;
                            height: 40px;
                            border-radius: 22px;
                            border-color: black;
                            border-style: outset;
                            border-width: 1px;

                            """

        button.setStyleSheet(buttonstyle)
        button2.setStyleSheet(buttonstyle2)
        button.setVisible(True)
        button2.setVisible(False)




        new2.mouseHover.connect(self.splittersize)
        splitter.splitterMoved.connect(self.splittermove)

        self.handleSplitterButton(False)

        button.clicked.connect(
            lambda: self.handleSplitterButton(True))

        button2.clicked.connect(
            lambda: self.handleSplitterButton(False))


    def splittermove(self):
        return self.splittersize(3)




    def splittersize(self, var):
        size = splitter.sizes()
        timer = QtCore.QTimer()
        if size[0] == 0:
            # self.anim()
            self.button.setVisible(False)
            self.button2.setVisible(True)

            # delay = self.delay()

            # self.button2.setVisible(True)
        else:
            if var != 3:
                self.button.setVisible(True)

                self.anim(var)
                self.button2.setVisible(False)
            else:
                self.button.setVisible(True)
                self.button2.setVisible(False)


            # if var == True:
            #     self.anim(var)
            #     self.button2.setVisible(False)
            # else:
            #     self.anim(var)
            #     self.button2.setVisible(False)
            # else:
            #     self.button.setVisible()
            #     self.button2.setVisible(False)
            #



    def handleSplitterButton(self, left=True):
        if left:
            size = splitter.sizes()
            if size[0]/size[1] < 0.25:
                splitter.setSizes([0, 1])
                self.splittersize(True)

            else:
                splitter.setSizes([8, 2])
                self.splittersize(3)
        else:
            splitter.setSizes([8, 2])
            self.splittersize(3)

    def anim(self, var):
        animation = QtCore.QPropertyAnimation(self)
        animation.setDuration(500)
        animation.setTargetObject(self.button)
        animation.setPropertyName(b"pos")
        animation.setEasingCurve(QtCore.QEasingCurve.Linear)
        if var == True:
            startval = QtCore.QPoint(-50, 130)
            endval = QtCore.QPoint(-25, 130)
        else:
            startval = QtCore.QPoint(-25, 130)
            endval = QtCore.QPoint(-50, 130)
        animation.setStartValue(startval)
        animation.setEndValue(endval)
        animation.start()



    def delay(self):
        self.button.setVisible(False)



if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.setGeometry(300, 200, 1000, 700)
    window.show()
    sys.exit(app.exec_())
