class Crop_Plot:
    # def __init__(self, name, unit_price, crop_yield, growth_time, exchangerate, water_req, sun_req, soil_req) -> None:
    #     self.name = name
    #     self.unit_price = unit_price
    #     self.crop_yield = crop_yield
    #     self.growth_time = growth_time
    #     self.exchangerate = exchangerate
    #     self.water_req = water_req
    #     self.sun_req = sun_req
    #     self.soil_req = soil_req

    def __init__(
        self,
        name,
        unit_price,
        crop_num,
        growth_time,
        days_until_harvest
    ) -> None:
        self.name = name
        self.unit_price = unit_price
        self.crop_num = crop_num
        self.growth_time = growth_time
        self.days_until_harvest = days_until_harvest

    
    
