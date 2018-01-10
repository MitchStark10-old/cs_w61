from attack.fire_attack import FireAttack
from attack.water_attack import WaterAttack
from attack.grass_attack import GrassAttack

class AttackFactory:
    def createAttack(self, canv, attack_type):
        if attack_type == 'f':
            return FireAttack(canv)
        elif attack_type == 'g':
            return GrassAttack(canv)
        elif attack_type == 'w':
            return WaterAttack(canv)
        else:
            raise ValueError("Bad Value sent to _getInvaderAttackBehavior: " + attack_type)