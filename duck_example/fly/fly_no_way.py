from interface import implements
from fly.fly_behavior import FlyBehavior

class FlyNoWay(implements(FlyBehavior)):
    def fly(self):
        print("Can't fly:(")