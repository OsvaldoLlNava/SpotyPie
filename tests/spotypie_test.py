import sys
sys.path.append('../')
import unittest
import Track

from SPYClass import APISFY
from SPYClass import DBSFY
from SPYClass import sinchronize
from spotyPie import SpotyPie
import sqlite3

class testSpotipy(unittest.TestCase):

    # def test_searchTrack(self):
    #     print("TEST searchTrack() <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< SEARCHTRACK()")
    #     print("TESTCASE CORRECT PARAMETERS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< TESTCASE")
    #     objSp=SpotyPie("credenciales.txt","Arma_tu_biblio.db")
    #     track=objSp.searchTrack('Dare','Gorillaz')
    #     print(track)
    #     self.assertEqual(track.__str__(),"[58MZs0B5Amxl0Mwc9FIRZc, DARE - Junior Sanchez Remix, Gorillaz, D-Sides [Special Edition], 326373]")

    #
    # def test_addTracktoMyPlaylist(self):
    #     print("TEST addTrackToMyPlaylist() <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< test_addTracktoMyPlaylist()")
    #     print("TESTCASE CORRECT PARAMETERS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>><<<< TESTCASE")
    #     class Mock_Track:
    #         def __init__(self,id, name, artist, album, duration):
    #             self.id = id
    #             self.name = name
    #             self.artist = artist
    #             self.album = album
    #             self.duration = duration
    #     mock=Mock_Track("58MZs0B5Amxl0Mwc9FIRZc", "DARE - Junior Sanchez Remix", "Gorillaz", "D-Sides [Special Edition]", 326373)
    #     objSp=SpotyPie("credenciales.txt","Arma_tu_biblio.db")
    #     objSp.deleteAllTracks()
    #     self.assertEqual(objSp.addTrackToMyPlaylist(mock),0) ##assert a la funcion
    #     print("Mostrando datos:\n")
    #     self.assertEqual(objSp.showMyPlaylist(),"{ID: 0 [58MZs0B5Amxl0Mwc9FIRZc, DARE - Junior Sanchez Remix, Gorillaz, D-Sides [Special Edition], 326373]}")
    #     objSp.showMyPlaylist()
    #
    # def test_deleteAllTracks(self):
    #     print("TEST delleteAllTracks() <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< delleteAllTracks()")
    #     print("TESTCASE CORRECT PARAMETERS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< TESTCASE")
    #     class Mock_Track:
    #         def __init__(self,id, name, artist, album, duration):
    #             self.id = id
    #             self.name = name
    #             self.artist = artist
    #             self.album = album
    #             self.duration = duration
    #     mock=Mock_Track("58MZs0B5Amxl0Mwc9FIRZc", "DARE - Junior Sanchez Remix", "Gorillaz", "D-Sides [Special Edition]", 326373)
    #     objSp=SpotyPie("credenciales.txt","Arma_tu_biblio.db")
    #
    #     objSp.bdd.deleteAllTracks()
    #     print("Base de datos lista para pruebas ...")
    #     print("Borrando datos de spotify ...")
    #     play=objSp.api.getPlaylistsIDSfromSpotify()
    #     objSp.api.deleteTrack(play)
    #     print("Playlist de spotify lista para pruebas ...")
    #     objSp.addTrackToMyPlaylist(mock)
    #     print("Mostrando datos:\n")
    #     print(objSp.showMyPlaylist())
    #     objSp.showMyPlaylist()
    #     print("delleteAllTracks() ...")
    #     self.assertEqual(objSp.deleteAllTracks(),0)
    #     print("Mostrando datos:\n")
    #     self.assertEqual(objSp.showMyPlaylist(),[])
    #     objSp.showMyPlaylist()

    # def test_deleteTracks(self):
    #     print("TEST delleteAllTracks() <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< delleteAllTracks()")
    #     print("TESTCASE CORRECT PARAMETERS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< TESTCASE")
    #     class Mock_Track:
    #         def __init__(self,id, name, artist, album, duration):
    #             self.id = id
    #             self.name = name
    #             self.artist = artist
    #             self.album = album
    #             self.duration = duration
    #     mock=Mock_Track("58MZs0B5Amxl0Mwc9FIRZc", "DARE - Junior Sanchez Remix", "Gorillaz", "D-Sides [Special Edition]", 326373)
    #     objSp=SpotyPie("credenciales.txt","Arma_tu_biblio.db")
    #
    #     objSp.deleteAllTracks()
    #     print("Playlist y bdd listas")
    #
    #     objSp.addTrackToMyPlaylist(mock)
    #     print("Track guardado")
    #     print("Mostrando datos:\n")
    #     print(objSp.showMyPlaylist())
    #
    #
    #     print("delleteTrack() ...")
    #     objSp.deleteTrack(mock.id)
    #     print("Mostrando datos:\n")
    #     self.assertEqual(objSp.showMyPlaylist(),[])
    #     objSp.showMyPlaylist()
    #
    #
    # def test_showMyPlaylist(self):
    #     print("TEST showMyPlaylist() <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< showMyPlaylist()")
    #     print("TESTCASE CORRECT PARAMETERS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< TESTCASE")
    #     class Mock_Track:
    #         def __init__(self,id, name, artist, album, duration):
    #             self.id = id
    #             self.name = name
    #             self.artist = artist
    #             self.album = album
    #             self.duration = duration
    #     mock1=Mock_Track("58MZs0B5Amxl0Mwc9FIRZc", "DARE - Junior Sanchez Remix", "Gorillaz", "D-Sides [Special Edition]", 326373)
    #     mock2=Mock_Track("08jkW1RWXUwKA3W0bqWGuU", "Get Lucky - Karaoke", "Tribute to Daft Punk", "Get Lucky", 258101)
    #     objSp=SpotyPie("credenciales.txt","Arma_tu_biblio.db")
    #
    #     objSp.deleteAllTracks()
    #     print("Playlist y bdd listas")
    #
    #     objSp.addTrackToMyPlaylist(mock1)
    #     objSp.addTrackToMyPlaylist(mock2)
    #     print("Tracks guardados")
    #     print("Mostrando datos:\n")
    #     print(objSp.showMyPlaylist())
    #     esperado="{ID: 0 [58MZs0B5Amxl0Mwc9FIRZc, DARE - Junior Sanchez Remix, Gorillaz, D-Sides [Special Edition], 326373]}\n{ID: 1 [08jkW1RWXUwKA3W0bqWGuU, Get Lucky - Karaoke, Tribute to Daft Punk, Get Lucky, 258101]}"
    #     self.assertEqual(objSp.showMyPlaylist(),esperado)
    #
    def test_makeSync(self):
        print("TEST makeSync() <<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>><<<<<<<<<<<<<<<<<<<< makeSync()")
        #Tests cases for makeSync
        #   * mismos datos
        #   * no hay datos
        #   * solo datos en spotify
        #   * solo datos en bddlist
        #   * mas datos en spotify que en bddlist
        #   * nas datos en bdd que en Spotify
        #   * mismos datos diferente orden
        #   * igual hasta la mitad de DATOS
        #   * datos en bdd erroneos

        print("TESTCASE  MISMOS DATOS  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>><<< TESTCASE")
        class Mock_Track:
            def __init__(self,id, name, artist, album, duration):
                self.id = id
                self.name = name
                self.artist = artist
                self.album = album
                self.duration = duration
        mock1=Mock_Track("58MZs0B5Amxl0Mwc9FIRZc", "DARE - Junior Sanchez Remix", "Gorillaz", "D-Sides [Special Edition]", 326373)
        mock2=Mock_Track("08jkW1RWXUwKA3W0bqWGuU", "Get Lucky - Karaoke", "Tribute to Daft Punk", "Get Lucky", 258101)
        objSp=SpotyPie("credenciales.txt","Arma_tu_biblio.db")

        objSp.deleteAllTracks()
        print("Playlist y bdd listas")

        objSp.addTrackToMyPlaylist(mock1)
        objSp.addTrackToMyPlaylist(mock2)
        print("Tracks guardados")
        print("Mostrando datos:\n")
        print(objSp.showMyPlaylist())
        esperado="{ID: 0 [58MZs0B5Amxl0Mwc9FIRZc, DARE - Junior Sanchez Remix, Gorillaz, D-Sides [Special Edition], 326373]}\n{ID: 1 [08jkW1RWXUwKA3W0bqWGuU, Get Lucky - Karaoke, Tribute to Daft Punk, Get Lucky, 258101]}"
        self.assertEqual(objSp.showMyPlaylist(),esperado)
    #


if __name__ == '__main__':
    unittest.main()
