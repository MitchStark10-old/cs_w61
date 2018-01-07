from interface import implements
from attack.attack_base import AttackBase

class WaterAttack(AttackBase):
    def __init__(self):
        attack_type = 'water'
        weakness_type = 'grass'
        strength_type = 'fire'
        movements_between_attack = 30
        attack_power = 3
        AttackBase.__init__(self, attack_type, weakness_type, strength_type, movements_between_attack, attack_power)
        print("water attack object created")