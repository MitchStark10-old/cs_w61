from interface import implements
from quack.quack_behavior import QuackBehavior

class NoQuack(implements(QuackBehavior)):
    def quack(self):
        print("...")