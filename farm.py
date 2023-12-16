from crop_plot import Crop_Plot
from environment import Enviroment


class Farm:
    def __init__(self, farmname, gametime, farmlocation) -> None:
        self.name = farmname
        self.time = gametime
        self.farmlocation = farmlocation
        self.plots = [
            Crop_Plot("carrots", .99, 1, 20, 20),
            Crop_Plot("lettuce", 1.49, 1, 23, 23),
            Crop_Plot("wheat", .45, 1, 12, 12),
            Crop_Plot("apples", 1.99, 1, 25, 25),
        ]
    
    def update_Farm():
        weather = Enviroment.rand_weather()
        pests = Enviroment.rand_pests()
        temprature = Enviroment.rand_temp()     
        
    

    # def create_plot(self, name, unit_price, crop_num, growth_time):
    #     new_plot = Crop_Plot(name, unit_price, crop_num, growth_time)
    #     self.plots.append(new_plot)

    # def __repr__(self) -> str:
    #     farm_details = ""
    #     for i in self.plots:
    #         farm_details += f"{i.name} "
