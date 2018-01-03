class Duck:
    def __init__(self):
        self._fly_behavior = None
        self._quack_behavior = None

    def setFlyBehavior(self, new_fly_behavior):
        self._fly_behavior = new_fly_behavior

    def setQuackBehavior(self, new_quack_behavior):
        self._quack_behavior = new_quack_behavior

    def performFly(self):
        self._fly_behavior.fly()

    def performQuack(self):
        self._quack_behavior.quack()

    def swim(self):
        print("All ducks float, even decoys!")