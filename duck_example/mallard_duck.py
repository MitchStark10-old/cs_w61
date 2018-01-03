from duck import Duck
from fly.fly_no_way import FlyNoWay
from quack.no_quack import NoQuack

class MallardDuck(Duck):
    def __init__(self):
        Duck.__init__(self)
        self.setFlyBehavior(FlyNoWay())
        self.setQuackBehavior(NoQuack())
