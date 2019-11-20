import sys
sys.path.append('../')
import unittest
import Track
import mock
from mock import patch
from SPYClass import APISFY
from SPYClass import DBSFY
from SPYClass import sinchronize
import sqlite3



#***********************************************************************************************************************************************************
#*          >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> PRUEAS UNITARIAS A CLASE APISFY <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<                   *
#***********************************************************************************************************************************************************

class testSpotipy(unittest.TestCase):
#     #ahique vaciar la biblioteca en cada ejecucion
#
    # def test_readCredentials(self):
    #     mock=["username: 32hzoj7ckzb2dgudlq5zfbudzoia","clientId: 005e25714bad49ab93e394adeabaaa96","clientSecret: 087a97142beb44a18e818424ae2b444c","scope: user-library-read playlist-read-private user-top-read playlist-modify-public","redirect: http://google.com/"]
    #     #print(mock)
    #     api=APISFY()
    #     r=api.readCredentials(mock)
    #     self.assertEqual(r[0],'32hzoj7ckzb2dgudlq5zfbudzoia')

    # #
    # def test_saveTrack(self):
    #     class Mock_Track:
    #         def __init__(self,uri_track, name, artist, album, duration):
    #             self.uri_track = uri_track
    #             self.name = name
    #             self.artist = artist
    #             self.album = album
    #             self.duration = duration
    #     mock_ids=['58MZs0B5Amxl0Mwc9FIRZc']#, '64Mgiyn0JSji95v7QEOv4U'
    #     api=APISFY()
    #     # api.deleteTrack(mock_ids)
    #     self.assertEqual(0,api.saveTrack(mock_ids))

    # def test_getTrackfromSpotify(self):
    #     # # CASO DE PRUEBA: cancion y artist correctos***************************** <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< TEST CASE
    #     track = 'Dare'
    #     artist = 'Gorillaz'
    #     #esp = 'El track es: DARE - Soulwax Remix de Gorillaz del album D-Sides'
    #     a=APISFY()
    #     res = a.getTrackfromSpotify(track, artist)
    #     #self.assertEqual(res, esp)
    #     print(res)


    # def test_getPlaylistsIDSfromSpotify(self):
    #     play=[]
    #     a=APISFY()
    #     play=a.getPlaylistsIDSfromSpotify()
    #     print(play)
    #
    # def test_getTrackListFromSpotify(self):
    #     api=APISFY()
    #     print(api.getTrackslistfromSpotify())
    #
    # def test_printPlaylistfrom(self):
    #     # # CASO DE PRUEBA: playlist vacia **************************************** <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< TEST CASE
    #     # guardar unos dos tracks, obtenerlos y luego mostrarlos
    #     # mock de clase track
    #     class Mock_Track:
    #         def __init__(self,uri_track, name, artist, album, duration):
    #             self.uri_track = uri_track
    #             self.name = name
    #             self.artist = artist
    #             self.album = album
    #             self.duration = duration
    #     objBDD=DBSFY('Arma_tu_biblio.db')
    #     objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
    #     objTrack=Mock_Track('58MZs0B5Amxl0Mwc9FIRZc','DARE - Junior Sanchez Remix','Gorillaz','D-Sides [Special Edition]', 326373)
    #     objBDD.saveTrack(objTrack)
    #     objTrack=Mock_Track('6TY7U0B5Amxl0Mwc9F1234','Una cancion','El artista','Mejor album', 387373)
    #     objBDD.saveTrack(objTrack)
    #     playlist=objBDD.getPlaylistFromDB()
    #     a=APISFY()
    #     print(a.printPlaylist(playlist))
    #     a=None
    #     objeBDD=None
    #     objTrack=None
    #     playlist=None
    # #
    # #     #aqui se obtendra un track por id
    #     def test_getTrackfromPlaylistWithID(self):
    #     # # CASO DE PRUEBA: playlist vacia **************************************** <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< TEST CASE
    #     # guardar unos dos tracks, obtenerlos y luego mostrarlos
    #     # mock de clase track
    #         class Mock_Track:
    #             def __init__(self,uri_track, name, artist, album, duration):
    #                 self.uri_track = uri_track
    #                 self.name = name
    #                 self.artist = artist
    #                 self.album = album
    #                 self.duration = duration
    #         objBDD=DBSFY('Arma_tu_biblio.db')
    #         objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
    #         objTrack=Mock_Track('58MZs0B5Amxl0Mwc9FIRZc','DARE - Junior Sanchez Remix','Gorillaz','D-Sides [Special Edition]', 326373)
    #         objBDD.saveTrack(objTrack)
    #         objTrack=Mock_Track('6TY7U0B5Amxl0Mwc9F1234','Una cancion','El artista','Mejor album', 387373)
    #         objBDD.saveTrack(objTrack)
    #         playlist=objBDD.getPlaylistFromDB()
    #         a=APISFY()
    #
    #         print(a.getTrackfromPlaylistWithID(playlist,0))
    #         a=None
    #         objeBDD=None
    #         objTrack=None
    #         playlist=None

    # def test_deleteTrack(self):
    #     api=APISFY()
    #     ids=['58MZs0B5Amxl0Mwc9FIRZc']
    #     self.assertEqual(0,api.deleteTrack(ids))

