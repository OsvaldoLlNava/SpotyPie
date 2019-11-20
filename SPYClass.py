import sqlite3
import spotipy
import spotipy.util as util
from Track import Track

class APISFY():
    sp=None
    def __init__(self):
        #credentials.append()
        archivo=open("credenciales.txt",'r')
        scope="playlist-modify-private playlist-modify-public user-library-read user-library-modify user-read-private playlist-read-private user-top-read"
        credentials=self.readCredentials(archivo)
        token = util.prompt_for_user_token(
            username=credentials[0],
            scope=scope,
            client_id=credentials[1],
            client_secret=credentials[2],
            redirect_uri=credentials[4])
        self.sp = spotipy.Spotify(auth=token)
        archivo.close()

    def readCredentials(self,archivo):
        credenciales = []
        for linea in archivo:
            cadena = ''
            espacio = 0
            texto = str(linea).strip()
            for i in range(0,len(texto)):
                if texto[i] == ' ':
                    espacio +=1
                if espacio == 1 and texto[i] != ' ':
                    cadena += texto[i]

            credenciales.append(cadena)
        return credenciales

    def saveTrack(self,idtrackList):
        try:
            self.sp.current_user_saved_tracks_add(idtrackList)  # Guarda en biblioteca
            print("Tracks agregados")
            return 0
        except:
            print("Error in save track")
            return 1

    def getTrackfromSpotify(self, song,artist): #busca en spotify
        try:
            self.sp.trace = False
            results = self.sp.search(q='artist:' + artist + ' track:' + song)
            #print(results['tracks']['items'])
            if len(results['tracks']['items'])!=0:
                #print(results)
                for track in results['tracks']['items']:
                    id_track = track['id']
                    name = track['name']
                    artist = track['artists'][0]['name']
                    album = track['album']['name']
                    duration = track['duration_ms']
                objectTrack = Track(id_track,name,artist,album,duration)
                return objectTrack #regresa el objeto track
        except:
            print ("Can't find the song")
            return 1

    def getPlaylistsIDSfromSpotify(self): #obtener mi playlist desde spotify, devuelve ids
        lib = self.sp.current_user_saved_tracks()
        playlistids=[]
        for track in lib['items']:
            playlistids.append((track['track']['id']))
        return playlistids

    def getTrackslistfromSpotify(self): #obtener mi playlist desde spotify, devuelve obj tracks
        lib = self.sp.current_user_saved_tracks()
        playlist=[]
        for track in lib['items']:
            id_track = track['id']
            name = track['name']
            artist = track['artists'][0]['name']
            album = track['album']['name']
            duration = track['duration_ms']
            playlist.append(Track(id_track,name,artist,album,duration))
        return playlist

    def printPlaylist(self,playlist): #imprimir playlist desde la bdd
        if len(playlist)<1:
            print("Nada en tu Playlist")
            return 1
        play_String=""
        i=0
        for t in playlist:
            if i==len(playlist)-1:
                play_String+="{ID: "+str(i)+" "+str(t)+"}"
            else:
                play_String+="{ID: "+str(i)+" "+str(t)+"}\n"
                i=i+1
        return play_String

#get track from spotify with id
    def getTrackfromPlaylistWithID(self,playlist,id):
        if playlist == None or id== None or len(playlist)<1 or id>len(playlist)-1:
            return 1
        return playlist[id]

    def deleteTrack(self,ids):
        try:
            self.sp.current_user_saved_tracks_delete(ids)
            print("Track Eliminado")
            return 0
        except:
            print("Error in delete")
            return 1

