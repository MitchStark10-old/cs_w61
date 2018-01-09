from pizza import Pizza

class ToppingDecorator(Pizza):
    def __init__(self, pizza):
        self.pizza = pizza

    def cut(self):
        self.pizza.cut()

    def getName(self):
        pass