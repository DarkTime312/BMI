from settings import *
import customtkinter as ctk


class BmiApp(ctk.CTk):
    """
    Main application class for the BMI calculator.

    This class sets up the main window and manages the overall layout and widgets.
    """
    def __init__(self):
        """Initialize the BMI calculator application."""
        super().__init__(fg_color=GREEN)

        # Window settings
        self.title('')
        self.geometry('400x400')
        self.iconbitmap('empty.ico')
        self.resizable(False, False)
        self.configure(padx=10)

        self.grid_layout()  # setting the grid layout
        self.create_widgets()  # creates the widgets

    def grid_layout(self):
        """Set up the grid layout for the main window."""
        for i, weight in enumerate([1, 3, 1, 2, 2]):
            self.rowconfigure(i, weight=weight, uniform='a')
        self.columnconfigure(0, weight=1)

    def create_widgets(self):
        """Create and initialize all widgets for the application."""
        self.unit_switch = UnitSwitch(self)
        self.result_label = ResultLabel(self, self.unit_switch)
        self.weight_frame = WeightFrame(self, self.unit_switch, self.result_label)
        self.height_frame = HeightFrame(self, self.unit_switch, self.result_label)


class UnitSwitch(ctk.CTkLabel):
    """
    A label that acts as a button to switch between metric and imperial units.
    """
    def __init__(self, parent, default_unit='metric'):
        """
        Initialize the UnitSwitch.

        Args:
            parent: The parent widget.
            default_unit (str): The default unit system ('metric' or 'imperial').
        """
        super().__init__(master=parent,
                         text=default_unit,
                         text_color=DARK_GREEN,
                         fg_color='transparent',
                         font=(FONT, SWITCH_FONT_SIZE, 'bold')
                         )
        self.parent = parent

        self.grid(row=0, column=0, sticky='ne')  # placing the label on the grid
        # Binding the label to a function to get run when label is clicked.
        self.bind('<Button-1>', self.change_unit)

    def change_unit(self, _):
        """
        Change the unit system and update related widgets.
        """
        current_text = self.cget('text')  # gets the current unit as text
        # switching the unit
        new_text = 'imperial' if current_text == 'metric' else 'metric'
        self.configure(text=new_text)

        # Runs the unit conversion logic based on new unit
        if new_text == 'imperial':
            self.parent.weight_frame.convert_weight_unit(to='imperial')
        else:  # if switched to metric
            self.parent.weight_frame.convert_weight_unit(to='metric')
        # runs the logic to update the label
        self.update_labels()

    def update_labels(self):
        """Update labels for both height and weight frames."""
        self.parent.height_frame.update_height()
        self.parent.weight_frame.update_weight()


class ResultLabel(ctk.CTkLabel):
    """
    A label that displays the calculated BMI.
    """
    def __init__(self, parent, switch_object):
        """
        Initialize the ResultLabel.

        Args:
            parent: The parent widget.
            switch_object: The UnitSwitch object for reference.
        """
        super().__init__(master=parent,
                         text='22.49',
                         fg_color='transparent',
                         text_color='white',
                         font=(FONT, MAIN_TEXT_SIZE, 'bold')
                         )
        # Reference to other classes
        self.switch_object = switch_object
        self.parent = parent
        # Placing the Label on the screen
        self.grid(row=1, column=0, sticky='news')

    def calculate_bmi(self):
        """
        Calculate the BMI based on the current unit system.

        Returns:
            float: The calculated BMI rounded to two decimal places.
        """
        if self.switch_object.cget('text') == 'metric':
            # gets the weight as kg
            weight = self.parent.weight_frame.weight_in_kg_var.get()
            # gets the height in centimeter and convert it to meter
            height = self.parent.height_frame.slider_var.get() / 100
            return round(weight / (height ** 2), 2)  # rounded to 2 decimals

        else:  # if unit is imperial
            # gets the cumulated weight as pound
            weight = self.parent.weight_frame.pound.get() + (self.parent.weight_frame.oz.get() / 16)
            # converts the height from centimeters to inches.
            height = (self.parent.height_frame.slider_var.get() / 2.54)
            return round((weight * 703) / (height ** 2), 2)

    def update_result(self, *args):
        """Gets the BMI and updates the text inside the label."""
        result = self.calculate_bmi()
        self.configure(text=result)


