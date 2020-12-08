import random

class Ore:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def mine(self):
        random_value = random.randint(20, 50)
        value = random_value
        return value

    def smelt():
        random_value = random.randint(2, 5)
        value = value * random_value
        return value

class Crystal(Ore):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def mine():
        random_value = random.randint(50, 100)
        value = random_value
        return value


    def smelt():
        random_value = random.randint(5, 10)
        value = value * random_value
        return value


class Smeltery:
    def __init__(self, name, fuel):
        self.name = name
        self.fuel = fuel

    def deposit_ore():
        return

    def process_ore():
        return

class Quarry:
    def __init__(self, name, resources):
        self.name = name
        self.resources = resources

        self.ore = list()

    def obtain_ore(self, Ore):
        self.ore.append(Ore)


    def sell_all():
        return
