from character.invader import Invader
from stack import Stack
from attack.attack_factory import AttackFactory
import json
from threading import Thread
import time

class Wave:
    def __init__(self, resource_manager, canv, path):
        self._resource_manager = resource_manager
        self._canv = canv
        self._path = path
        self.wave_count = 0
        self.invaders = Stack()
        self._attack_factory = AttackFactory()
        self.seconds_between_invaders = 0

    def sendInvader(self):
        #print("part 2")
        if (self.invaders.isEmpty()):
            return
        invader_type = self.invaders.pop()
        attack = self._attack_factory.createAttack(self._canv, invader_type)
        i = Invader(self._canv, self._path, self._resource_manager.bank, attack)
        for t in self._resource_manager.towers:
            i.addObserver(t)
        self._resource_manager.invaders.append(i)
        #print("complete")

    def isWaveFinished(self):
        return self.invaders.isEmpty()


    def readAndSendNextWave(self):
        if not self.isWaveFinished():
            print("Cannot start new wave during active wave!")
            return

        json_data = open('wave_' + str(self.wave_count) + '.json').read()

        data = json.loads(json_data)
        print(data)
        self.seconds_between_invaders = data["seconds_between_invaders"]
        invader_list = data["invaders"]
        for i in invader_list:
            self.invaders.push(i)

        self.wave_count += 1