from interface import implements
from attack.attack_base import AttackBase

class GrassAttack(AttackBase):
    def __init__(self, canv):
        attack_type = 'grass'
        weakness_type = 'fire'
        strength_type = 'water'
        movements_between_attack = 40
        attack_power = 2
        AttackBase.__init__(self, attack_type, weakness_type, strength_type, movements_between_attack, attack_power, canv)
        print("grass attack object created")