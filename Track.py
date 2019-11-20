
class Track:

    def __init__(self,id, name, artist, album, duration):
        self.id = id
        self.name = name
        self.artist = artist
        self.album = album
        self.duration = duration

    def __str__(self):
        if self.id != None:
            return str(f"[{self.id}," +f" de {self.name},"+f"{self.artist},"+f" {self.album},"+f" {self.duration}]")