#
#
#
class DBSFY():# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////DBSFY

    cur=None
    con=None
    def __init__(self, archivo):
        try:
            self.con = sqlite3.connect(archivo)
            self.cur = self.con.cursor()
            self.cur.execute('''CREATE TABLE IF NOT EXISTS Track
            (ID Text,
            Name TeSxt,
            Artist Text,
            Album Text,
            Duration Text
            )
            ''')
            self.con.commit()
        except:
            print("Error en constructor")
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< GUARDARTRACK

    def saveTrack(self, Track):
        #Primero revisemos los elementos de track,la estructurra del objeto track y las conexiones
        # print ("[DEBUG 'Track.uri_track'] ",Track.uri_track)
        # print ("[DEBUG 'Track.name'] ",Track.name)
        # print ("[DEBUG 'Track.artist'] ",Track.artist)
        # print ("[DEBUG 'Track.album'] ",Track.album)
        # print ("[DEBUG 'Track.duration'] ",Track.duration)
        #validar uri
        if Track==None:
            print("Track is null")
            return 1

        if (not isinstance(Track.uri_track, str)) or Track.uri_track==(" " or "")  or Track.uri_track==None or len(Track.uri_track)==0  or len(Track.uri_track)!=22 :
            print("Error en uri_track [if]", Track.uri_track)
            return 1
        for x in Track.uri_track:
            if not (x.isnumeric() or x.isalpha()):
                print("Error en uri_track tiene caracteres especiales")
                return 1
        #validar name
        if (not isinstance(Track.name, str)) or Track.name==None or Track.name==" " or Track.name=="" or (len(Track.name)>50):
            print("Error en name ", Track.name)
            return 1
        #aqui es la validacion de caracteres maliciosos y sql iny.(pendiente)

        # #validar artista
        if (not isinstance(Track.artist, str)) or Track.artist==None or Track.artist==" " or Track.artist=="" or (len(Track.artist)>50):
            print("Error en artist ", Track.artist)
            return 1
        #aqui es la validacion de caracteres maliciosos y sql iny.(pendiente, tambien decidir si metemos las validaciones en metodos)

        #validar album
        if (not isinstance(Track.album, str)) or Track.album==None or Track.album==" " or Track.album=="" or (len(Track.album)>50):
            print("Error en album ", Track.album)
            return 1
        #aqui es la validacion de caracteres maliciosos y sql iny.(pendiente)

        #
        # #validar duracion
        if (not (isinstance(Track.duration,int)) or Track.duration==None or('.' or '-' or ',' or '' or ' ' or "'") in str(Track.duration)) or Track.duration>2147483647 or Track.duration<1:
            # duration=float(Track.duration)
            # duration=(duration/1000.00)/60.00
            # print ('float duration',duration)
            print('Error en la duracion ',Track.duration, type(Track.duration))
            return 1
        #valida que no se repita
        try:
            # conect = sqlite3.connect('Arma_tu_biblio.db')
            # cursor = conect.cursor()
            showTracks = self.cur.execute("SELECT ID FROM Track where ID = ?",(Track.uri_track,)).fetchall()
            #print(showTracks,len(showTracks))
        except:
            print("Error en validar que no se repita")
            return 1
        if len(showTracks)>0:
            print("Error el track "+Track.uri_track+" ya existe")
            return 1
        else:
            self.cur.execute("INSERT INTO Track VALUES (?,?,?,?,?)",(Track.uri_track,Track.name,Track.artist,Track.album,Track.duration))
            self.con.commit()
            #conect.close()
            return 0
        print ('Error en ejecucion de query')
        return 1
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< BORRAR TRACK
    def deleteTrack(self, id_track):#debe pasarse el id
        try:
            # conect = sqlite3.connect('Arma_tu_biblio.db')
            # cursor = conect.cursor()
            self.cur.execute("DELETE FROM Track WHERE ID = ?",id_track)
            self.con.commit()
            # conect.close()
            return 0
        except:
            return 1

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< BORRAR TRACKS
    def deleteAllTracks(self):#debe pasarse el id
        try:
            # conect = sqlite3.connect('Arma_tu_biblio.db')
            # cursor = conect.cursor()
            self.cur.execute("DELETE FROM Track")
            self.con.commit()
            # conect.close()
            return 0
        except:
            return 1
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< MOSTRAR TRACKS

    def getPlaylistFromDB(self):
        try:
            # conect = sqlite3.connect('Arma_tu_biblio.db')
            # cursor = conect.cursor()
            showTracks = self.cur.execute("SELECT * from Track").fetchall()
            tracks = []
            i = 0
            for t in showTracks:
                tracks.append(Track(t[0], t[1], t[2], t[3], t[4]))
                i+=1
            if len(tracks)>0:
                # conect.close()
                return tracks
            # conect.close()
            print("Nada que mostrar")
            return 1
        except:
            print("Error en consulta de playlist")
            return 1

    def getIDSFromDB(self,playlist):
        ids=[]
        for id in playlist:
            ids.append(id.id)
        return ids

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< MOSTRAR TRAC
class sinchronize():

    def __init__(self):
        pass

    def updateBDDfromSpotify(self,librarySpotify,objBDD):
        #validat library y  verque no se repitan
        for item in librarySpotify['items']:
            song = item['track']
            #se los manda en el update pero si se repiten
            iD = song['id']
            name = song['name']
            artist = song['artists'][0]['name']
            album = song['album']['name']
            duration = song['duration_ms']
            try:
                cursor = objBDD.cursor()
                cursor.execute("INSERT INTO Track VALUES ('{}','{}','{}','{}','{}')".format(iD, name, artist, album, duration))
                conect.commit()
                conect.close()
                print("updateBDDfromSpotify OK")
                return 0
            except:
                print("Error in updateBDDfromSpotify")


    def updateSpotifyfromBDD(self,SPYFIOBJ,libraryBDD):
        #validat library y  verque no se repitan
        if SPYFIOBJ.saveTrack(libraryBDD):
            print("updateSpotifyfromBDD OK")
            return 0
        return 1

    def checkBDDvsSpotify(self, idsSpotify,idsBDD):
        tracks_diff=[]
        for id in idsBDD:
            if id not in idsSpotify:
                tracks_diff.append(id)
        if len(tracks_diff)>0:
            return tracks_diff
        return 1
