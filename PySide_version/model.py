class Height:
    def __init__(self, height_cm, height_str):
        self.height_cm: int = height_cm
        self.height_str: str = height_str


class Weight:
    def __init__(self, weight_kg, weight_pd, weight_oz, weight_str):
        self.weight_kg: float = weight_kg
        self.weight_pd: int = weight_pd
        self.weight_oz: int = weight_oz
        self.weight_str: str = weight_str


class BmiModel:
    def __init__(self):
        super().__init__()
        self.height: Height | None = None
        self.weight: Weight | None = None
        self.unit: str | None = None

    def switch_unit(self):
        current_unit = self.get_unit()  # gets the current unit as text
        new_unit = 'imperial' if current_unit == 'metric' else 'metric'
        self.set_unit(new_unit)

    def set_height(self, height: int):

        current_unit: str = self.get_unit()
        # if value is None:
        #     value = self.slider_var.get()
        if current_unit == 'metric':
            value = f'{height / 100:.2f}m'
        else:  # imperial
            feet, inch = divmod(height / 2.54, 12)
            value = f"{int(feet)}'{int(inch)}''"
        self.height = Height(height, value)

    def set_unit(self, unit: str):
        self.unit = unit

    def get_unit(self):
        return self.unit

    def get_height(self):
        return self.height

    def set_initial_weight(self, weight_in_kg):
        self.weight = Weight(weight_kg=weight_in_kg,
                             weight_pd=143,
                             weight_oz=8,
                             weight_str="65.0kg")

    def update_weight(self, kg=None, pound=None, ounce=None, weight_str=None):
        if kg:
            self.weight.weight_kg = kg
        if pound:
            self.weight.weight_pd = pound
        if ounce:
            self.weight.weight_oz = ounce
        if weight_str:
            self.weight.weight_str = weight_str

        if self.get_unit() == 'metric':
            self.weight.weight_str = f'{round(self.weight.weight_kg, 1)}kg'
        else:
            self.weight.weight_str = f'{self.weight.weight_pd}lb {self.weight.weight_oz}oz'

    def get_weight(self):
        return self.weight

    def adjust_weight(self, is_increment: bool, big_step: bool):
        """
        Increment or decrements the weight value in big steps.
        """
        current_unit = self.get_unit()
        current_weight = self.get_weight()

        if big_step:
            # Decides the operation as addition or subtraction based on increment parameter.
            adjustment = 1 if is_increment else -1
            # if the unit is metric and the current weight is above zero
            if current_unit == 'metric' and (weight := current_weight.weight_kg) > 0:
                # adds or subtracts 1 kg
                weight_in_kg = round(weight, 1) + adjustment
                self.update_weight(kg=weight_in_kg)
            else:  # if the unit is imperial
                if current_weight.weight_pd > 0:
                    # adds or subtract 1 pound
                    weight_in_pound = current_weight.weight_pd + adjustment
                    self.update_weight(pound=weight_in_pound)
        else:  # Small step
            adjustment = 0.1 if is_increment else -0.1
            if current_unit == 'metric' and (weight := current_weight.weight_kg) > 0:
                # adds or subtracts 100 grams
                weight_in_kg = round(weight, 1) + adjustment
                self.update_weight(kg=weight_in_kg)

            else:  # imperial
                if is_increment:
                    if current_weight.weight_oz == 15:  # in case we're at maximum amount of ounce
                        self.update_weight(ounce=0,
                                           pound=current_weight.weight_pd + 1
                                           )
                    else:  # otherwise add 1 to ounce
                        self.update_weight(ounce=(current_weight.weight_oz + 1))
                else:  # decrement
                    if current_weight.weight_oz == 0:  # in case we're at minimum ounce
                        self.update_weight(ounce=15,
                                           pound=current_weight.weight_pd - 1
                                           )
                    else:  # otherwise subtract one from ounce
                        self.update_weight(ounce=current_weight.weight_oz - 1)
