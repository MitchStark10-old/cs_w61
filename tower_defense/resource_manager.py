
class ResourceManager:
    def __init__(self, bank):
        self.invaders = []
        self.towers = []
        self.bank = bank

    def getMoney(self):
        return self.bank.getMoney()

    def removeAllInvaders(self):
        for i in self.invaders[:]:
            i.removeSelfFromGame()
            self.invaders.remove(i)