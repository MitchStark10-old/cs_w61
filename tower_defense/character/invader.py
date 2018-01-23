from character.attackable_character import AttackableCharacter
from character.observable import Observable
from interface import implements
from distance_calculator import DistanceCalculator
import math

class Invader(AttackableCharacter, implements(Observable)):
    def __init__(self, canvas, path, bank, attack):
        starting_health = 20
        attack_range = 3 * 30
        AttackableCharacter.__init__(self, starting_health, attack, attack_range)
        self._color = self.getColorByAttackType()
        self._observers = []
        self._canv = canvas
        self._path = path
        self._bank = bank
        self._alive = True
        self._movements = 0

        self._size = 4   # radius of circle to draw (for now)

        # _dest_cell is the next cell's center that we are moving toward.
        # Start at the 0th cell, which may be off the screen.  Use it
        # to get your x, y value.  Then, find the 1st cell and use that to
        # set the x and y directions.
        self._dest_cell_idx = 0
        self._dest_cell = self._path.get_cell(0)
        self._x, self._y = self._dest_cell.get_center()

        print("Invader: self._x, self._y = ", self._x, self._y)

        self._compute_new_dir()

        # identifier for the circle we draw to represent the invader
        self._id = None
        self.render()

    def getColorByAttackType(self):
        attack_type = self.getAttack().getAttackType()
        if (attack_type == "fire"):
            return "red"
        elif (attack_type == "water"):
            return "blue"
        elif (attack_type == "grass"):
            return "darkgreen"
        else:
            raise ValueError("Attack type [" + attack_type + "] not valid")

    def addObserver(self, new_observer):
        self._observers.append(new_observer)

    def removeObserver(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notifyObservers(self):
        for o in self._observers:
            o.notify(self)

    def removeAllObservers(self):
        self._observers = []
    
    def getMovementsBetweenAttack(self):
        return self._attack.getMovementsBetweenFire() * 2

    def _compute_new_dir(self):
        '''Get (and remember) the next cell in that path, and then
        compute the xdir and ydir to get us from our current position
        to the center of that next cell.'''
        self._dest_cell_idx += 1
        self._dest_cell = self._path.get_cell(self._dest_cell_idx)
        d = self._dest_cell.get_center_x() - self._x
        if d > 0:
            self._xdir = 1
        elif d == 0:
            self._xdir = 0
        else:
            self._xdir = -1
        d = self._dest_cell.get_center_y() - self._y
        if d > 0:
            self._ydir = 1
        elif d == 0:
            self._ydir = 0
        else:
            self._ydir = -1

    def getNearestTower(self):
        known_towers = self._observers
        smallest_distance = math.inf
        return_tower = None

        for t in known_towers:
            current_distance = DistanceCalculator.calculateDistance(self.getXCoord(), self.getYCoord(), t.getXCoord(), t.getYCoord())
            if current_distance < smallest_distance:
                smallest_distance = current_distance
                return_tower = t               

        return return_tower

    def removeSelfFromGame(self):
        self._canv.delete(self._id)


    def move(self):
        if (self._movements % self.getMovementsBetweenAttack() == 0):
            nearest_tower = self.getNearestTower()
            if nearest_tower is not None:
                if not DistanceCalculator.targetOutOfRange(self, nearest_tower, self._attack_range):
                    self._attack.attack(nearest_tower, self)

        if self.getHealth() <= 0:
            #TODO: Remove this invader from the board
            if self._alive:
                self._bank.getInvaderRansom()
                self._alive = False
            self.notifyObservers()
            return

        if (self._x, self._y) == self._dest_cell.get_center():
            # move on to the next cell
            # TODO: HANDLE END OF PATH!
            self._compute_new_dir()

        self._x += self._xdir
        self._y += self._ydir
        self._movements += 1
        self.notifyObservers()

    def getXCoord(self):
        return self._x

    def getYCoord(self):
        return self._y

    def getCoordinates(self):
        return (self._x, self._y)

    def render(self):
        self._canv.delete(self._id)
        self.move()
        self._id = self._canv.create_oval(self._x - self._size, self._y - self._size,
                                          self._x + self._size, self._y + self._size,
                                          fill = self._color)
        # TODO: not sure this is where I want this to happen...
        if not self._alive:
            return
        self._canv.after(30, self.render)
                                          

        
