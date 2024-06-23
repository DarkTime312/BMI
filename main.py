from settings import *
import customtkinter as ctk


class App(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color=GREEN)

        # Window settings
        self.title('')
        self.geometry('400x400')
        self.iconbitmap('empty.ico')
        self.resizable(False, False)
        self.configure(padx=10)

        # window layout
        self.rowconfigure(0, weight=12, uniform='a')
        self.rowconfigure(1, weight=33, uniform='a')
        self.rowconfigure(2, weight=10, uniform='a')
        self.rowconfigure(3, weight=20, uniform='a')
        self.rowconfigure(4, weight=20, uniform='a')

        self.columnconfigure(0, weight=1)

        # creating widgets
        self.unit_switch = UnitSwitch(self)
        self.result_label = ResultLabel(self)
        self.weight_frame = WeightFrame(self, self.unit_switch)
        self.height_frame = HeightFrame(self, self.unit_switch)


class UnitSwitch(ctk.CTkLabel):
    def __init__(self, parent, default_unit='metric'):
        super().__init__(master=parent,
                         text=default_unit,
                         text_color=DARK_GREEN,
                         fg_color='transparent',
                         width=0,
                         font=(FONT, SWITCH_FONT_SIZE, 'bold')
                         )
        self.parent = parent
        self.bind('<Button-1>', self.change_unit)
        self.grid(row=0, column=0, sticky='ne')
        self.pound = 0
        self.oz = 0

    def change_unit(self, _):
        current_text = self.cget('text')
        new_text = 'imperial' if current_text == 'metric' else 'metric'
        self.configure(text=new_text)
        if new_text == 'imperial':
            self.parent.weight_frame.convert_weight_unit(to='imperial')
        else:
            self.parent.weight_frame.convert_weight_unit(to='metric')
        self.update_labels()

    def update_labels(self):
        # update height label
        self.parent.height_frame.update_height()
        self.parent.weight_frame.update_weight()


class ResultLabel(ctk.CTkLabel):
    def __init__(self, parent):
        super().__init__(master=parent,
                         text='22.49',
                         fg_color='transparent',
                         text_color='white',
                         font=(FONT, MAIN_TEXT_SIZE, 'bold')
                         )
        self.grid(row=1, column=0, sticky='news')