class WeightFrame(ctk.CTkFrame):
    """
    A frame that contains the buttons to adjust the weight.
    """
    def __init__(self, parent, switch_object, result_label):
        super().__init__(master=parent,
                         fg_color=WHITE
                         )
        # Reference to other classes
        self.switch_object = switch_object
        self.result_label = result_label

        self.grid(row=3, column=0, sticky='news', pady=10)

        # setting the layout
        self.rowconfigure(0, weight=10)

        self.columnconfigure(0, weight=25, uniform='d')
        self.columnconfigure(1, weight=10, uniform='d')
        self.columnconfigure(2, weight=35, uniform='d')
        self.columnconfigure(3, weight=10, uniform='d')
        self.columnconfigure(4, weight=25, uniform='d')

        self.create_vars()  # creates the variables
        self.create_widgets()  # creates the widgets
        self.widgets_layout()  # places the widgets on the screen

    def create_vars(self):
        """
        Creates variables to store weight
        in metric and imperial units.
        """
        # A variable to store the weight as kg
        self.weight_in_kg_var = ctk.DoubleVar(value=65.1)
        # A variable to store the pound part of imperial unit
        self.pound = ctk.IntVar(value=143)
        # A variable to store the ounce part of imperial unit
        self.oz = ctk.IntVar(value=4)

        # Binding a function to each variable that will be run
        # every time the variable is changed
        self.weight_in_kg_var.trace('w', self.result_label.update_result)
        self.pound.trace('w', self.result_label.update_result)
        self.oz.trace('w', self.result_label.update_result)

    def create_widgets(self):
        """
        Creates all the widgets in the frame.
        """
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
                                                  command=lambda: self.big_adjustment(increment=False),

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
                                                    command=lambda: self.small_adjustment(increment=False)
                                                    )

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
                                                  command=lambda: self.big_adjustment(increment=True),
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
                                                    command=lambda: self.small_adjustment(increment=True),
                                                    )
        # The weight label
        self.weight_label = ctk.CTkLabel(self,
                                         text='65.0kg',
                                         font=(FONT, INPUT_FONT_SIZE)
                                         )

    def widgets_layout(self):
        """Adds the widget to the frame."""
        self.big_decrement_button.grid(row=0, column=0, padx=5, pady=5)
        self.small_decrement_button.grid(row=0, column=1, padx=5, pady=5)
        self.weight_label.grid(row=0, column=2)
        self.big_increment_button.grid(row=0, column=4, padx=5, pady=5)
        self.small_increment_button.grid(row=0, column=3, padx=5, pady=5)

    def big_adjustment(self, increment=True):
        """
        Increment or decrements the weight value in big steps.
        """
        # Decides the operation as addition or subtraction based on increment parameter.
        adjustment = 1 if increment else -1
        # if the unit is metric and the current weight is above zero
        if self.switch_object.cget('text') == 'metric' and (weight := self.weight_in_kg_var.get()) > 0:
            # adds or subtracts 1 kg
            self.weight_in_kg_var.set(round(weight, 1) + adjustment)
        else:  # if the unit is imperial
            if self.pound.get() > 0:
                # adds or subtract 1 pound
                self.pound.set(value=(self.pound.get() + adjustment))
        # updates the label
        self.update_weight()

    def small_adjustment(self, increment=True):
        """
        Increment or decrements the weight value in small steps.
        """
        # Decides the operation as addition or subtraction based on increment parameter.
        adjustment = 0.1 if increment else -0.1
        if self.switch_object.cget('text') == 'metric' and (weight := self.weight_in_kg_var.get()) > 0:
            # adds or subtracts 100 grams
            self.weight_in_kg_var.set(round(weight, 1) + adjustment)
        else:  # imperial
            if increment:
                if self.oz.get() == 15:  # in case we're at maximum amount of ounce
                    self.oz.set(value=0)  # reset ounce to 0
                    self.pound.set(value=(self.pound.get() + 1))  # add one to pound
                else:  # otherwise add 1 to ounce
                    self.oz.set(value=(self.oz.get() + 1))
            else:  # decrement
                if self.oz.get() == 0:  # in case we're at minimum ounce
                    self.oz.set(value=15)  # start from top
                    self.pound.set(value=(self.pound.get() - 1))  # subtract one from pound
                else:  # otherwise subtract one from ounce
                    self.oz.set(self.oz.get() - 1)

        self.update_weight()

    def update_weight(self):
        """Updates the text showing the weight."""
        if self.switch_object.cget('text') == 'metric':
            self.weight_label.configure(text=f'{round(self.weight_in_kg_var.get(), 1)}kg')
        else:
            self.weight_label.configure(text=f'{self.pound.get()}lb {self.oz.get()}oz')

    def convert_weight_unit(self, to='imperial'):
        """
        Converts the weight between units.
        """
        if to == 'imperial':  # Converting metric to imperial
            weight_in_kg = self.weight_in_kg_var.get()
            weight_in_decimal_pound = weight_in_kg * 2.205

            # convert the decimal pound to pound + ounce format
            integer_part, decimal_part = divmod(weight_in_decimal_pound, 1)
            self.pound.set(value=int(integer_part))
            self.oz.set(value=int(decimal_part * 16))  # converts decimal pound to ounce
        else:
            # Converting imperial to metric
            total_weight_in_ounce = self.oz.get() + (self.pound.get() * 16)
            total_weight_in_kg = round(total_weight_in_ounce / 35.27, 1)
            self.weight_in_kg_var.set(total_weight_in_kg)  # update the variable


