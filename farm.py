from crop_plot import Crop_Plot
from environment import Enviroment


class Farm:
    def __init__(self, farmname, gametime, farmlocation) -> None:
        self.name = farmname
        self.time = gametime
        self.farmlocation = farmlocation
        self.plots = [
            Crop_Plot("carrots", 0.99, 1, 20, 20),
            Crop_Plot("lettuce", 1.49, 1, 23, 23),
            Crop_Plot("wheat", 0.45, 1, 12, 12),
            Crop_Plot("apples", 1.99, 1, 25, 25),
        ]

    # def get_user_input

    def update_Farm(self):
        weather = Enviroment.rand_weather()
        pests = Enviroment.rand_pests()
        temprature = Enviroment.rand_temp()

        # if weather == 'sunlight':
        #     for i in self.plots:
        #         i.days_until_harvest -= 
        # elif weather == 'rain':



        # Advance daycount +1
        gametime += 1
