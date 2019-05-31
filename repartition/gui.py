import json

from PySide2.QtCore import Slot, QEvent
from PySide2.QtWidgets import QMainWindow, QWidget, \
    QVBoxLayout, QComboBox, QTextBrowser

from repartition import gui_listener
from repartition.gui_generic_tools import LeftAlignTitleLabel


class Main(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Repartition Reader")
        main_widget = QWidget()
        self.layout = QVBoxLayout()
        self.logs_window = QTextBrowser()
        self.pcb = PCombo()

        self.layout.addWidget(LeftAlignTitleLabel("Select project :"))
        self.layout.addWidget(self.pcb)
        self.layout.addWidget(self.logs_window)

        main_widget.setLayout(self.layout)
        self.setCentralWidget(main_widget)
        self.show()

        # ENCULE DE TES GRANDS MORTS
        print(self.pcb.selected)

        # Je voudrais que quand ce pcb.selected change ça relance mon with en dessous pour changer
        # les valeurs qui sont affichées et prendre d'autres valeurs qui sont dans mon json

        with open('repartition.json') as json_file:
            data = json.load(json_file)
            for a in data['projects'][self.pcb.selected]:
                self.log_it('Icon: ' + a['icon'])
                self.log_it('Grab: ' + a['grab'])
                self.log_it('')

    @Slot(str)
    def log_it(self, message):
        self.logs_window.append(message)


class PCombo(QComboBox):

    def __init__(self):
        super().__init__()

        self.selected = 'timedisc'
        self.projets = ['timedisc', 'Atelier Web', '@omp/utils', '@omp/grille', 'admin-utilisateurs']
        self.addItems(self.projets)
        self.currentIndexChanged.connect(self.projet_change)

    def projet_change(self):
        self.selected = self.currentText()