class HeightFrame(ctk.CTkFrame):
    def __init__(self, parent, switch_object, result_label):
        super().__init__(master=parent,
                         fg_color=WHITE,
                         )
        # Reference to other classes
        self.switch_object = switch_object
        self.result_label = result_label

        self.grid(row=4, column=0, sticky='news', pady=10)

        # set layout
        self.rowconfigure(0, weight=1)

        self.columnconfigure(0, weight=3, uniform='e')
        self.columnconfigure(1, weight=1, uniform='e')

        self.create_widgets()

    def create_widgets(self):
        self.slider_var = ctk.IntVar(value=170)
        self.slider_var.trace('w', self.result_label.update_result)

        self.height_slider = ctk.CTkSlider(self,
                                           width=240,
                                           progress_color=GREEN,
                                           button_color=GREEN,
                                           button_hover_color=GRAY,
                                           fg_color=LIGHT_GRAY,
                                           from_=100,  # 100 cm
                                           to=250,  # 250 cm
                                           variable=self.slider_var,
                                           command=self.update_height)
        self.height_slider.grid(row=0, column=0)

        self.height_label = ctk.CTkLabel(self,
                                         text='1.70m',
                                         font=(FONT, INPUT_FONT_SIZE),
                                         )
        self.height_label.grid(row=0, column=1)

    def update_height(self, value=None):
        """
        Updates the height shown on screen based on the selected amount with slider.
        """
        current_unit = self.switch_object.cget('text')
        if value is None:
            value = self.slider_var.get()
        if current_unit == 'metric':
            value = f'{value / 100:.2f}m'
        else:  # imperial
            cm_to_feet = value * 0.0328084
            feet, remainder = divmod(cm_to_feet, 1)
            inch = int(remainder * 12)
            value = f"{int(feet)}'{inch}''"
        self.height_label.configure(text=value)


# Running the app
app = BmiApp()
app.mainloop()
