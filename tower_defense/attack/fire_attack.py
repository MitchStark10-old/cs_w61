from interface import implements
from attack.attack_base import AttackBase

class FireAttack(AttackBase):
    def __init__(self):
        attack_type = 'fire'
        weakness_type = 'water'
        strength_type = 'grass'
        seconds_in_between_attack = 2
        attack_power = 5
        AttackBase.__init__(self, attack_type, weakness_type, strength_type, seconds_in_between_attack, attack_power)
        print("fire attack object created")
