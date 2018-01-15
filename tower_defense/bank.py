#This class keeps track of the money for the user
class Bank:
    def __init__(self, app):
        self._money = 30
        self._app = app

    def buyTower(self):
        successful_purchase = False
        if (self._money >= 10):
            self._money -= 10
            self._app.updateGoldAmount(self._money)
            successful_purchase = True

        return successful_purchase

    def getInvaderRansom(self):
        self._money += 1
        self._app.updateGoldAmount(self._money)

    def getMoney(self):
        return self._money