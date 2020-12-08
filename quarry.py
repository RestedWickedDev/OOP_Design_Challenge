import random

class Ore:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def mine(self):
        random_value = random.randint(20, 50)
        self.value = random_value
        return self.value

    def smelt(self):
        random_value = random.randint(2, 5)
        self.value = self.value * random_value
        return self.value

class Crystal(Ore):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def mine(self):
        random_value = random.randint(50, 100)
        self.value = random_value
        return self.value


    def smelt(self):
        random_value = random.randint(5, 10)
        self.value = self.value * random_value
        return self.value

class Quarry:
    def __init__(self, name, resources):
        self.name = name
        self.resources = resources

        self.ore = list()
        self.crystal = list()

    def obtain_ore(self, name, value):
        name = Ore("iron", value)
        self.ore.append(name)

    def obtain_crystal(self, name, value):
        name = Crystal("diamond", value)
        self.crystal.append(name)

    def sell_all(self):
        sum_value = 0
        for ore in self.ore:
            sum_value += ore.value
        for crystal in self.crystal:
            sum_value += crystal.value
        return sum_value

class Smeltery:
    def __init__(self, name, temperature):
        self.name = name
        self.temperature = temperature
        self.Quarry = Quarry("BlackCrow", "Iron")

    def process_ore(self):
        for ore in self.Quarry.ore:
            ore.mine()
            ore.smelt()
            value = ore.value + self.temperature

    def process_crystal(self):
        for crystal in self.Quarry.crystal:
            crystal.mine()
            crystal.smelt()
            value = crystal.value + self.temperature


if __name__ == "__main__":
    smeltery = Smeltery("SuperForge", 100)
    smeltery.Quarry.obtain_ore("ore", 0)
    smeltery.Quarry.obtain_crystal("crystal", 0)
    smeltery.process_ore()
    smeltery.process_crystal()
    print(smeltery.Quarry.sell_all())
