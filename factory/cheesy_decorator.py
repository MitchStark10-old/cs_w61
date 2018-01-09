from topping_decorator import ToppingDecorator

class CheesyDecorator(ToppingDecorator):
    def __init__(self, pizza, cheese_type):
        ToppingDecorator.__init__(self, pizza)
        self.cheese_type = cheese_type

    def prepare(self):
        self.pizza.prepare()
        print(self.cheese_type + " Cheese")

    def getName(self):
        return self.cheese_type + " Cheese " + self.pizza.getName()