from PySide6.QtWidgets import QWidget
from hPyT import *

from ui_ui import Ui_BMIView


class BmiView(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_BMIView()
        self.ui.setupUi(self)
        self.set_titlebar_color()

        self.setWindowTitle(' ')

    def set_titlebar_color(self):
        title_bar_color.set(self, '#50BFAB')  # sets the titlebar color to white
