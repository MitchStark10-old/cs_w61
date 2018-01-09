
class PizzaStore:

    def createPizza(self, item, cut_type):
        raise NotImplementedError()

    def orderPizza(self, type, cut_type):
        pizza = self.createPizza(type, cut_type)
        print("Making a", pizza.getName(), "---")
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza