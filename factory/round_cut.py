from interface import implements
from cut_behavior import CutBehavior

class RoundCut(implements(CutBehavior)):
    def cut(self):
        print("Cutting into a circle")