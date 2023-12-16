import numpy as np
import math
from environment import Environment

class CropYield():

    def __init__(self, environment: Environment, max_height, starting_height):

        self.current_environment = environment
        self.parameters = np.array([self.current_environment.rainfall, self.current_environment.sunlight, self.current_environment.temperature, self.current_environment.nitrogen_level, self.current_environment.fertilizer, self.current_environment.disease, self.current_environment.pests])

        self.max_height = max_height
        self.current_height = starting_height
        self.starting_height = starting_height

    
    def updateEnvironment(self, environment: Environment):
        self.current_environment = environment
        self.parameters = np.array([self.current_environment.rainfall, self.current_environment.sunlight, self.current_environment.temperature, self.current_environment.nitrogen_level, self.current_environment.fertilizer, self.current_environment.disease, self.current_environment.pests])


    def calculateWeights(self):
        rain = -1 * math.e ** (0.15 * self.current_environment.rainfall)
        sun = -1 * math.e ** (0.15 * self.current_environment.sunlight) 
        temperature = 0.25 - (75 - self.current_environment.temperature) ** 2 / 1200
        nitrogen = -1 * 0.04 * self.current_environment.nitrogen_level
        fertilizer = 0.15
        disease = 0.15
        pest = 0.15

        self.weights = np.array([rain, sun, temperature, nitrogen, fertilizer, disease, pest])


    def growth(self):
        self.calculateWeights()
        # print("k: " + str(np.dot(self.parameters, self.weights)))
        # print("rest: " + str((self.current_height + 1) * (self.max_height - self.current_height)))
        # print("cur: " + str(self.current_height) + " max: " + str(self.max_height))
        self.current_height = max(0, self.current_height + np.dot(self.parameters, self.weights) / 1000 * (self.current_height + 1) * (self.max_height - self.current_height))


def simulation(days):
    plant = CropYield(Environment(0, 0, 80, 0, 0, 0, 0), 10, 0)
    for i in range(days):
        e = Environment(0, 0, 75, i, 0, 0, 0)
        plant.updateEnvironment(e)
        plant.growth()
        
        print(f"day {i}: {plant.current_height}")

    # with open("data.txt", "w") as f:
    #     f.write("\n".join([str(i) for i in y_data]))
    #
    # with open("x.txt", "w") as f:
    #     f.write("\n".join([str(i) for i in range(days)]))
    

simulation(30) 

