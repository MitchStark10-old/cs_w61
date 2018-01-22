import math

class DistanceCalculator:

    @staticmethod
    def calculateDistance(x1,y1,x2,y2):  
        dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
        return dist

    @staticmethod
    def targetOutOfRange(attack_owner, target, attack_range):
        invader_x, invader_y = target.getCoordinates()
        self_x, self_y = attack_owner.getCoordinates()

        if (invader_x < self_x + attack_range) and (invader_x > self_x - attack_range):
            if (invader_y < self_y + attack_range) and (invader_y > self_y - attack_range):
                return False

        return True