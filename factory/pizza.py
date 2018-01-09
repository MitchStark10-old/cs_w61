
class Pizza:
    def __init__(self, cut_behavior):
        self.name = None
        self.dough = None
        self.sauce = None
        self.cut_behavior = cut_behavior
        #self.toppings = []

    def prepare(self):
        print("Prepare", self.name)
        print("Tossing dough...")
        print("Adding sauce...")
        print("Adding toppings:")
        # for t in self.toppings:
        #     print("  ", t)

    def bake(self):
        print("Back for 25 minutes at 350")

    def cut(self):
        self.cut_behavior.cut()

    def box(self):
        print("Place pizza in offical PizzaStore box")

    def getName(self):
        return self.name

    def __str__(self):
        res = "----" + self.name + "----\n"
        res += self.dough + "\n"
        res += self.sauce + "\n"
        # for t in self.toppings:
        #     res += self.t + "\n"
        return res