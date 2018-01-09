from interface import implements
from cut_behavior import CutBehavior

class SquareCut(implements(CutBehavior)):
    def cut(self):
        print("Cutting into a square")
