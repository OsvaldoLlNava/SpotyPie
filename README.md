# SpotyPie
Hello, spotyPie is an demo about how apis works, we used python3.7, requests 2.22.0 and spotypy 2.4.4 librarys, there are a class to control the api interaction, one to database control, and other to maintain sichronized database and our spotify acount, we need are logged as developer in spotify first. The objective is to communicate with an api and store the answer. For storage we use sqlite3. What can spotyPie do?:

  * get track from spotify with song's name and artist's name and allow save on spotify "liked songs" playlist
  * further to make an backup of your favorite tracks from spotify into file for export latter to other user
  * starting of backup file we can upload to our playlist
  * get our playlist from spotify
  * delete some or all tracks
  * maintain our datas in database file and spotify acount sinchronized
  
 Also are included the tests in /tests folder.

FILE SPYCLASS.PY<br> 
  class APISFY\()<br>
      \* readCredentials(list file) > return credentials if ok or 0 if not.<br>
      \* saveTrack(list idTrackList) > return 0 in exit or 1 if there an error<br>
      \* getTrackFromSpotify(string songName, string artistName) > return object track or 1<br>
      \* getPlaylistIDSfromSpotify() > return list playlistids or 1<br>
      \* getTrackslistfromSpotify() > return list playlist or 1<br>
      \* printPlaylist(playlist play) > return playlist string and an index for each one or 1<br>
      \* getTrackfromPlaylistWithID(playlist play,int index) > return track.id for play[index] or 1<br>
      \* deleteTrack(playlistids ids) > return 0 if ok and else one<br>
<br>
  class DBSFY()<br>
      * __init__(string archivo_path) > initialize the object DBSFY and connect to database file<br>
      * saveTrack(Track track) > return 0 if saved or else 1<br>
      * deleteTrack(string id_track) > return 0=ok or 1=no_okey<br>
      * deleteAllTracks() > return 0=ok or 1=no_okey<br>
      * getPlaylistfromDB() > return tracks list or 1=no_okey<br>
      * getIDSFromDB(playlist tracks_list) > return list of id or 1<br>

  class sinchronize()<br>
      * updateBDDfromSpotify(playlist librarySpotify, DBSFY objDB) > return 0 =ok or 1=no_okey<br>
      * updateSpotifyfromBDD(APISFY apiObj, playlist libraryFromDB) > return 0 =ok or 1=no_okey<br>
      * checkBDDvsSpotify(list idsSpotify,list idsBDD) > return an list of unsinchronized tracks<br>
<br>       
FILE TRACK.PY<br>
   class Track()<br>
      * __init__(string id, sting nameSong, string album, int duration)  > initialize an new Track instance<br>
      * __str__() > return str(f"[{self.id}," +f" de {self.name},"+f"{self.artist},"+f" {self.album},"+f" {self.duration}]")<br>
<br>
FILE SPOTYPIE.PY<br>
   class spotypie()<br>
      * __init__(string credentialsFilePath, string DBFilePath) > initialize SpotiPie Object <br>
      * addTrackToMyPlaylist(list[Track] tracks) > return 0=OK or 1=NO_OK<br>
      * showMyPlaylist() > return 0 or 1<br>
      * deleteTrack(string idTrack) > return 0 or 1<br>
      * deleteAllTracks() > return 0 or 1<br>
      * makeSync() > return 0 or 1<br>
      * close() > return 1 or close<br>
 <br>
<br>
... for now this is it, enjoy the music :)<br>
