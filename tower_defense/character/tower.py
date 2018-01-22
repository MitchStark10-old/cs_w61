from interface import implements
from character.attackable_character import AttackableCharacter
from character.observer import Observer
from distance_calculator import DistanceCalculator

class Tower(AttackableCharacter, implements(Observer)):
    def __init__(self, attack, resource_manager, cell):
        self._notification_count = 0
        self._resource_manager = resource_manager
        self._cell = cell
        self.subscribeToAllInvaders()
        start_health = 100
        attack_range = attack.getCellRange() * 30
        AttackableCharacter.__init__(self, start_health, attack, attack_range)
        self._target = None

    def subscribeToAllInvaders(self):
        for i in self._resource_manager.invaders:
            i.addObserver(self)

    def updateForInvaderDeath(self, observed_invader):
        self._target = None
        # observed_invader.removeAllObservers() #this prevents reassignment, don't know why
        if observed_invader in self._resource_manager.invaders:
            self._resource_manager.invaders.remove(observed_invader)

    def sendAttack(self):
        if (DistanceCalculator.targetOutOfRange(self, self._target, self._attack_range)):
            self._target = None
            return
    
        if (self._notification_count % self._attack.getMovementsBetweenFire()) == 0:
            self._attack.attack(self._target, self)
        self._notification_count += 1

    def reassignTargetWhenNeeded(self, observed_invader):
        if self._target is None:
            #Add as target
            self._target = observed_invader

    def unsubscribeFromAllInvaders(self):
        for i in self._resource_manager.invaders:
            i.removeObserver(self)

    def removeTowerFromGame(self):
        #remove tower from canvas
        self._cell.set_type('other')
        #remove tower from subscribed list
        self.unsubscribeFromAllInvaders()
        #remove tower from app.towers
        if self in self._resource_manager.towers:
            self._resource_manager.towers.remove(self)
        
        del self

    def notify(self, observed_invader):
        if (self.getHealth() <= 0):
            self.removeTowerFromGame()
            return

        if self._target == observed_invader:
            if observed_invader.getHealth() <= 0:
                self.updateForInvaderDeath(observed_invader)
            else:
                self.sendAttack()
            return
        self.reassignTargetWhenNeeded(observed_invader)

    def getXCoord(self):
        return self._cell.get_center_x()
    
    def getYCoord(self):
        return self._cell.get_center_y()

    def getCoordinates(self):
        return self._cell.get_center()