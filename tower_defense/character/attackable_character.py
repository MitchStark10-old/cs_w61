from interface import interface

class AttackableCharacter:
    def __init__(self, start_health, attack, attack_range):
        self._health = start_health
        self._attack = attack
        self._attack_range = attack_range

    def decreaseHealth(self, health_decrease):
        self._health -= health_decrease

    def getAttack(self):
        return self._attack

    def setAttack(self, new_attack):
        self._attack = new_attack

    def getHealth(self):
        return self._health

    def getXCoord(self):
        raise NotImplementedError()

    def getYCoord(self):
        raise NotImplementedError()

    def getCoordinates(self):
        raise NotImplementedError()