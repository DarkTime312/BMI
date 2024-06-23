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
        self.rowconfigure(0, weight=1, uniform='a')
        self.rowconfigure(1, weight=3, uniform='a')
        self.rowconfigure(2, weight=2, uniform='a')
        self.rowconfigure(3, weight=2, uniform='a')

        self.columnconfigure(0, weight=1, uniform='b')

        # test

        # lbl2 = ctk.CTkLabel(self, fg_color='blue', text='')
        # lbl2.grid(row=1, column=0, sticky='news', pady=5)
        #
        # lbl3 = ctk.CTkLabel(self, fg_color='brown', text='')
        # lbl3.grid(row=2, column=0, sticky='news', pady=5)
        #
        # lbl4 = ctk.CTkLabel(self, fg_color='yellow', text='')
        # lbl4.grid(row=3, column=0, sticky='news', pady=10)
        UnitSwitch(self).grid(row=0, column=0, sticky='ne', pady=5)


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

    def change_unit(self, _):
        current_text = self.cget('text')
        new_text = 'imperial' if current_text == 'metric' else 'metric'
        self.configure(text=new_text)


app = App()
app.mainloop()
