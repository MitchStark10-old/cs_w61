from interface import interface

class AttackableCharacter:
    def __init__(self, start_health):
        self._health = start_health

    def decreaseHealth(self, health__decrease):
        self._health -= health__decrease