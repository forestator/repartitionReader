from PySide2.QtWidgets import QApplication, QStyle
from repartition.gui import Main


if __name__ == '__main__':
    app = QApplication([])
    main = Main()
    app.exec_()
