import Track
import mock
from mock import patch
from SPYClass import APISFY
from SPYClass import DBSFY
from SPYClass import sinchronize
import sqlite3


class SpotyPie():

    api=None
    bdd=None
    sync=None

    def __init__(self,credentialsFilePath,BDDFIlePath ):
        self.sync=sinchronize()
        self.bdd=DBSFY(BDDFIlePath)
        self.api=APISFY(credentialsFilePath)
        self.makeSync()
        print()
#><<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ok
    def searchTrack(self, songName, artistName):
        return self.api.getTrackfromSpotify(songName,artistName)

#><<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ok
    def addTrackToMyPlaylist(self,track):#must be Track Object
        idlist_adapt={track.id}
        if self.api.saveTrack(idlist_adapt) !=0:
            print (" [-] Error in addTrackToMyPlaylist")
            return 1
        self.bdd.saveTrack(track)
        return 0

#><<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ok
    def showMyPlaylist(self):
        playlist=[]
        try:
            playlist=self.bdd.getPlaylistFromDB()
            if len(playlist)>0:
                #print(self.api.printPlaylist(playlist))
                return self.api.printPlaylist(playlist)
            return playlist
        except:
            print(" [-] Error in showMyPlaylist:getPlaylistFromDB")
            return 1
#><<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ok

    def deleteTrack(self,idtrack): #pasarlo en forma de str
        #print("deleting...",idtrack)
        # try:
        listid_adapt=[idtrack]
        if self.api.deleteTrack(listid_adapt)!=0:
            print(" [-] Error in deleteTrack:api")
            return 1
        if self.bdd.deleteTrack(idtrack) != 0:
            print(" [-] Error in deleteTrack:bdd")
            return 1
        return 0
        # except:
        #     print("Error in deleteTrack")
        #     return 1
#><<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ok
    def deleteAllTracks(self):
        try:
            playlist_sp=self.api.getPlaylistsIDSfromSpotify()
            #print("playlist: >>> ",playlist_sp)
            if len(playlist_sp)>0:
                if self.api.deleteTrack(playlist_sp) !=0:
                    print(" [-] Error in delete track from spotify")
                    return 1
                print(" [+] Tracks deleted from spotify")
            idsbdd=self.bdd.getIDSFromDB(self.bdd.getPlaylistFromDB())
            #print(" >>>>>>>>>",idsbdd)
            if len(idsbdd)>0:
                if self.bdd.deleteAllTracks()!=0:
                    return 1
                print(" [+] Tracks deleted from database")
            if len(idsbdd)<1 and len(playlist_sp)<1:
                print(" [+] No hay informacion")
                return 1
            print(" [+] Tracks deleted")
            return 0
        except:
            return 1
            print(" [-] Error in deleteAllTrack")
# ><<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def close(self):
        try:
            self.bdd.con.close()
            self.bdd=None
            self.api=None
        #
        except:
            print(" [-] Error in close")
            return 1
#><<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def makeSync(self):
        # try:
        # print("Debuging makesync")

        unsync=[]
        idsSpotify=self.api.getPlaylistsIDSfromSpotify()
        # print(" > idsSpotify: ",idsSpotify) # ok
        if len(idsSpotify)>0:
            tracksbdd=self.bdd.getPlaylistFromDB()
            # print(" > tracksbdd: ",tracksbdd) # ok
            if type(tracksbdd)==int:
                print(" [-] Type is int!")
                return 1
            if(len(tracksbdd)>0):
                idsBDD=self.bdd.getIDSFromDB(tracksbdd)
                # print(" > idsBDD: ",idsBDD) # ok
                unsync=self.sync.checkBDDvsSpotify(idsSpotify,idsBDD)
                # print(" > unsync: ",unsync) # ok
                if(len(unsync)>0):
                    self.sync.updateSpotifyfromBDD(self.api,unsync)
                    self.bdd.deleteAllTracks()
                    # print("\n\nself.api.getTrackslistfromSpotify() ",self.api.getTrackslistfromSpotify())
                    self.sync.updateBDDfromSpotify(self.api.getTrackslistfromSpotify(),self.bdd)
                    #print("Synchronized 01!")
                    return 0
            else:
                self.sync.updateBDDfromSpotify(self.api.getTrackslistfromSpotify(),self.bdd)
                #print("Synchronized 02!")
                return 0
        idsbdd=self.bdd.getIDSFromDB(self.bdd.getPlaylistFromDB())

        if len(idsbdd)>0:
            self.sync.updateSpotifyfromBDD(self.api,idsbdd)
            #print("Synchronized! 03")
            return 0
        else:
            print(" [+] Nada que sincronizar")
            return 0
        print()
        return 1
        # except:
        #     print("Error in makeSync")
        #     return 1
