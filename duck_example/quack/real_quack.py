from interface import implements
from quack.quack_behavior import QuackBehavior

class RealQuack(implements(QuackBehavior)):
    def quack(self):
        print("Quack!")