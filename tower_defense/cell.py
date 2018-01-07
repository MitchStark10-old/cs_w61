from tkinter import *
from character.tower import Tower
from attack.fire_attack import FireAttack
from attack.water_attack import WaterAttack
from attack.grass_attack import GrassAttack
import random


class Cell:
    TYPE2COL = { 'path': 'brown', 'fire-tower': 'red', 'other': 'white', 'water-tower': 'blue', 'grass-tower': 'darkgreen' }
    def __init__(self, canvas, x, y, size, type='other'):
        self._canv = canvas
        self._x = x
        self._y = y
        self._size = size
        self._ulx = x * size          # upper-left x
        self._lrx = self._ulx + size  # lower-right x
        self._uly = y * size          # upper-left y
        self._lry = self._uly + size  # lower-right y
        self._tag = "cell" + str(x) + str(y)
        self._id = None
        # True when the mouse is in this cell.
        self._mouseIn = False
        self.set_type(type)
        self._id = self._canv.create_rectangle(self._ulx, self._uly, self._lrx, self._lry,
                                               fill=Cell.TYPE2COL[self._type], tag=self._tag)
        self._canv.tag_bind(self._id, "<Enter>", self.highlight)
        self._canv.tag_bind(self._id, "<Leave>", self.clear)
        self._canv.tag_bind(self._id, "<ButtonPress-1>", self.onClick)
        self._tower = None

    def clear(self, event=None):
        self._mouseIn = False
        self._canv.itemconfig(self._id, fill=Cell.TYPE2COL[self._type])

    def highlight(self, event=None):
        # Show green where the mouse is.
        self._canv.itemconfig(self._id, fill='green')
        self._mouseIn = True

    def onClick(self, event=None):
        if (self._type == 'other'):
            #place tower
            self._tower = Tower(FireAttack())
            self.set_type('fire-tower')
            print("Placed fire tower")
        elif self._type == 'fire-tower':
            self._tower.setAttack(WaterAttack())
            self.set_type('water-tower')
        elif self._type == 'water-tower':
            self._tower.setAttack(GrassAttack())
            self.set_type('grass-tower')
        elif self._type == 'grass-tower':
            self._tower.setAttack(FireAttack())
            self.set_type('fire-tower')
        else:
            print("Can't place tower here")

    def __contains__(self, xy):
        '''Return True if the given x,y tuple is in the rectangle, False
        otherwise.'''
        x, y = xy
        return self._ulx < x < self._lrx and self._uly < y < self._lry

    def get_x(self):
        return self._x
    def get_y(self):
        return self._y

    def get_center(self):
        return (self.get_center_x(), self.get_center_y())

    def get_center_x(self):
        return self._ulx + (self._size / 2)
    def get_center_y(self):
        return self._uly + (self._size / 2)

    def set_type(self, type):
        self._type = type     # should use sub-class?
        if self._id is not None:
            self._canv.itemconfig(self._id, fill=Cell.TYPE2COL[self._type])
        

    
