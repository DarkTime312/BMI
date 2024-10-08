from functools import partial
from typing import Literal

from view import BmiView
from model import BmiModel


class BmiController:
    def __init__(self):
        super().__init__()

        self.view = BmiView()
        self.model = BmiModel()
        self.initial_setup()
        self.connect_signals_to_slots()

    def initial_setup(self):
        self.model.set_unit('metric')
        self.view.update_unit_view('metric')
        self.model.set_initial_weight(65)
        self.model.set_initial_height(170)
        self.view.ui.slider_height.setValue(170)
        self.view.update_height_text('1.70m')

    def connect_signals_to_slots(self):
        self.view.ui.btn_unit.clicked.connect(self.change_unit)
        self.view.ui.slider_height.valueChanged.connect(self.update_height)
        self.view.ui.btn_big_minus.clicked.connect(partial(self.adjust_weight,
                                                           is_increment=False,
                                                           big_step=True))
        self.view.ui.btn_big_plus.clicked.connect(partial(self.adjust_weight,
                                                          is_increment=True,
                                                          big_step=True))
        self.view.ui.btn_small_minus.clicked.connect(partial(self.adjust_weight,
                                                             is_increment=False,
                                                             big_step=False))
        self.view.ui.btn_small_plus.clicked.connect(partial(self.adjust_weight,
                                                            is_increment=True,
                                                            big_step=False))

    def change_unit(self):
        self.model.switch_unit()
        new_unit = self.model.get_unit()
        self.view.update_unit_view(new_unit)
        self.model.set_height(self.view.get_height())

        self.calculate_bmi()
        self.view.update_weight_label(self.model.weight.weight_str)
        self.view.update_height_text(self.model.height.height_str)

    def update_height(self, height: int):
        self.model.set_height(height)
        self.view.update_height_text(self.model.height.height_str)
        self.calculate_bmi()

    def adjust_weight(self, is_increment: bool, big_step: bool):
        self.model.adjust_weight(is_increment=is_increment,
                                 big_step=big_step)
        self.view.update_weight_label(self.model.get_weight().weight_str)
        self.calculate_bmi()

    def calculate_bmi(self):
        self.model.calculate_bmi()

        if self.model.get_unit() == 'metric':
            self.view.update_bmi_text(str(self.model.bmi_metric))
        else:
            self.view.update_bmi_text(str(self.model.bmi_imperial))
