class AttackBase:
    def __init__(self, attack_type, attack_weakness, attack_strength, seconds_between_fire, attack_power):
        self._attack_type = attack_type
        self._attack_weakness = attack_weakness
        self._attack_strength = attack_strength
        self._seconds_between_fire = seconds_between_fire
        self._attack_power = attack_power

    def getAttackType(self):
        return self._attack_type

    def getAttackWeakness(self):
        return self._attack_weakness

    def getAttackStrength(self):
        return self._attack_strength

    def getSecondsBetweenFire(self):
        return self._seconds_between_fire

    #character to attack can be either tower or invader
    def attack(self, character_to_attack):
        multiplier = 1

        if character_to_attack.getAttack().getAttackType() == self._attack_strength:
            multiplier = 2
        elif character_to_attack.getAttack().getAttackType() == self._attack_weakness:
            multiplier = (0.5)

        hp_affected = self._attack_power * multiplier

        character_to_attack.decreaseHealth(hp_affected)