#***********************************************************************************************************************************************************
#*          >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> PRUEAS UNITARIAS A CLASE DBSFY <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<                    *
#***********************************************************************************************************************************************************
    # def test_saveTrack(self):
    #     # prueba de guardar un track correctamente _/
    #     # un track raro, tracks iguales _/,track malo
    #     # track nulo _/ ,
    #     # la base de datos no existe o no coinciden tablas o atributos
    #     # revisar la salida y labase de datos para asserts
    #     #
    #     # mock de clase track
    #     class Mock_Track:
    #         def __init__(self,uri_track, name, artist, album, duration):
    #             self.uri_track = uri_track
    #             self.name = name
    #             self.artist = artist
    #             self.album = album
    #             self.duration = duration
    #
    #     objBDD=DBSFY('Arma_tu_biblio.db')
    #
    #     # CASO DE PRUEBA: UN TRACK CORRECTO **************************************** <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< TEST CASE
    #     objTrack=Mock_Track('58MZs0B5Amxl0Mwc9FIRZc','DARE - Junior Sanchez Remix','Gorillaz','D-Sides [Special Edition]', 326373)
    #     objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
    #     objBDD.saveTrack(objTrack)
    #     #a=objBDD.getPlaylistFromDB()
        #print(a[0].__str__())
        #self.assertEqual((a[0]).__str__(),"[58MZs0B5Amxl0Mwc9FIRZc, de DARE - Junior Sanchez Remix,Gorillaz, D-Sides [Special Edition], 326373]")

        # #CASO DE PRUEBA DE UN TRACK NULO **************************************** <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< TEST CASE
        # print("TEST CASE: TRACK NULO")
        # objTrack=None
        # objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        # a=objBDD.saveTrack(objTrack)
        # self.assertEqual(a,1)

        # #CASO DE PRUEA: EL TRACK  YA EXISTE **************************************** <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< TEST CASE
        # print("TEST CASE: EL TRACK YA EXISTE")
        # printer=APISFY()
        # objTrack=Mock_Track('58MZs0B5Amxl0Mwc9FIRZc','DARE - Junior Sanchez Remix','Gorillaz','D-Sides [Special Edition]', 326373)
        # objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        # a=objBDD.saveTrack(objTrack)
        # print(objTrack.uri_track, "guardado") if a==0 else print(objTrack.uri_track,"No guardado")
        # b=objBDD.saveTrack(objTrack)
        # print(objTrack.uri_track, "guardado") if b==0 else print(objTrack.uri_track,"No guardado")
        # self.assertEqual(a,0) # si se guarda la primera vez
        # self.assertEqual(b,1) # no se guarda la segunda vez
        # play=objBDD.getPlaylistFromDB()
        # m=printer.printPlaylist(play)
        # self.assertEqual(len(play),1)#validar que solo se haya guardado uno

        # CASOS DE PRUEBA: PRUEBAS A uri_track *************************************** <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< TEST CASES URI

        # print("TEST CASE: uri_track es ' ' ") #**************************************************************************
        # objTrack=Mock_Track(' ','DARE - Junior Sanchez Remix','Gorillaz','D-Sides [Special Edition]', 326373)
        # objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        # a=objBDD.saveTrack(objTrack)
        # print(objTrack.uri_track, "guardado") if a==0 else print(objTrack.uri_track,"No guardado")
        # self.assertEqual(a,1) # no lo guarda
        # objTrack= None
        #
        # print("TEST CASE: uri_track es '' ")  #**************************************************************************
        # objTrack=Mock_Track('AAAAAAAAAAAAAAAAAAAAAA','Cancion',' ','D-Sides [Special Edition]', 326373)
        # objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        # a=objBDD.saveTrack(objTrack)
        # print(objTrack.uri_track, "guardado") if a==0 else print(objTrack.uri_track,"No guardado")
        # self.assertEqual(a,1) # no lo guarda
        # objTrack=None
        #
        # print("TEST CASE: uri_track es None ") #**************************************************************************
        # objTrack=Mock_Track(None,'DARE - Junior Sanchez Remix','Gorillaz','D-Sides [Special Edition]', 326373)
        # objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        # a=objBDD.saveTrack(objTrack)
        # print(objTrack.uri_track, "guardado") if a==0 else print(objTrack.uri_track,"No guardado")
        # self.assertEqual(a,1) # no lo guarda
        # objTrack = None
        #
        # # continuar con string,float, zero pading, negatives, more than len and different
        # print("TEST CASE: uri_track es MAYOR A 22") #**********************************************************************
        # objTrack=Mock_Track('A'*23,'DARE - Junior Sanchez Remix','Gorillaz','D-Sides [Special Edition]', 326373)
        # objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        # a=objBDD.saveTrack(objTrack)
        # print(objTrack.uri_track, "guardado") if a==0 else print(objTrack.uri_track,"No guardado")
        # self.assertEqual(a,1) # no lo guarda
        # objTrack= None
        #
        # # caracteres no imprimibles y algunos especiales
        # print("TEST CASE: uri_track tiene caracteres especiales") #*******************************************************
        # objTrack=Mock_Track('@'*22,'DARE - Junior Sanchez Remix','Gorillaz','D-Sides [Special Edition]', 326373)
        # objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        # a=objBDD.saveTrack(objTrack)
        # print(objTrack.uri_track, "guardado") if a==0 else print(objTrack.uri_track,"No guardado")
        # self.assertEqual(a,1) # no lo guarda
        # objTrack=None
        #
        # #checar con float
        # print("TEST CASE: uri_track float") #*****************************************************************************
        # objTrack=Mock_Track(234567890123456789.00,'DARE - Junior Sanchez Remix','Gorillaz','D-Sides [Special Edition]', 326373)
        # objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        # a=objBDD.saveTrack(objTrack)
        # print(objTrack.uri_track, "guardado") if a==0 else print(objTrack.uri_track,"No guardado")
        # self.assertEqual(a,1) # no lo guarda
        # objTrack=None
        #
        # print("TEST CASE: uri_track tiene padding de ceros") #************************************************************
        # objTrack=Mock_Track(("0"*20)+"22",'DARE - Junior Sanchez Remix','Gorillaz','D-Sides [Special Edition]', 326373)
        # objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        # a=objBDD.saveTrack(objTrack)
        # print(objTrack.uri_track, "guardado") if a==0 else print(objTrack.uri_track,"No guardado")
        # self.assertEqual(a,0) # lo guarda
        # objTrack= None
        #
        # # CASOS DE PRUEBA: PRUEBAS A NAME *************************************** <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< TEST CASES NAME
        # print("TEST CASE: name es ' ' ")  #**************************************************************************
        # objTrack=Mock_Track('AAAAAAAAAAAAAAAAAAAAAA',' ','Gorillaz','D-Sides [Special Edition]', 326373)
        # objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        # a=objBDD.saveTrack(objTrack)
        # print(objTrack.uri_track, "guardado") if a==0 else print(objTrack.uri_track,"No guardado")
        # self.assertEqual(a,1) # no lo guarda
        # objTrack=None
        #
        # print("TEST CASE: Name es '' ")  #**************************************************************************
        # objTrack=Mock_Track('AAAAAAAAAAAAAAAAAAAAAA','Cancion','','D-Sides [Special Edition]', 326373)
        # objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        # a=objBDD.saveTrack(objTrack)
        # print(objTrack.uri_track, "guardado") if a==0 else print(objTrack.uri_track,"No guardado")
        # self.assertEqual(a,1) # no lo guarda
        # objTrack=None
        #
        # print("TEST CASE: name es None ")  #**************************************************************************
        # objTrack=Mock_Track('AAAAAAAAAAAAAAAAAAAAAA',None,'Gorillaz','D-Sides [Special Edition]', 326373)
        # objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        # a=objBDD.saveTrack(objTrack)
        # print(objTrack.uri_track, "guardado") if a==0 else print(objTrack.uri_track,"No guardado")
        # self.assertEqual(a,1) # no lo guarda
        # objTrack=None
        #
        # print("TEST CASE: name es MAYOR A 50") #**********************************************************************
        # objTrack=Mock_Track('AAAAAAAAAAAAAAAAAAAAAA',"B"*52,'Gorillaz','D-Sides [Special Edition]', 326373)
        # objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        # a=objBDD.saveTrack(objTrack)
        # print(objTrack.uri_track, "guardado") if a==0 else print(objTrack.uri_track,"No guardado")
        # self.assertEqual(a,1) # no lo guarda
        # objTrack=None
        #
        # print("TEST CASE: name tiene caracteres especiales") #*******************************************************
        # objTrack=Mock_Track('AAAAAAAAAAAAAAAAAAAAAA',"Dare",'Gorillaz','D-Sides [Special Edition]', 326373)
        # objTrack.name="@#$%%&/()="
        # objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        # a=objBDD.saveTrack(objTrack)
        # print(objTrack.uri_track, "guardado") if a==0 else print(objTrack.uri_track,"No guardado")
        # self.assertEqual(a,0) # lo guarda por que aun no se ha definido esta validacion
        # objTrack=None
        # # checar con int
        #
        # print("TEST CASE: name int como int") #*****************************************************************************
        # objTrack=Mock_Track('AAAAAAAAAAAAAAAAAAAAAA',1234,'Gorillaz','D-Sides [Special Edition]', 326373)
        # objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        # a=objBDD.saveTrack(objTrack)
        # print(objTrack.uri_track, "guardado") if a==0 else print(objTrack.uri_track,"No guardado")
        # self.assertEqual(a,1) # no lo guarda por que acepta solo strings
        # objTrack= None
        #
        # print("TEST CASE: name int como string") #***************************************************************************
        # objTrack=Mock_Track('AAAAAAAAAAAAAAAAAAAAAA',"1234",'Gorillaz','D-Sides [Special Edition]', 326373)
        # objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        # a=objBDD.saveTrack(objTrack)
        # print(objTrack.uri_track, "guardado") if a==0 else print(objTrack.uri_track,"No guardado")
        # self.assertEqual(a,0) # lo guarda por que esta como string
        # objTrack = None
        #
        # print("TEST CASE: name flaot como tal") #****************************************************************************
        # objTrack=Mock_Track('AAAAAAAAAAAAAAAAAAAAAA',1234.5,'Gorillaz','D-Sides [Special Edition]', 326373)
        # objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        # a=objBDD.saveTrack(objTrack)
        # print(objTrack.uri_track, "guardado") if a==0 else print(objTrack.uri_track,"No guardado")
        # self.assertEqual(a,1) # no lo guarda por que acepta solo strings
        # objTrack= None
        #
        # print("TEST CASE: name float como string") #***************************************************************************
        # objTrack=Mock_Track('AAAAAAAAAAAAAAAAAAAAAA',"1234.5",'Gorillaz','D-Sides [Special Edition]', 326373)
        # objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        # a=objBDD.saveTrack(objTrack)
        # print(objTrack.uri_track, "guardado") if a==0 else print(objTrack.uri_track,"No guardado")
        # self.assertEqual(a,0) # lo guarda por que esta como string
        # objTrack=None
        # # aun falta validar mas detalles, mas casos de prueba y mejorar el codigo
        #
        # #CASOS DE PRUEBA: PRUEBAS A ARITST *************************************** <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< TEST CASES ARTIST
        # print("TEST CASE: artist es ' ' ")  #**************************************************************************
        # objTrack=Mock_Track('AAAAAAAAAAAAAAAAAAAAAA','Cancion',' ','D-Sides [Special Edition]', 326373)
        # objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        # a=objBDD.saveTrack(objTrack)
        # print(objTrack.uri_track, "guardado") if a==0 else print(objTrack.uri_track,"No guardado")
        # self.assertEqual(a,1) # no lo guarda
        # objTrack=None
        #
        # print("TEST CASE: artist es '' ")  #**************************************************************************
        # objTrack=Mock_Track('AAAAAAAAAAAAAAAAAAAAAA','Cancion','','D-Sides [Special Edition]', 326373)
        # objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        # a=objBDD.saveTrack(objTrack)
        # print(objTrack.uri_track, "guardado") if a==0 else print(objTrack.uri_track,"No guardado")
        # self.assertEqual(a,1) # no lo guarda
        # objTrack=None
        #
        # print("TEST CASE: artist es None ")  #**************************************************************************
        # objTrack=Mock_Track('AAAAAAAAAAAAAAAAAAAAAA','Cancion',None,'D-Sides [Special Edition]', 326373)
        # objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        # a=objBDD.saveTrack(objTrack)
        # print(objTrack.uri_track, "guardado") if a==0 else print(objTrack.uri_track,"No guardado")
        # self.assertEqual(a,1) # no lo guarda
        # objTrack=None
        #
        # print("TEST CASE: artist es MAYOR A 50") #**********************************************************************
        # objTrack=Mock_Track('AAAAAAAAAAAAAAAAAAAAAA','Dare',"B"*52,'D-Sides [Special Edition]', 326373)
        # objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        # a=objBDD.saveTrack(objTrack)
        # print(objTrack.uri_track, "guardado") if a==0 else print(objTrack.uri_track,"No guardado")
        # self.assertEqual(a,1) # no lo guarda
        # objTrack=None
        #
        # print("TEST CASE: artist tiene caracteres especiales") #*******************************************************
        # objTrack=Mock_Track('AAAAAAAAAAAAAAAAAAAAAA',"Dare",'$#%&/=','D-Sides [Special Edition]', 326373)
        # objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        # a=objBDD.saveTrack(objTrack)
        # print(objTrack.uri_track, "guardado") if a==0 else print(objTrack.uri_track,"No guardado")
        # self.assertEqual(a,0) # lo guarda por que aun no se ha definido esta validacion
        # objTrack=None
        #
        # # # checar con int
        # print("TEST CASE: artist int como int") #*****************************************************************************
        # objTrack=Mock_Track('AAAAAAAAAAAAAAAAAAAAAA','Dare',1234,'D-Sides [Special Edition]', 326373)
        # objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        # a=objBDD.saveTrack(objTrack)
        # print(objTrack.uri_track, "guardado") if a==0 else print(objTrack.uri_track,"No guardado")
        # self.assertEqual(a,1) # no lo guarda por que acepta solo strings
        # objTrack= None
        #
        # print("TEST CASE: artist int como string") #***************************************************************************
        # objTrack=Mock_Track('AAAAAAAAAAAAAAAAAAAAAA',"Dare",'1234','D-Sides [Special Edition]', 326373)
        # objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        # a=objBDD.saveTrack(objTrack)
        # print(objTrack.uri_track, "guardado") if a==0 else print(objTrack.uri_track,"No guardado")
        # self.assertEqual(a,0) # lo guarda por que esta como string
        # objTrack = None
        #
        # print("TEST CASE: artist flaot como tal") #****************************************************************************
        # objTrack=Mock_Track('AAAAAAAAAAAAAAAAAAAAAA','Dare',1234.5,'D-Sides [Special Edition]', 326373)
        # objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        # a=objBDD.saveTrack(objTrack)
        # print(objTrack.uri_track, "guardado") if a==0 else print(objTrack.uri_track,"No guardado")
        # self.assertEqual(a,1) # no lo guarda por que acepta solo strings
        # objTrack= None
        #
        # print("TEST CASE: artist float como string") #***************************************************************************
        # objTrack=Mock_Track('AAAAAAAAAAAAAAAAAAAAAA',"Dare",'1234.5','D-Sides [Special Edition]', 326373)
        # objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        # a=objBDD.saveTrack(objTrack)
        # print(objTrack.uri_track, "guardado") if a==0 else print(objTrack.uri_track,"No guardado")
        # self.assertEqual(a,0) # lo guarda por que esta como string
        # objTrack=None
        # #aun falta validar mas detalles, mas casos de prueba y mejorar el codigo
        #
        # # CASOS DE PRUEBA: PRUEBAS A ALBUM *************************************** <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< TEST CASES album
        # print("TEST CASE: album es ' ' ")  #**************************************************************************
        # objTrack=Mock_Track('AAAAAAAAAAAAAAAAAAAAAA','Cancion','Gorillaz',' ', 326373)
        # objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        # a=objBDD.saveTrack(objTrack)
        # print(objTrack.uri_track, "guardado") if a==0 else print(objTrack.uri_track,"No guardado")
        # self.assertEqual(a,1) # no lo guarda
        # objTrack=None
        #
        # print("TEST CASE: album es '' ")  #**************************************************************************
        # objTrack=Mock_Track('AAAAAAAAAAAAAAAAAAAAAA','Cancion','Gorillaz','', 326373)
        # objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        # a=objBDD.saveTrack(objTrack)
        # print(objTrack.uri_track, "guardado") if a==0 else print(objTrack.uri_track,"No guardado")
        # self.assertEqual(a,1) # no lo guarda
        # objTrack=None
        #
        # print("TEST CASE: album es None ")  #**************************************************************************
        # objTrack=Mock_Track('AAAAAAAAAAAAAAAAAAAAAA','Cancion',"Gorillaz",None, 326373)
        # objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        # a=objBDD.saveTrack(objTrack)
        # print(objTrack.uri_track, "guardado") if a==0 else print(objTrack.uri_track,"No guardado")
        # self.assertEqual(a,1) # no lo guarda
        # objTrack=None
        #
        # print("TEST CASE: album es MAYOR A 50") #**********************************************************************
        # objTrack=Mock_Track('AAAAAAAAAAAAAAAAAAAAAA','Dare',"Gorillaz",'B'*52, 326373)
        # objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        # a=objBDD.saveTrack(objTrack)
        # print(objTrack.uri_track, "guardado") if a==0 else print(objTrack.uri_track,"No guardado")
        # self.assertEqual(a,1) # no lo guarda
        # objTrack=None
        #
        # print("TEST CASE: album tiene caracteres especiales") #*******************************************************
        # objTrack=Mock_Track('AAAAAAAAAAAAAAAAAAAAAA',"Dare",'Gorillaz','D-Sides [Special Edition]', 326373)
        # objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        # a=objBDD.saveTrack(objTrack)
        # print(objTrack.uri_track, "guardado") if a==0 else print(objTrack.uri_track,"No guardado")
        # self.assertEqual(a,0) # lo guarda por que aun no se ha definido esta validacion
        # objTrack=None
        #
        # # # checar con int
        # print("TEST CASE: album int como int") #*****************************************************************************
        # objTrack=Mock_Track('AAAAAAAAAAAAAAAAAAAAAA','Dare',"Gorillaz",1234, 326373)
        # objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        # a=objBDD.saveTrack(objTrack)
        # print(objTrack.uri_track, "guardado") if a==0 else print(objTrack.uri_track,"No guardado")
        # self.assertEqual(a,1) # no lo guarda por que acepta solo strings
        # objTrack= None
        #
        # print("TEST CASE: album int como string") #***************************************************************************
        # objTrack=Mock_Track('AAAAAAAAAAAAAAAAAAAAAA',"Dare","Gorillaz",'1234', 326373)
        # objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        # a=objBDD.saveTrack(objTrack)
        # print(objTrack.uri_track, "guardado") if a==0 else print(objTrack.uri_track,"No guardado")
        # self.assertEqual(a,0) # lo guarda por que esta como string
        # objTrack = None
        #
        # print("TEST CASE: album flaot como tal") #****************************************************************************
        # objTrack=Mock_Track('AAAAAAAAAAAAAAAAAAAAAA','Dare',"Gorillaz",1234.5, 326373)
        # objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        # a=objBDD.saveTrack(objTrack)
        # print(objTrack.uri_track, "guardado") if a==0 else print(objTrack.uri_track,"No guardado")
        # self.assertEqual(a,1) # no lo guarda por que acepta solo strings
        # objTrack= None
        #
        # print("TEST CASE: album float como string") #***************************************************************************
        # objTrack=Mock_Track('AAAAAAAAAAAAAAAAAAAAAA',"Dare",'Gorillaz','1234.5', 326373)
        # objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        # a=objBDD.saveTrack(objTrack)
        # print(objTrack.uri_track, "guardado") if a==0 else print(objTrack.uri_track,"No guardado")
        # self.assertEqual(a,0) # lo guarda por que esta como string
        # objTrack=None
        # # aun falta validar mas detalles, mas casos de prueba y mejorar el codigo
        #
        #
        # #CASOS DE PRUEBA: PRUEBAS A DURATION *************************************** <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< TEST CASES DURATION
        # print("TEST CASE: duration es ' ' ")  #**************************************************************************
        # objTrack=Mock_Track('AAAAAAAAAAAAAAAAAAAAAA','Cancion','Gorillaz','D-Sides [Special Edition]', ' ' )
        # objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        # a=objBDD.saveTrack(objTrack)
        # print(objTrack.uri_track, "guardado") if a==0 else print(objTrack.uri_track,"No guardado")
        # self.assertEqual(a,1) # no lo guarda
        # objTrack=None
        #
        # print("TEST CASE: duration es '' ")  #**************************************************************************
        # objTrack=Mock_Track('AAAAAAAAAAAAAAAAAAAAAA','Cancion','Gorillaz','D-Sides [Special Edition]', '')
        # objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        # a=objBDD.saveTrack(objTrack)
        # print(objTrack.uri_track, "guardado") if a==0 else print(objTrack.uri_track,"No guardado")
        # self.assertEqual(a,1) # no lo guarda
        # objTrack=None
        #
        # print("TEST CASE: duration es None ")  #**************************************************************************
        # objTrack=Mock_Track('AAAAAAAAAAAAAAAAAAAAAA','Cancion',"Gorillaz",'D-Sides [Special Edition]', None)
        # objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        # a=objBDD.saveTrack(objTrack)
        # print(objTrack.uri_track, "guardado") if a==0 else print(objTrack.uri_track,"No guardado")
        # self.assertEqual(a,1) # no lo guarda
        # objTrack=None
        #
        # print("TEST CASE: duration es string") #**********************************************************************
        # objTrack=Mock_Track('AAAAAAAAAAAAAAAAAAAAAA','Dare',"Gorillaz",'D-Sides [Special Edition]', "Esto es una cadena")
        # objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        # a=objBDD.saveTrack(objTrack)
        # print(objTrack.uri_track, "guardado") if a==0 else print(objTrack.uri_track,"No guardado")
        # self.assertEqual(a,1) # no lo guarda
        # objTrack=None
        #
        # print("TEST CASE: duration mayor a 2147483647") #*******************************************************
        # objTrack=Mock_Track('AAAAAAAAAAAAAAAAAAAAAA',"Dare",'Gorillaz','D-Sides [Special Edition]', 2147483647+3)
        # objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        # a=objBDD.saveTrack(objTrack)
        # print(objTrack.uri_track, "guardado") if a==0 else print(objTrack.uri_track,"No guardado")
        # self.assertEqual(a,1) # no guarda
        # objTrack=None
        #
        # # # checar con int
        # print("TEST CASE: duration es 0") #*****************************************************************************
        # objTrack=Mock_Track('AAAAAAAAAAAAAAAAAAAAAA','Dare',"Gorillaz",'D-Sides [Special Edition]', 0)
        # objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        # a=objBDD.saveTrack(objTrack)
        # print(objTrack.uri_track, "guardado") if a==0 else print(objTrack.uri_track,"No guardado")
        # self.assertEqual(a,1) # no lo guarda por que acepta solo strings
        # objTrack= None
        #
        # print("TEST CASE: duration es negativo") #***************************************************************************
        # objTrack=Mock_Track('AAAAAAAAAAAAAAAAAAAAAA',"Dare","Gorillaz",'D-Sides [Special Edition]', -1)
        # objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        # a=objBDD.saveTrack(objTrack)
        # print(objTrack.uri_track, "guardado") if a==0 else print(objTrack.uri_track,"No guardado")
        # self.assertEqual(a,1) # no lo guarda
        # objTrack = None
        #
        # print("TEST CASE: duration flaot") #****************************************************************************
        # objTrack=Mock_Track('AAAAAAAAAAAAAAAAAAAAAA','Dare',"Gorillaz",'D-Sides [Special Edition]', 326373.5)
        # objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        # a=objBDD.saveTrack(objTrack)
        # print(objTrack.uri_track, "guardado") if a==0 else print(objTrack.uri_track,"No guardado")
        # self.assertEqual(a,1) # no lo guarda por que acepta solo strings
        # objTrack= None
        #
        # print("TEST CASE: duration float como double") #***************************************************************************
        # objTrack=Mock_Track('AAAAAAAAAAAAAAAAAAAAAA',"Dare",'Gorillaz','D-Sides [Special Edition]', 326373.15)
        # objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        # a=objBDD.saveTrack(objTrack)
        # print(objTrack.uri_track, "guardado") if a==0 else print(objTrack.uri_track,"No guardado")
        # self.assertEqual(a,1) # no lo guarda
        # objTrack=None
        # aun falta validar mas detalles, mas casos de prueba y mejorar el codigo
    #
    # def test_deleteTrack(self):
    #     # aqui se probara solo el nombre
    #     # ahi que revisar primero que exista
    #     # prueba borrar track existente
    #     # borrar track que no existente
    #     # intentos de inyeccion
    #     # la base de datos no existe o no coinciden tablas o atributos
    #
    #

    # def test_getPlaylisrFromDB(self):
    # #revisar que pasa cuando no tienes nada en la labase
    #     obj=DBSFY('Arma_tu_biblio.db')
    #     showTracks = obj.getPlaylistFromDB()
    #     for x in showTracks:
    #         print(x)

    # def test_deleteAllTracks(self):
    #     obj=DBSFY('Arma_tu_biblio.db')
    #     showTracks = obj.getPlaylistFromDB()
    #
    #     if(type(showTracks)=="List"):
    #         for x in showTracks:
    #             print("x")
    #         print("Borrando todo...")
    #         obj.deleteAllTracks()
    #     else:
    #      print("Error")


    # def test_getIDSfromDB(self):
    #     class Mock_Track:
    #         def __init__(self,uri_track, name, artist, album, duration):
    #             self.uri_track = uri_track
    #             self.name = name
    #             self.artist = artist
    #             self.album = album
    #             self.duration = duration
    #     obj=DBSFY('Arma_tu_biblio.db')
    #     try:
    #         obj.deleteAllTracks()
    #     except:
    #         return 1
    #     mock1=Mock_Track('AAAAAAAAAAAAAAAAAAAAAA',"Dare",'Gorillaz','D-Sides [Special Edition]', 326373123)
    #     mock2=Mock_Track('BBBBBBBBBBBBBBBBBBBBBB',"Get Lucky",'Daft Punk','Album Daft-Punk', 326373123)
    #     obj.saveTrack(mock1)
    #     obj.saveTrack(mock2)
    #     playlist=obj.getPlaylistFromDB()
    #     r=['AAAAAAAAAAAAAAAAAAAAAA','BBBBBBBBBBBBBBBBBBBBBB']
    #     self.assertEqual(obj.getIDSFromDB(playlist),r)




