from abc import ABC, abstractmethod

class DBService(ABC):
    @abstractmethod
    def saveTrack(self):
        pass

    @abstractmethod
    def deleteTrack(self):
        pass


    @abstractmethod
    def getPlaylistFromDB(self):
        pass
    
