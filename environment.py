import random


class Enviroment:
    def __init__(
        self,
        rainfall,
        sunlight,
        temperature,
        nitrogen_level,
        fertilizer,
        disease,
        pests,
    ):
        # Days since last rainfall
        self.rainfall = rainfall
        # Days since last sunlight
        self.sunlight = sunlight
        # Temperature of the past day
        self.temperature = temperature
        # Nitrogen level of the past day in mg/L
        self.nitrogen_level = nitrogen_level
        # Days since last fertilized
        self.fertilizer = fertilizer
        # Days since last diseased
        self.disease = disease
        #  Days since last pests
        self.pests = pests
        

        
        # def fertilizer() -> int:
        # if userinputfertilizer == 1
        #     counterfertilizer ==5



    def rand_weather(self) -> str: 
        weather_events = ["rain", "sunlight"]
        index = random.randint(0, len(weather_events) - 1)
        weather_event = weather_events[index]
        if weather_event == 'rain':
            self.rainfall = 0
            self.sunlight += 1
        elif weather_event == 'sunlight':
            self.sunlight = 0 
            self.rainfall += 1
        return weather_event
    

    def rand_pests() -> int:
        tempvar = random.randint(1,20)
        if tempvar == '15':
            return 3
        return 0
    
        
    def rand_temp(weather_event) -> int:
        temperature = 72
        if weather_event == 'rain':
            temperature = random.randint(40, 50)
        elif weather_event == "sunlight":
            temperature = random.randint(75, 90)
            
        return temperature
