from typing import Literal

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

    def update_unit_view(self, unit):
        self.ui.btn_unit.setText(unit)

    def get_unit(self) -> str:
        return self.ui.btn_unit.text()

    def update_height_text(self, height: str):
        """
        Updates the height shown on screen based on the selected amount with slider.
        """
        self.ui.lbl_height.setText(height)

    def update_weight_label(self, weight: str):
        self.ui.lbl_weight.setText(weight)

    def update_bmi_text(self, bmi: str):
        """Gets the BMI and updates the text inside the label."""
        self.ui.lbl_result.setText(bmi)
