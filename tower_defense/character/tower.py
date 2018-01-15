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
        attack_range = attack.getCellRange() * 30
        AttackableCharacter.__init__(self, start_health, attack, attack_range)
        self._target = None

    def subscribeToAllInvaders(self):
        for i in self._app.invaders:
            i.addObserver(self)

    def updateForInvaderDeath(self, observed_invader):
        self._target = None
        # observed_invader.removeAllObservers() #this prevents reassignment, don't know why
        if observed_invader in self._app.invaders:
            self._app.invaders.remove(observed_invader)

    def _targetOutOfRange(self):
        invader_x, invader_y = self._target.getCoordinates()
        self_x, self_y = self.getCoordinates()

        if (invader_x < self_x + self._attack_range) and (invader_x > self_x - self._attack_range):
            if (invader_y < self_y + self._attack_range) and (invader_y > self_y - self._attack_range):
                return False

        return True

    def sendAttack(self):
        if (self._targetOutOfRange()):
            self._target = None
            return

        if (self._notification_count % self._attack.getMovementsBetweenFire()) == 0:
            self._attack.attack(self._target, self)
        self._notification_count += 1

    def reassignTargetWhenNeeded(self, observed_invader):
        if self._target is None:
            #Add as target
            self._target = observed_invader

    def notify(self, observed_invader):
        if self._target == observed_invader:
            if observed_invader.getHealth() <= 0:
                self.updateForInvaderDeath(observed_invader)
            else:
                self.sendAttack()
            return
        self.reassignTargetWhenNeeded(observed_invader)

    def getXCoord(self):
        return self._cell.get_x()
    
    def getYCoord(self):
        return self._cell.get_y()

    def getCoordinates(self):
        return self._cell.get_center()