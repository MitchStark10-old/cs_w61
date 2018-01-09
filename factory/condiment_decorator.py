from topping_decorator import ToppingDecorator

class CondimentDecorator(ToppingDecorator):
    def __init__(self, pizza, condiment_type):
        ToppingDecorator.__init__(self, pizza)
        self.condiment_type = condiment_type

    def prepare(self):
        self.pizza.prepare()
        print(self.condiment_type)

    def getName(self):
        return self.condiment_type + " " + self.pizza.getName()