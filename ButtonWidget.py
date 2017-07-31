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


class SplitterButton(QtWidgets.QWidget):
    def __init__(self, frame1=None, frame2=None, parent=None):

        QtWidgets.QWidget.__init__(self)
        if parent is None:
            parent = QtWidgets.QSplitter()
        # self.orientation = False
        # if orientation is None:
        #     orientation = True
        self.splitter = parent
        splitter = self.splitter
        # handle = splitter.handle(1)
        # splitterstyle = "QSplitter::handle{background: rgb(53, 53, 53); width: 2px; height: 2px;}"
        # splitter.setStyleSheet(splitterstyle)
        # splitter.setHandleWidth(5)
        if frame1 is None:
            frame1 = QtWidgets.QFrame(self)

        if frame2 is None:
            frame2 = QtWidgets.QFrame(self)
        label = QtWidgets.QFrame(frame1)
        label2 = QtWidgets.QFrame(frame2)

        self.frame2 = frame2

        # style1 = "background: rgb(70,70,70)"
        #
        # style2 = "background: rgb(53,53,53)"
        # label.setStyleSheet(style1)
        # label2.setStyleSheet(style1)

        new = QtWidgets.QFrame(label2)
        new.setFixedSize(30,300)
        new2 = HoverButton(label2)
        lay = QtWidgets.QHBoxLayout(label2)
        lay.addWidget(new2)
        lay.addWidget(new)
        lay.setContentsMargins(0,0,0,0)

        splitter.addWidget(label2)
        splitter.addWidget(label)
        # splitter.setCollapsible(frame2, True)
        layout = QtWidgets.QHBoxLayout(self)
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
        splitter = self.splitter
        size = splitter.sizes()
        timer = QtCore.QTimer()
        if size[0] == 0:

            self.button.setVisible(False)
            self.button2.setVisible(True)

        else:
            if var != 3:
                self.button.setVisible(True)

                self.anim(var)
                self.button2.setVisible(False)
            else:
                self.button.setVisible(True)
                self.button2.setVisible(False)





    def handleSplitterButton(self, left=True):
        splitter = self.splitter
        if left:
            # self.frame2.resize(0,0)
            size = splitter.sizes()
            # splitter.setSizes([0,1])

            if size[0]/size[1] < 0.25:
                splitter.setSizes([0, 1])
                self.splittersize(True)

            else:
                 splitter.setSizes([3.5, 6.5])
                 self.splittersize(3)
        #
        # if left:
        #     size = splitter.sizes()
        #     splitter.setSizes([0,1])
        #     self.splittersize(True)
        else:
            splitter.setSizes([3.5, 6.5])
            self.splittersize(3)
            # print(size)
            # print('expect 1,1')


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


if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = SplitterButton()
    window.setGeometry(300, 200, 1000, 700)
    window.show()
    sys.exit(app.exec_())
