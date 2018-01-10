from character.invader import Invader
from stack import Stack
from attack.attack_factory import AttackFactory
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
        self._attack_factory = AttackFactory()
        self.seconds_between_invaders = 0

    def _sendWave(self):
        #begin sending invaders one at a time
        while not self.invaders.isEmpty():
            print("testing...")
            self._sendInvader()

    def sendInvader(self):
        #print("part 2")
        if (self.invaders.isEmpty()):
            return
        invader_type = self.invaders.pop()
        attack = self._attack_factory.createAttack(invader_type)
        i = Invader(self._canv, self._path, attack)
        for t in self._app.towers:
            i.addObserver(t)
        self._app.invaders.append(i)
        #print("complete")

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