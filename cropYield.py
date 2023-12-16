import numpy as np

class cropYield():

    def __init__(self, daysSinceRain, sunlight, nutrients, fertilizer, diseases, pests):
        self.parameters = np.array([daysSinceRain, sunlight, nutrients, fertilizer, diseases, pests])
        # self.daysSinceRaine = daysSinceRain
        # self.sunlight = sunlight
        # self.nutrients = nutrients
        # self.fertilizer = fertilizer
        # self.diseases = diseases
        # self.pests = pests
        with open("weights.txt", "r") as f:
            self.weights = np.array([float(i) for i in f.read().split('\n')[:-1]])

    def calculateYield(self):
        return np.dot(self.parameters, self.weights)


x = cropYield(1, 1, 1, 1, 1, 1)
print(x.calculateYield())
