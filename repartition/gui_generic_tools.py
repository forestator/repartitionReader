from PySide2 import QtCore
from PySide2.QtWidgets import QWidget, QHBoxLayout, QLabel


class SwitchContainer(QWidget):
    def __init__(self, widget1, widget2):
        super().__init__()

        self.visible = 1

        self.widget1 = widget1
        self.widget2 = widget2

        self.layout = QHBoxLayout()
        self.layout.addWidget(widget1)
        self.layout.addWidget(widget2)
        self.setLayout(self.layout)

        self.widget2.hide()

    def switch(self):
        if self.visible == 1:
            self.widget1.hide()
            self.widget2.show()
            self.visible = 2
        else:
            self.widget2.hide()
            self.widget1.show()
            self.visible = 1


class LeftAlignLabel(QLabel):
    def __init__(self, name):
        super().__init__(name)
        self.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)

class RightAlignLabel(QLabel):
    def __init__(self, name):
        super().__init__(name)
        self.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

class MeasurementLabel(QLabel):
    def __init__(self, title):
        super().__init__()
        self.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.title = title
        self.setText("")

    def setText(self, value=None):
        if value is None:
            value = ""
        tt = f"{self.title}: {value}"
        super().setText(tt)


class LeftAlignTitleLabel(QLabel):
    def __init__(self, name):
        super().__init__(name)
        font = self.font()
        font.setPointSize(12)
        font.setBold(True)
        self.setFont(font)
        self.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)


class LeftAlignSubTitleLabel(QLabel):
    def __init__(self, name):
        super().__init__(name)
        font = self.font()
        font.setPointSize(12)
        self.setFont(font)
        self.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
