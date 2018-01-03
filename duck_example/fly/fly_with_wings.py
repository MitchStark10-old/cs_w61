from interface import implements
from fly.fly_behavior import FlyBehavior

class FlyWithWings(implements(FlyBehavior)):
    def fly(self):
        print("I'm Flying!")