import random

class EngineECU:

    def __init__(self):
        self.rpm = 800
        self.temperature = 25
        self.fuel_level = 100

    def update(self):
        self.rpm = random.randint(800, 4000)
        self.temperature += 1
        self.fuel_level -= 1

    def read_signals(self):
        return {
            "rpm": self.rpm,
            "temperature": self.temperature,
            "fuel_level": self.fuel_level
        }


if __name__ == "__main__":

    ecu = EngineECU()

    for _ in range(5):

        ecu.update()

        print(ecu.read_signals())