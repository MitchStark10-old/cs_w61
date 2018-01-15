from interface import Interface

class Observable(Interface):
    def addObserver(self, new_observer):
        pass

    def removeObserver(self, observer):
        pass

    def notifyObservers(self):
        pass

    def removeAllObservers(self):
        pass