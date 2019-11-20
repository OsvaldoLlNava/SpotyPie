# SpotyPie
Hello, spotyPie is an demo about how apis works, we used python3.7, requests 2.22.0 and spotypy 2.4.4 librarys, there are a class to control the api interaction, one to database control, and other to maintain sichronized database and our spotify acount, we need are logged as developer in spotify first. The objective is to communicate with an api and store the answer. For storage we use sqlite3. What can spotyPie do?:

  * get track from spotify with song's name and artist's name and allow save on spotify "liked songs" playlist
  * further to make an backup of your favorite tracks from spotify into file for export latter to other user
  * starting of backup file we can upload to our playlist
  * get our playlist from spotify
  * delete some or all tracks
  * maintain our datas in database file and spotify count sinchronized
  
 Also are included the tests in /tests folder.

FILE SPYCLASS.PY 
  class APISFY() 
      * readCredentials(list file) > return credentials if ok or 0 if not.
      * saveTrack(list idTrackList) > return 0 in exit or 1 if there an error
      * getTrackFromSpotify(string songName, string artistName) > return object track or 1
      * getPlaylistIDSfromSpotify() > return list playlistids or 1
      * getTrackslistfromSpotify() > return list playlist or 1
      * printPlaylist(playlist play) > return playlist string and an index for each one or 1
      * getTrackfromPlaylistWithID(playlist play,int index) > return track.id for play[index] or 1
      * deleteTrack(playlistids ids) > return 0 if ok and else one

  class DBSFY()
      * __init__(string archivo_path) > initialize the object DBSFY and connect to database file
      * saveTrack(Track track) > return 0 if saved or else 1
      * deleteTrack(string id_track) > return 0=ok or 1=no_okey
      * deleteAllTracks() > return 0=ok or 1=no_okey
      * getPlaylistfromDB() > return tracks list or 1=no_okey
      * getIDSFromDB(playlist tracks_list) > return list of id or 1

  class sinchronize()
      * updateBDDfromSpotify(playlist librarySpotify, DBSFY objDB) > return 0 =ok or 1=no_okey
      * updateSpotifyfromBDD(APISFY apiObj, playlist libraryFromDB) > return 0 =ok or 1=no_okey
      * checkBDDvsSpotify(list idsSpotify,list idsBDD) > return an list of unsinchronized tracks
    
    
FILE TRACK.PY
   class Track()
      * __init__(string id, sting nameSong, string album, int duration)  > initialize an new Track instance
      * __str__() > return str(f"[{self.id}," +f" de {self.name},"+f"{self.artist},"+f" {self.album},"+f" {self.duration}]")

FILE SPOTYPIE.PY
   class spotypie()
      * __init__(string credentialsFilePath, string DBFilePath) > initialize SpotiPie Object
      * addTrackToMyPlaylist(list[Track] tracks) > return 0=OK or 1=NO_OK
      * showMyPlaylist() > return 0 or 1
      * deleteTrack(string idTrack) > return 0 or 1
      * deleteAllTracks() > return 0 or 1
      * makeSync() > return 0 or 1
      * close() > return 1 or close
 

... for now this is it, enjoy the music :)
