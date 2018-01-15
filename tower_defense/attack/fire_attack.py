from interface import implements
from attack.attack_base import AttackBase

class FireAttack(AttackBase):
    def __init__(self, canv):
        attack_type = 'fire'
        weakness_type = 'water'
        strength_type = 'grass'
        movements_between_attack = 50
        attack_power = 5
        AttackBase.__init__(self, attack_type, weakness_type, strength_type, movements_between_attack, attack_power, canv)
        print("fire attack object created")

    def getCellRange(self):
        return 5