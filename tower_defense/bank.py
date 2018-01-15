#This class keeps track of the money for the user
class Bank:
    def __init__(self):
        self._money = 30

    def buyTower(self):
        successful_purchase = False
        if (self._money >= 10):
            self._money -= 10
            successful_purchase = True

        return successful_purchase

    def getInvaderRansom(self):
        self._money += 1