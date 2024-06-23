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

        # test
        #
        # lbl4 = ctk.CTkLabel(self, fg_color='yellow', text='')
        # lbl4.grid(row=3, column=0, sticky='news', pady=10)
        self.unit_switch = UnitSwitch(self)
        self.result_label = ResultLabel(self)
        self.weight_frame = WeightFrame(self)
        self.height_frame = HeightFrame(self)


class UnitSwitch(ctk.CTkLabel):
    def __init__(self, parent, default_unit='metric'):
        super().__init__(master=parent,
                         text=default_unit,
                         text_color=DARK_GREEN,
                         fg_color='transparent',
                         width=0,
                         font=(FONT, SWITCH_FONT_SIZE, 'bold')
                         )
        self.bind('<Button-1>', self.change_unit)
        self.grid(row=0, column=0, sticky='ne')

    def change_unit(self, _):
        current_text = self.cget('text')
        new_text = 'imperial' if current_text == 'metric' else 'metric'
        self.configure(text=new_text)


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
    def __init__(self, parent):
        super().__init__(master=parent,
                         fg_color=WHITE
                         )
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
        self.weight_label = ctk.CTkLabel(self,
                                         text='65.0kg',
                                         font=(FONT, INPUT_FONT_SIZE)
                                         )
        self.weight_label.grid(row=0, column=2)


class HeightFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent,
                         fg_color=WHITE,
                         )
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
                                           fg_color=LIGHT_GRAY)
        self.height_slider.grid(row=0, column=0)

        self.height_label = ctk.CTkLabel(self,
                                         text='1.70m',
                                         font=(FONT, INPUT_FONT_SIZE),
                                         )
        self.height_label.grid(row=0, column=1)



app = App()
app.mainloop()
