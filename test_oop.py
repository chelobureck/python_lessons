class Car:
    def __init__(self, color, brend, vin):
        self.color = color
        self.brend = brend
        self.__vin = vin

    def drift(self, drift):
        return f"{self.color} {self.brend} очень круто {drift}!"

    def make_sound(self,sound):
        return f"{self.color} ({self.brend}) она делает {sound}"

    def __get_vin(self):
        return f'VIN number : {self.__vin}'

    def get_secret_vin(self):
        return self.__get_vin()


class Racing(Car):
    def make_sound(self): # type: ignore
        return "Врум-Врум!"



racing = Racing("красная","Ламбарджини", "123324532341234")
print(racing.drift("дрифтит"))
print(racing.make_sound())
print(racing.get_secret_vin())

# test line