#***********************************************************************************************************************************************************
#*          >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> PRUEAS UNITARIAS A CLASE SINCHRONIZE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<                    *
#***********************************************************************************************************************************************************

    # def test_checkBDDvsSpotify(self):
    #     id_prueba1='58MZs0B5Amxl0Mwc9FIRZc'
    #     id_prueba2='64Mgiyn0JSji95v7QEOv4U'
    #     a=APISFY()
    #     s=sinchronize()
    #     #d=DBSFY("./../Arma_tu_biblio.db")
    #     #idsSp=a.getPlaylistfromSpotify()
    #     idsSp=[id_prueba1,id_prueba2]#d.getPlaylistFromDB()
    #     idsBDD=[id_prueba1,id_prueba2]
    #     print (idsBDD)
    #     print(idsSp)
    #     print(s.checkBDDvsSpotify(idsSp,idsBDD))

    def test_updateBDDfromSpotify(self):
        #eliminar todo de mi playlist
        #eliminar todo de mi base de datos
        #subir dos tracks a spotify
        #revisar que se hayn subido
        #sinchronize
        #assert
        pass

    def test_updateSpotifyfromBDD(self):
        #eliminar todo de mi playlist
        #liminar todo de mi bdd
        #subimos 2 tracaks a la bdd
        #revisar que se hayan subido
        #sinchronize
        #assert
        pass
    #a los otros 2

if __name__ == '__main__':
    unittest.main()
