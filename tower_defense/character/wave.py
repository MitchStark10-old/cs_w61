from character.invader import Invader
from stack import Stack
from attack.fire_attack import FireAttack
from attack.water_attack import WaterAttack
from attack.grass_attack import GrassAttack
import json
from threading import Thread
import time

class Wave:
    def __init__(self, app, canv, path):
        self._app = app
        self._canv = canv
        self._path = path
        self.wave_count = 0
        self.invaders = Stack()
        self.seconds_between_invaders = 0

    def _sendWave(self):
        #begin sending invaders one at a time
        while not self.invaders.isEmpty():
            print("testing...")
            self._sendInvader()

    def _sendInvader(self):
        print("part 2")
        if (self.invaders.isEmpty()):
            return
        invader_type = self.invaders.pop()
        attack = self._getInvaderAttackBehavior(invader_type)
        self._app.invaders.append(Invader(self._canv, self._path, attack))
        print("complete")

    def _getInvaderAttackBehavior(self, invader_type):
        if invader_type == 'f':
            return FireAttack()
        elif invader_type == 'g':
            return GrassAttack()
        elif invader_type == 'w':
            return WaterAttack()
        else:
            raise ValueError("Bad Value sent to _getInvaderAttackBehavior: " + invader_type)

    def isWaveFinished(self):
        return self.invaders.isEmpty()


    def readAndSendNextWave(self):
        if not self.isWaveFinished():
            print("Cannot start new wave during active wave!")

        json_data = open('wave_' + str(self.wave_count) + '.json').read()

        data = json.loads(json_data)
        print(data)
        self.seconds_between_invaders = data["seconds_between_invaders"]
        invader_list = data["invaders"]
        for i in invader_list:
            self.invaders.push(i)

        self.wave_count += 1
        self._sendWave()