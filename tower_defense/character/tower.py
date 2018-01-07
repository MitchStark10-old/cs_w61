from interface import implements
from character.attackable_character import AttackableCharacter
from character.observer import Observer

class Tower(AttackableCharacter, implements(Observer)):
    def __init__(self, attack):
        self._notification_count = 0
        start_health = 35
        attack_range = 5
        AttackableCharacter.__init__(self, start_health, attack, attack_range)
        self._target = None

    def notify(self, observed_invader):
        if self._target == observed_invader:
            if observed_invader.getHealth() <= 0:
                print("Invader has died!")
                self._target = None
            else:
                if (self._notification_count % self._attack.getMovementsBetweenFire()) == 0:
                    print("Attacking!")
                    self._attack.attack(self._target)
                self._notification_count += 1

        if self._target is None:
            #Add as target
            self._target = observed_invader
        #elif observed invader is closer than the target, change targets
