from duck import Duck
from fly.fly_with_wings import FlyWithWings
from quack.real_quack import RealQuack

class RealDuck(Duck):
    def __init__(self):
        Duck.__init__(self)
        self.setFlyBehavior(FlyWithWings())
        self.setQuackBehavior(RealQuack())