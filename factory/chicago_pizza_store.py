from pizza_store import PizzaStore
from chicago_style import *
from square_cut import SquareCut
from round_cut import RoundCut
from cheesy_decorator import CheesyDecorator
from condiment_decorator import CondimentDecorator

class ChicagoPizzaStore(PizzaStore):

    def createPizza(self, item, cut_type):
        if cut_type == 'square':
            cut_behavior = SquareCut()
        elif cut_type == 'round':
            cut_behavior = RoundCut()

        if item == "cheese":
            return CheesyDecorator(ChicagoStylePizza(cut_behavior), 'Mozarella')
        elif item == "veggie":
            return CondimentDecorator(CondimentDecorator(CondimentDecorator(ChicagoStylePizza(cut_behavior), 'Onion'), 'Pepper'), 'Onion')
        elif item == "clam":
            return CondimentDecorator(ChicagoStylePizza(cut_behavior), 'Clam')
        elif item == "pepperoni":
            return CondimentDecorator(ChicagoStylePizza(cut_behavior), 'Pepperoni')
        else:
            return None

