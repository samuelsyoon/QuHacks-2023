import random


class Environment:
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
        # Amount of rainfall in the past 2 days in cm
        self.rainfall = rainfall
        # Amount of sunlight in the past 2 days measured in hrs
        self.sunlight = sunlight
        # Average temperature of the past 24 hours
        self.temperature = temperature
        # Average nitrogen level over last two days measured in mg/L
        self.nitrogen_level = nitrogen_level
        # Boolean is Fertilizer present
        self.fertilizer = fertilizer
        # Boolean is Disease present
        self.disease = disease
        # int (0: no pests; 1: pests for one more day)
        self.pests = pests


    def rand_weather() -> str: 
        weather_events = ["rain", "sunlight"]
        index = random.randint(0, len(weather_events) - 1)
        weather_event = weather_events[index]
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
