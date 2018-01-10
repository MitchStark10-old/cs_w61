from attack.fire_attack import FireAttack
from attack.water_attack import WaterAttack
from attack.grass_attack import GrassAttack

class AttackFactory:
    def createAttack(self, attack_type):
        if attack_type == 'f':
            return FireAttack()
        elif attack_type == 'g':
            return GrassAttack()
        elif attack_type == 'w':
            return WaterAttack()
        else:
            raise ValueError("Bad Value sent to _getInvaderAttackBehavior: " + attack_type)