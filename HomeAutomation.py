class HomeAutomation:
    def __init__(self):
        self.lights = {}
        self.outlets = {}

    def add_light(self, light_name):
        self.lights[light_name] = False
        print(f"Ajouter une nouvelle lumière: {light_name}")

    def add_outlet(self, outlet_name):
        self.outlets[outlet_name] = False
        print(f"Ajouter une nouvelle prise: {outlet_name}")

    def turn_on_light(self, light_name):
        if light_name in self.lights:
            self.lights[light_name] = True
            print(f"Allume la lumière: {light_name}")
        else:
            print(f"Pas de lumière de trouvé avec le nom : {light_name}")

    def turn_off_light(self, light_name):
        if light_name in self.lights:
            self.lights[light_name] = False
            print(f"Eteint la lumière: {light_name}")
        else:
            print(f"Pas de lumère de trouvée avec le nom : {light_name}")

    def switch_on_outlet(self, outlet_name):
        if outlet_name in self.outlets:
            self.outlets[outlet_name] = True
            print(f"Allume la prise de : {outlet_name}")
        else:
            print(f"Pas de prise de trouvée avec le nom : {outlet_name}")

    def switch_off_outlet(self, outlet_name):
        if outlet_name in self.outlets:
            self.outlets[outlet_name] = False
            print(f"Eteint la prise de : {outlet_name}")
        else:
            print(f"Pas de prise de trouvée avec le nom : {outlet_name}")
