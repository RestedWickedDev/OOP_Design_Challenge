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


class Smeltery:
    def __init__(self, name, temperature):
        self.name = name
        self.temperature = temperature

    def deposit_ore(self):
        return

    def process_ore(self):
        for ore in Quarry.ore:
            Ore.smelt()
            ore.value + self.temperature
        return

class Quarry:
    def __init__(self, name, resources):
        self.name = name
        self.resources = resources

        self.ore = list()

    def obtain_ore(self, Ore):
        self.ore.append(Ore)
        return self.ore


    def sell_all(self):
        sum_value = 0
        for ore in self.ore:
            sum_value += ore.value
        return sum_value

if __name__ == "__main__":
    ore = Ore("Iron", 0)
    ore.mine()
    ore2 = Crystal("Diamond", 0)
    ore2.mine()
    smelt = Smeltery("Skyforge", 100)
    smelt.process_ore()
    quarry = Quarry("BlackCrow Mine", "iron")
    quarry.obtain_ore(ore)
    quarry.obtain_ore(ore2)
    print(quarry.sell_all())
