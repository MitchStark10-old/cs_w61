from character.attackable_character import AttackableCharacter

class Invader(AttackableCharacter):
    def __init__(self, canvas, path, attack):
        starting_health = 20
        AttackableCharacter.__init__(self, starting_health)
        self._attack = attack
        self._canv = canvas
        self._path = path

        self._size = 4   # radius of circle to draw (for now)

        # _dest_cell is the next cell's center that we are moving toward.
        # Start at the 0th cell, which may be off the screen.  Use it
        # to get your x, y value.  Then, find the 1st cell and use that to
        # set the x and y directions.
        self._dest_cell_idx = 0
        self._dest_cell = self._path.get_cell(0)
        self._x, self._y = self._dest_cell.get_center()

        print("Invader: self._x, y = ", self._x, self._y)

        self._compute_new_dir()

        # identifier for the circle we draw to represent the invader
        self._id = None
        self.render()

    def getAttack(self):
        return self._attack

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

    def move(self):
        if (self._x, self._y) == self._dest_cell.get_center():
            # move on to the next cell
            # TODO: HANDLE END OF PATH!
            self._compute_new_dir()
        self._x += self._xdir
        self._y += self._ydir

    def render(self):
        self._canv.delete(self._id)
        self.move()
        self._id = self._canv.create_oval(self._x - self._size, self._y - self._size,
                                          self._x + self._size, self._y + self._size,
                                          fill = "black")
        # TODO: not sure this is where I want this to happen...
        self._canv.after(30, self.render)
                                          

        
