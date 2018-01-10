from interface import implements
from character.attackable_character import AttackableCharacter
from character.observer import Observer

class Tower(AttackableCharacter, implements(Observer)):
    def __init__(self, attack, app, cell):
        self._notification_count = 0
        self._app = app
        self._cell = cell
        self.subscribeToAllInvaders()
        start_health = 35
        attack_range = 5
        AttackableCharacter.__init__(self, start_health, attack, attack_range)
        self._target = None

    def subscribeToAllInvaders(self):
        for i in self._app.invaders:
            i.addObserver(self)

    def notify(self, observed_invader):
        if self._target == observed_invader:
            if observed_invader.getHealth() <= 0:
                self._target = None
                if observed_invader in self._app.invaders:
                    self._app.invaders.remove(observed_invader)
                    print("made it here")
                return
            else:
                if (self._notification_count % self._attack.getMovementsBetweenFire()) == 0:
                    print("Attacking!")
                    self._attack.attack(self._target, self)
                self._notification_count += 1

        if self._target is None:
            #Add as target
            self._target = observed_invader
        #elif observed invader is closer than the target, change targets

    def getXCoord(self):
        return self._cell.get_x()
    
    def getYCoord(self):
        return self._cell.get_y()

    def getCoordinates(self):
        return self._cell.get_center()