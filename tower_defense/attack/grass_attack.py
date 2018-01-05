from interface import implements
from attack.attack_base import AttackBase

class GrassAttack(AttackBase):
    def __init__(self):
        attack_type = 'grass'
        weakness_type = 'fire'
        strength_type = 'water'
        seconds_in_between_attack = 0.5
        attack_power = 2
        AttackBase.__init__(self, attack_type, weakness_type, strength_type, seconds_in_between_attack, attack_power)
        print("water attack object created")