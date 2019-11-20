from abc import ABC, abstractmethod

class DBService(ABC):
    @abstractmethod
    def saveTrack(self, track):
        pass
