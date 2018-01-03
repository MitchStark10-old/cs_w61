from mallard_duck import MallardDuck
from real_duck import RealDuck

ducks = [RealDuck(), MallardDuck()]

for duck in ducks:
    duck.performFly()
    duck.performQuack()