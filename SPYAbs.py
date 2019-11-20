from abc import ABC, abstractmethod

class SFYSERVICE(ABC):
    @abstractmethod
    def get_track_info(self, trackName, artist):
        pass
