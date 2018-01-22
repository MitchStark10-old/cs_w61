import math

class Projectile:
    def __init__(self, canvas, target, shooter):
        self._canv = canvas
        self._target = target
        self._shooter = shooter
        self._finished = False

        self._size = 2   # radius of circle to draw (for now)

        self._x, self._y = self._shooter.getCoordinates()

        self._compute_new_dir()

        # identifier for the circle we draw to represent the invader
        self._id = None
        self.render()

    def _compute_new_dir(self):
        '''Get (and remember) the next cell in that path, and then
        compute the xdir and ydir to get us from our current position
        to the center of that next cell.'''
        xDiff = self._target.getXCoord() - self._x
        yDiff = self._target.getYCoord() - self._y
        angle = math.atan2(yDiff, xDiff)
        self._xdir = math.cos(angle)
        self._ydir = math.sin(angle)


    def checkForFinished(self):
        targetX = int(self._target.getXCoord())
        targetY = int(self._target.getYCoord())
        if int(self._x) in range(targetX-4, targetX+4) and int(self._y) in range(targetY-4, targetY+5):
            self._finished = True

    def move(self):
        self.checkForFinished()
        self._x += self._xdir*3
        self._y += self._ydir*3
        self._compute_new_dir()


    def render(self):
        self._canv.delete(self._id)
        if self._finished == False:
            self.move()
            self._id = self._canv.create_oval(self._x - self._size, self._y - self._size,
                                          self._x + self._size, self._y + self._size,
                                          fill = "Black")
            # TODO: not sure this is where I want this to happen...
            self._canv.after(20, self.render)
        else:
            del self