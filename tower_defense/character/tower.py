from interface import implements
from character.attackable_character import AttackableCharacter
from character.observer import Observer

class Tower(AttackableCharacter, implements(Observer)):
    def __init__(self, attack):
        start_health = 35
        attack_range = 5
        AttackableCharacter.__init__(self, start_health, attack, attack_range)
        self._target = None

    def notify(self, observed_invader):
        if self._target == observed_invader:
            if observed_invader.getHealth() <= 0:
                self._target = None

        if self._target is None:
            #Add as target
            pass
        #elif observed_invader is closer than the target, focus on that one