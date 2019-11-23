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

    def test_searchTrack(self):
        print("TEST searchTrack() <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< SEARCHTRACK()")
        print("TESTCASE CORRECT PARAMETERS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< TESTCASE")
        objSp=SpotyPie("credenciales.txt","Arma_tu_biblio.db")
        track=objSp.searchTrack('Dare','Gorillaz')
        print("Track: ",track)
        self.assertEqual(track.__str__(),"[58MZs0B5Amxl0Mwc9FIRZc, DARE - Junior Sanchez Remix, Gorillaz, D-Sides [Special Edition], 326373]")


    def test_addTracktoMyPlaylist(self):
        print("TEST addTrackToMyPlaylist() <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< test_addTracktoMyPlaylist()")
        print("TESTCASE CORRECT PARAMETERS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>><<<< TESTCASE")
        class Mock_Track:
            def __init__(self,id, name, artist, album, duration):
                self.id = id
                self.name = name
                self.artist = artist
                self.album = album
                self.duration = duration
        mock=Mock_Track("58MZs0B5Amxl0Mwc9FIRZc", "DARE - Junior Sanchez Remix", "Gorillaz", "D-Sides [Special Edition]", 326373)
        objSp=SpotyPie("credenciales.txt","Arma_tu_biblio.db")
        objSp.deleteAllTracks()
        self.assertEqual(objSp.addTrackToMyPlaylist(mock),0) ##assert a la funcion
        print("Mostrando datos:\n")
        self.assertEqual(objSp.showMyPlaylist(),"{ID: 0 [58MZs0B5Amxl0Mwc9FIRZc, DARE - Junior Sanchez Remix, Gorillaz, D-Sides [Special Edition], 326373]}")
        objSp.showMyPlaylist()

    def test_deleteAllTracks(self):
        print("TEST delleteAllTracks() <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< delleteAllTracks()")
        print("TESTCASE CORRECT PARAMETERS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< TESTCASE")
        class Mock_Track:
            def __init__(self,id, name, artist, album, duration):
                self.id = id
                self.name = name
                self.artist = artist
                self.album = album
                self.duration = duration
        mock=Mock_Track("58MZs0B5Amxl0Mwc9FIRZc", "DARE - Junior Sanchez Remix", "Gorillaz", "D-Sides [Special Edition]", 326373)
        objSp=SpotyPie("credenciales.txt","Arma_tu_biblio.db")

        objSp.bdd.deleteAllTracks()
        print("Base de datos lista para pruebas ...")
        print("Borrando datos de spotify ...")
        play=objSp.api.getPlaylistsIDSfromSpotify()
        objSp.api.deleteTrack(play)
        print("Playlist de spotify lista para pruebas ...")
        objSp.addTrackToMyPlaylist(mock)
        print("Mostrando datos:\n")
        print(objSp.showMyPlaylist())
        objSp.showMyPlaylist()
        print("delleteAllTracks() ...")
        self.assertEqual(objSp.deleteAllTracks(),0)
        print("Mostrando datos:\n")
        self.assertEqual(objSp.showMyPlaylist(),[])
        objSp.showMyPlaylist()

    def test_deleteTracks(self):
        print("TEST delleteAllTracks() <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< delleteAllTracks()")
        print("TESTCASE CORRECT PARAMETERS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< TESTCASE")
        class Mock_Track:
            def __init__(self,id, name, artist, album, duration):
                self.id = id
                self.name = name
                self.artist = artist
                self.album = album
                self.duration = duration
        mock=Mock_Track("58MZs0B5Amxl0Mwc9FIRZc", "DARE - Junior Sanchez Remix", "Gorillaz", "D-Sides [Special Edition]", 326373)
        objSp=SpotyPie("credenciales.txt","Arma_tu_biblio.db")

        objSp.deleteAllTracks()
        print("Playlist y bdd listas")

        objSp.addTrackToMyPlaylist(mock)
        print("Track guardado")
        print("Mostrando datos:\n")
        print(objSp.showMyPlaylist())


        print("delleteTrack() ...")
        objSp.deleteTrack(mock.id)
        print("Mostrando datos:\n")
        self.assertEqual(objSp.showMyPlaylist(),[])
        objSp.showMyPlaylist()


    def test_showMyPlaylist(self):
        print("TEST showMyPlaylist() <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< showMyPlaylist()")
        print("TESTCASE CORRECT PARAMETERS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< TESTCASE")
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
    # def test_makeSync(self):
    #     print("TEST makeSync() <<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>><<<<<<<<<<<<<<<<<<<< makeSync()")
    # #     # Tests cases for makeSync
    # #     #   * mismos datos......................... ok
    # #     #   * no hay datos......................... ok
    # #     #   * solo datos en spotify................ ok
    # #     #   * solo datos en bddlist................ ok
    # #     #   * mas datos en spotify que en bddlist.. ok
    # #     #   * nas datos en bdd que en Spotify...... ok
    # #     #   * mismos datos diferente orden......... ok
    # #     #   * igual hasta la mitad de DATOS........ ok
    # #     #   * datos en bdd erroneos................
    # #
    # #
    #     class Mock_Track:
    #         def __init__(self,id, name, artist, album, duration):
    #             self.id = id
    #             self.name = name
    #             self.artist = artist
    #             self.album = album
    #             self.duration = duration
    #     objSp=SpotyPie("credenciales.txt","Arma_tu_biblio.db")
    #     mock1=Mock_Track("58MZs0B5Amxl0Mwc9FIRZc", "DARE - Junior Sanchez Remix", "Gorillaz", "D-Sides [Special Edition]", 326373)
    #     mock2=Mock_Track("08jkW1RWXUwKA3W0bqWGuU", "Get Lucky - Karaoke", "Tribute to Daft Punk", "Get Lucky", 258101)
    #     mock3=Mock_Track("504jTZvXdP8YYVtd19rfuX", "BDE (Best Day Ever) - Live","Mac Miller", "Live From Space", 321960)
    #     mock4=Mock_Track("7I708EIVfgOpcv6ltbXwbm", "Another Brick in the Wall", "Pink Floyd Tribute Band", "World's Greatest Rock Anthems - The Only Rock Tributes Album You'll Ever Need! (Deluxe Version)", 188013)
    #     mockFake1=Mock_Track("A"*22, "CANCION FALSA 1", "ARTISTA FALSO 1", "ALBUM FALSO 1", 100000)
    #     mockFake2=Mock_Track("B"*22, "CANCION FALSA 2", "ARTISTA FALSO 2", "ALBUM FALSO 2", 100000)
    # #
    #     #
    #     print("TESTCASE  MISMOS DATOS  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>><<< TESTCASE")
    #
    #     objSp.deleteAllTracks()
    #     print("Playlist y bdd listas")
    #
    #
    #     objSp.addTrackToMyPlaylist(mock1)
    #     objSp.addTrackToMyPlaylist(mock2)
    #     print("Tracks guardados")
    #     print("Mostrando datos:\n")
    #     print(objSp.showMyPlaylist())
    #     esperado="{ID: 0 [58MZs0B5Amxl0Mwc9FIRZc, DARE - Junior Sanchez Remix, Gorillaz, D-Sides [Special Edition], 326373]}\n{ID: 1 [08jkW1RWXUwKA3W0bqWGuU, Get Lucky - Karaoke, Tribute to Daft Punk, Get Lucky, 258101]}"
    #     self.assertEqual(objSp.showMyPlaylist(),esperado)
    #     self.assertEqual(objSp.makeSync(),0)
    #
    #     print("TESTCASE SIN  DATOS  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>><<< TESTCASE")
    #     objSp.deleteAllTracks()
    #     print("Playlist y bdd listos")
    #     print(objSp.showMyPlaylist())
    #     #print(objSp.makeSync())
    #     self.assertEqual(objSp.makeSync(),0)
    #
    #     print("TESTCASE DATOS SOLO EN BDD  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>><<< TESTCASE")
    #
    #     objSp.deleteAllTracks()
    #     print("Playlist y bdd listas")
    #
    #     objSp.bdd.saveTrack(mock1)
    #     objSp.bdd.saveTrack(mock2)
    #     print("Tracks guardados")
    #     print("Mostrando datos (mostrara los de la bdd):\n")
    #     print(objSp.showMyPlaylist())
    #     print("\nMostrando datos (mostrara los de la spotify):\n")
    #     print(objSp.api.printPlaylist(objSp.api.getTrackslistfromSpotify()))
    #     #esperado="{ID: 0 [58MZs0B5Amxl0Mwc9FIRZc, DARE - Junior Sanchez Remix, Gorillaz, D-Sides [Special Edition], 326373]}\n{ID: 1 [08jkW1RWXUwKA3W0bqWGuU, Get Lucky - Karaoke, Tribute to Daft Punk, Get Lucky, 258101]}"
    #     #objSp.showMyPlaylist()
    #     self.assertEqual(objSp.makeSync(),0)
    #     print("\nMostrando datos (mostrara los de la spotify):\n")
    #     print(objSp.api.printPlaylist(objSp.api.getTrackslistfromSpotify()))
    #     expect=""
    #     expect+="{ID: 0 [08jkW1RWXUwKA3W0bqWGuU, Get Lucky - Karaoke, Tribute to Daft Punk, Get Lucky, 258101]}\n"
    #     expect+="{ID: 1 [58MZs0B5Amxl0Mwc9FIRZc, DARE - Junior Sanchez Remix, Gorillaz, D-Sides [Special Edition], 326373]}"
    #     self.assertEqual(objSp.api.printPlaylist(objSp.api.getTrackslistfromSpotify()),expect)
    #
    #     print("TESTCASE DATOS SOLO EN SPOTIFY  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>><<< TESTCASE")
    #
    #     objSp.deleteAllTracks()
    #     print("Playlist y bdd listas")
    #
    #     objSp.api.saveTrack({mock1.id})
    #     objSp.api.saveTrack({mock2.id})
    #     print("Tracks guardados")
    #     print("Mostrando datos (mostrara los de la bdd):\n")
    #     print(objSp.showMyPlaylist())
    #     print("\nMostrando datos (mostrara los de la spotify):\n")
    #     print(objSp.api.printPlaylist(objSp.api.getTrackslistfromSpotify()))
    #     self.assertEqual(objSp.makeSync(),0)
    #     print("\n(Sincronizados) Mostrando datos (mostrara los de la bdd):\n")
    #     stridsbdd=objSp.api.printPlaylist(objSp.bdd.getIDSFromDB(objSp.bdd.getPlaylistFromDB()))
    #     print(stridsbdd)
    #     print("assert ...")
    #     expect=""
    #     expect+="{ID: 0 08jkW1RWXUwKA3W0bqWGuU}\n"
    #     expect+="{ID: 1 58MZs0B5Amxl0Mwc9FIRZc}"
    #
    #     print("TESTCASE DATOS SOLO EN SPOTIFY  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>><<< TESTCASE")
    #
    #     objSp.deleteAllTracks()
    #     print("Playlist y bdd listas")
    #
    #     objSp.api.saveTrack({mock1.id})
    #     objSp.api.saveTrack({mock2.id})
    #     print("Tracks guardados")
    #     print("Mostrando datos (mostrara los de la bdd):\n")
    #     print(objSp.showMyPlaylist())
    #     print("\nMostrando datos (mostrara los de la spotify):\n")
    #     print(objSp.api.printPlaylist(objSp.api.getTrackslistfromSpotify()))
    #     self.assertEqual(objSp.makeSync(),0)
    #     print("\n(Sincronizados) Mostrando datos (mostrara los de la bdd):\n")
    #     stridsbdd=objSp.api.printPlaylist(objSp.bdd.getIDSFromDB(objSp.bdd.getPlaylistFromDB()))
    #     print(stridsbdd)
    #     print("assert ...")
    #     expect=""
    #     expect+="{ID: 0 08jkW1RWXUwKA3W0bqWGuU}\n"
    #     expect+="{ID: 1 58MZs0B5Amxl0Mwc9FIRZc}"
    #
    #     print("TESTCASE  MAS DATOS EN SPOTIFY  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>><<< TESTCASE")
    #
    #     objSp.deleteAllTracks()
    #     print("Playlist y bdd listas\n")
    #
    #     objSp.api.saveTrack({mock1.id})
    #     objSp.api.saveTrack({mock2.id})
    #     objSp.api.saveTrack({mock3.id})
    #     objSp.bdd.saveTrack(mock4)
    #     print("Tracks guardados")
    #     print("Mostrando datos (mostrara los de la bdd):\n")
    #     print(objSp.showMyPlaylist())
    #     print("\nMostrando datos (mostrara los de la spotify):\n")
    #     print(objSp.api.printPlaylist(objSp.api.getTrackslistfromSpotify()))
    #     print("assert ...")
    #     self.assertEqual(objSp.makeSync(),0)
    #     print("\n(Sincronizados) Mostrando datos (mostrara los de la bdd):\n")
    #     stridsbdd=objSp.api.printPlaylist(objSp.bdd.getIDSFromDB(objSp.bdd.getPlaylistFromDB()))
    #     print(">>>> ",stridsbdd,"<<<<<<")
    #     expect=""
    #     expect+="{ID: 0 08jkW1RWXUwKA3W0bqWGuU}\n"
    #     expect+="{ID: 1 504jTZvXdP8YYVtd19rfuX}\n"
    #     expect+="{ID: 2 7I708EIVfgOpcv6ltbXwbm}\n"
    #     expect+="{ID: 3 58MZs0B5Amxl0Mwc9FIRZc}"
    #     self.assertEqual(stridsbdd,expect)
    #
    #     print("TESTCASE  MAS DATOS EN BDD  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>><<< TESTCASE")
    #
    #     objSp.deleteAllTracks()
    #     print("Playlist y bdd listas\n")
    #
    #     objSp.bdd.saveTrack(mock1)
    #     objSp.bdd.saveTrack(mock2)
    #     objSp.bdd.saveTrack(mock3)
    #     objSp.api.saveTrack({mock4.id})
    #     print("Tracks guardados")
    #     print("Mostrando datos (mostrara los de la bdd):\n")
    #     print(objSp.showMyPlaylist())
    #     print("\nMostrando datos (mostrara los de la spotify):\n")
    #     print(objSp.api.printPlaylist(objSp.api.getTrackslistfromSpotify()))
    #     print("assert ...")
    #     self.assertEqual(objSp.makeSync(),0)
    #     print("\n(Sincronizados) Mostrando datos (mostrara los de la playlist):\n")
    #     stridsbdd=objSp.api.printPlaylist(objSp.api.getPlaylistsIDSfromSpotify())
    #     print(">>>> ",stridsbdd,"<<<<<<")
    #     expect=""
    #     expect+="{ID: 0 08jkW1RWXUwKA3W0bqWGuU}\n"
    #     expect+="{ID: 1 504jTZvXdP8YYVtd19rfuX}\n"
    #     expect+="{ID: 2 7I708EIVfgOpcv6ltbXwbm}\n"
    #     expect+="{ID: 3 58MZs0B5Amxl0Mwc9FIRZc}"
    #     self.assertEqual(stridsbdd,expect)
    #
    #     print("TESTCASE MISMA CANTIDAD DIFERENTE ORDEN  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>><<< TESTCASE")
    #
    #     objSp.deleteAllTracks()
    #     # print("Playlist y bdd listas\n")
    #
    #     objSp.bdd.saveTrack(mock1)
    #     objSp.bdd.saveTrack(mock2)
    #     objSp.bdd.saveTrack(mock3)
    #     objSp.api.saveTrack({mock3.id})
    #     objSp.api.saveTrack({mock2.id})
    #     objSp.api.saveTrack({mock1.id})
    #     print("Tracks guardados")
    #     print("Mostrando datos (mostrara los de la bdd):\n")
    #     print(objSp.showMyPlaylist())
    #     print("\nMostrando datos (mostrara los de la spotify):\n")
    #     print(objSp.api.printPlaylist(objSp.api.getTrackslistfromSpotify()))
    #     print("assert ...")
    #     self.assertEqual(objSp.makeSync(),0)
    #     print("\n(Sincronizados) Mostrando datos (mostrara los de la playlist):\n")
    #     stridsbdd=objSp.api.printPlaylist(objSp.api.getPlaylistsIDSfromSpotify())
    #     print(">>>> ",stridsbdd,"<<<<<<")
    #     expect=""
    #     expect+="{ID: 0 08jkW1RWXUwKA3W0bqWGuU}\n"
    #     expect+="{ID: 1 504jTZvXdP8YYVtd19rfuX}\n"
    #     expect+="{ID: 2 58MZs0B5Amxl0Mwc9FIRZc}"
    #     self.assertEqual(stridsbdd,expect)
    #     print("TESTCASE MISMA CANTIDAD IGUALES HASTA LA MITAD INFERIOR  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>><<< TESTCASE")
    #
    #     objSp.deleteAllTracks()
    #     # print("Playlist y bdd listas\n")
    #
    #     objSp.bdd.saveTrack(mock1)
    #     objSp.bdd.saveTrack(mock2)
    #     objSp.bdd.saveTrack(mock3)
    #     objSp.bdd.saveTrack(mock4)
    #     objSp.api.saveTrack({mock1.id})
    #     objSp.api.saveTrack({mock2.id})
    #     objSp.api.saveTrack({mock4.id})
    #     objSp.api.saveTrack({mock3.id})
    #     print("Tracks guardados")
    #     print("Mostrando datos (mostrara los de la bdd):\n")
    #     print(objSp.showMyPlaylist())
    #     print("\nMostrando datos (mostrara los de la spotify):\n")
    #     print(objSp.api.printPlaylist(objSp.api.getTrackslistfromSpotify()))
    #     print("assert ...")
    #     self.assertEqual(objSp.makeSync(),0)
    #     print("\n(Sincronizados) Mostrando datos (mostrara los de la playlist):\n")
    #     stridsbdd=objSp.api.printPlaylist(objSp.api.getPlaylistsIDSfromSpotify())
    #     print(">>>> ",stridsbdd,"<<<<<<")
    #     expect=""
    #     expect+="{ID: 0 08jkW1RWXUwKA3W0bqWGuU}\n"
    #     expect+="{ID: 1 504jTZvXdP8YYVtd19rfuX}\n"
    #     expect+="{ID: 2 7I708EIVfgOpcv6ltbXwbm}\n"
    #     expect+="{ID: 3 58MZs0B5Amxl0Mwc9FIRZc}"
    #     self.assertEqual(stridsbdd,expect)
    #
    #     print("TESTCASE MISMA CANTIDAD IGUALES DESDE LA MITAD SUPERIOR  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>><<< TESTCASE")
    #
    #     objSp.deleteAllTracks()
    #     # print("Playlist y bdd listas\n")
    #
    #     objSp.bdd.saveTrack(mock1)
    #     objSp.bdd.saveTrack(mock3)
    #     objSp.bdd.saveTrack(mock1)
    #     objSp.bdd.saveTrack(mock4)
    #     objSp.api.saveTrack({mock4.id})
    #     objSp.api.saveTrack({mock2.id})
    #     objSp.api.saveTrack({mock1.id})
    #     objSp.api.saveTrack({mock4.id})
    #     print("Tracks guardados")
    #     print("Mostrando datos (mostrara los de la bdd):\n")
    #     print(objSp.showMyPlaylist())
    #     print("\nMostrando datos (mostrara los de la spotify):\n")
    #     print(objSp.api.printPlaylist(objSp.api.getTrackslistfromSpotify()))
    #     print("assert ...")
    #     self.assertEqual(objSp.makeSync(),0)
    #     print("\n(Sincronizados) Mostrando datos (mostrara los de la playlist):\n")
    #     stridsbdd=objSp.api.printPlaylist(objSp.api.getPlaylistsIDSfromSpotify())
    #     print(">>>> ",stridsbdd,"<<<<<<")
    #     expect=""
    #     expect+="{ID: 0 08jkW1RWXUwKA3W0bqWGuU}\n"
    #     expect+="{ID: 1 504jTZvXdP8YYVtd19rfuX}\n"
    #     expect+="{ID: 2 7I708EIVfgOpcv6ltbXwbm}\n"
    #     expect+="{ID: 3 58MZs0B5Amxl0Mwc9FIRZc}"
    #     self.assertEqual(stridsbdd,expect)
    #     print("TESTCASE DATOS INVALIDOS EN BASE DE DATOS  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>><<< TESTCASE")
    #
    #     objSp.deleteAllTracks()
    #     # print("Playlist y bdd listas\n")
    #
    #     objSp.bdd.saveTrack(mockFake1)
    #     objSp.bdd.saveTrack(mockFake2)
    #
    #     print("\nTracks guardados?")
    #     print("\nMostrando datos (mostrara los de la bdd):\n")
    #     print(objSp.showMyPlaylist())
    #
    #     print("\nMostrando datos (mostrara los de la spotify):\n")
    #     print(objSp.api.printPlaylist(objSp.api.getTrackslistfromSpotify()))
    #
    #     print("\nassert ...")
    #     self.assertEqual(objSp.makeSync(),0)#,0)
    #
    #     print("\n(Sincronizados) Mostrando datos (mostrara los de la playlist):\n")
    #     stridsapi=objSp.api.printPlaylist(objSp.api.getPlaylistsIDSfromSpotify())
    #     print(">>>> ",stridsapi,"<<<<<<")
    #
    #     print("\n(Sincronizados) Mostrando datos (mostrara los de la bdd):\n")
    #     stridsbdd=objSp.api.printPlaylist(objSp.bdd.getIDSFromDB(objSp.bdd.getPlaylistFromDB()))
    #     print(">>>> ",stridsbdd,"<<<<<<")
    #     self.assertEqual(stridsapi,1) #


if __name__ == '__main__':
    unittest.main()