class WeightFrame(ctk.CTkFrame):
    def __init__(self, parent, switch_object):
        super().__init__(master=parent,
                         fg_color=WHITE
                         )
        self.switch_object = switch_object
        self.pound = 143
        self.oz = 4
        self.grid(row=3, column=0, sticky='news', pady=10)

        # setting the layout
        self.rowconfigure(0, weight=10)

        self.columnconfigure(0, weight=25, uniform='d')
        self.columnconfigure(1, weight=10, uniform='d')
        self.columnconfigure(2, weight=35, uniform='d')
        self.columnconfigure(3, weight=10, uniform='d')
        self.columnconfigure(4, weight=25, uniform='d')

        # create widgets
        self.create_widgets()

    def create_widgets(self):
        # Decrement buttons
        self.big_decrement_button = ctk.CTkButton(self,
                                                  text='-',
                                                  font=(FONT, INPUT_FONT_SIZE),
                                                  width=60,
                                                  height=50,
                                                  corner_radius=BUTTON_CORNER_RADIUS,
                                                  text_color=BLACK,
                                                  fg_color=LIGHT_GRAY,
                                                  hover_color=GRAY,
                                                  command=self.big_dec

                                                  )
        self.small_decrement_button = ctk.CTkButton(self,
                                                    text='-',
                                                    font=(FONT, INPUT_FONT_SIZE),
                                                    width=30,
                                                    height=40,
                                                    corner_radius=BUTTON_CORNER_RADIUS,
                                                    text_color=BLACK,
                                                    fg_color=LIGHT_GRAY,
                                                    hover_color=GRAY,
                                                    command=self.small_dec
                                                    )
        self.big_decrement_button.grid(row=0, column=0, padx=5, pady=5)
        self.small_decrement_button.grid(row=0, column=1, padx=5, pady=5)

        # Increment buttons
        self.big_increment_button = ctk.CTkButton(self,
                                                  text='+',
                                                  font=(FONT, INPUT_FONT_SIZE),
                                                  width=60,
                                                  height=50,
                                                  corner_radius=BUTTON_CORNER_RADIUS,
                                                  text_color=BLACK,
                                                  fg_color=LIGHT_GRAY,
                                                  hover_color=GRAY,

                                                  )
        self.small_increment_button = ctk.CTkButton(self,
                                                    text='+',
                                                    font=(FONT, INPUT_FONT_SIZE),
                                                    width=30,
                                                    height=40,
                                                    corner_radius=BUTTON_CORNER_RADIUS,
                                                    text_color=BLACK,
                                                    fg_color=LIGHT_GRAY,
                                                    hover_color=GRAY,
                                                    )
        self.big_increment_button.grid(row=0, column=4, padx=5, pady=5)
        self.small_increment_button.grid(row=0, column=3, padx=5, pady=5)

        # The weight label
        self.weight_var = ctk.DoubleVar(value=65.0)
        self.weight_label = ctk.CTkLabel(self,
                                         text='65.0kg',
                                         font=(FONT, INPUT_FONT_SIZE)
                                         )
        self.weight_label.grid(row=0, column=2)

    def big_dec(self):
        if self.switch_object.cget('text') == 'metric':
            self.weight_var.set(round(self.weight_var.get(), 1) - 1)
        else:
            if self.pound > 0:
                self.pound -= 1
        self.update_weight()

    def small_dec(self):
        if self.switch_object.cget('text') == 'metric':
            self.weight_var.set(round(self.weight_var.get(), 1) - 0.1)
        else:
            if self.oz == 0:
                self.oz = 15
                self.pound -= 1
            else:
                self.oz -= 1

        self.update_weight()


    def update_weight(self):
        if self.switch_object.cget('text') == 'metric':
            self.weight_label.configure(text=f'{round(self.weight_var.get(), 1)}kg')
        else:
            self.weight_label.configure(text=f'{self.pound}lb {self.oz}oz')

    def convert_weight_unit(self, to='imperial'):
        if to == 'imperial':
            weight_in_kg = round(self.weight_var.get(), 1)
            weight_in_pound = weight_in_kg * 2.205
            self.pound = int(weight_in_pound // 1)
            self.oz = int((weight_in_pound % 1) * 16)
        else:
            total_oz = self.oz + (self.pound * 16)
            total_kg = round(total_oz / 35.27, 1)
            self.weight_var.set(total_kg)




class HeightFrame(ctk.CTkFrame):
    def __init__(self, parent, switch_object):
        super().__init__(master=parent,
                         fg_color=WHITE,
                         )
        self.switch_object = switch_object
        self.grid(row=4, column=0, sticky='news', pady=10)

        # set layout
        self.rowconfigure(0, weight=1)

        self.columnconfigure(0, weight=30, uniform='e')
        self.columnconfigure(1, weight=10, uniform='e')

        self.create_widgets()

    def create_widgets(self):
        self.height_slider = ctk.CTkSlider(self,
                                           width=240,
                                           progress_color=GREEN,
                                           button_color=GREEN,
                                           button_hover_color=GRAY,
                                           fg_color=LIGHT_GRAY,
                                           from_=100,
                                           to=250,
                                           command=self.update_height)
        self.height_slider.grid(row=0, column=0)
        self.height_slider.set(170)

        self.height_label = ctk.CTkLabel(self,
                                         text='1.70m',
                                         font=(FONT, INPUT_FONT_SIZE),
                                         )
        self.height_label.grid(row=0, column=1)

    def update_height(self, value=None):
        current_unit = self.switch_object.cget('text')
        if value is None:
            value = self.height_slider.get()
        if current_unit == 'metric':
            value = f'{value / 100:.2f}m'
        else:
            cm_to_feet = value * 0.0328084
            feet, remainder = divmod(cm_to_feet, 1)
            inch = int(remainder * 12)
            value = f"{int(feet)}'{inch}''"
        self.height_label.configure(text=value)


app = App()
app.mainloop()
