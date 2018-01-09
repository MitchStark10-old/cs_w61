from pizza import Pizza
from square_cut import SquareCut

class ChicagoStylePizza(Pizza):
    def __init__(self, cut_behavior):
        Pizza.__init__(self, cut_behavior)
        self.name = "Chicago Style Deep Dish Pizza"
        self.dough = "Extra Thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"

    def getName(self):
        return self.name


# class ChicagoStyleClamPizza(Pizza):
#     def __init__(self, cut_behavior):
#         Pizza.__init__(self, cut_behavior)
#         self.name = "Chicago Style Pizza"
#         self.dough = "Extra Thick Crust Dough"
#         self.sauce = "Plum Tomato Sauce"

#         self.toppings.append("Shedded Mozzarella Cheese")
#         self.toppings.append("Frozen Clams from Chesapeake Bay")


# class ChicagoStylePepperoniPizza(Pizza):
#     def __init__(self, cut_behavior):
#         Pizza.__init__(self, cut_behavior)
#         self.name = "Chicago Style Pepperoni Pizza"
#         self.dough = "Extra Thick Crust Dough"
#         self.sauce = "Plum Tomato Sauce"

#         self.toppings.append("Shedded Mozzarella Cheese")
#         self.toppings.append("Black Olives")
#         self.toppings.append("Spinach")
#         self.toppings.append("Eggplant")
#         self.toppings.append("Sliced Pepperoni")


# class ChicagoStyleVeggiePizza(Pizza):
#     def __init__(self, cut_behavior):
#         Pizza.__init__(self, cut_behavior)
#         self.name = "Chicago Style Veggie Pizza"
#         self.dough = "Extra Thick Crust Dough"
#         self.sauce = "Plum Tomato Sauce"

#         self.toppings.append("Shedded Mozzarella Cheese")
#         self.toppings.append("Black Olives")
#         self.toppings.append("Spinach")
#         self.toppings.append("Eggplant")

