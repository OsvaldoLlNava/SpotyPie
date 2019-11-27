from abc import ABC, abstractmethod

class SFYSERVICE(ABC):
    @abstractmethod
    def saveTrack(self):
        pass
    
    @abstractmethod
    def deleteTrack(self):
        pass
    
    @abstractmethod
    def printPlaylist(self):
        pass


