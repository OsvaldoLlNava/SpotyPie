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
        sync=synchronize()
        bdd=DBSFY(BDDFIlePath)
        api=APISF(credentialsFilePath)
        self.makeSync()

    def addTrackToMyPlaylist(self,tracks):#must be a list of tracks
        if api.saveTrack(tracks) !=0:
            print ("Error in addTrackToMyPlaylist")
            return 1
        return 0

    def showMyPlaylist(self):
        try:
            playlist=bdd.getPlaylistFromDB()
            if len(playlist)>0:
                print(api.printPlaylist(playlist))
                return 0
            print("Error in showMyPlaylist")
            return 1
        except:
            print("Error in showMyPlaylist:getPlaylistFromDB")
            return 1


    def deleteTrack(self,idtrack): #pasarlo en forma de lista
        try:
            if api.deleteTrack(idtrack)!=0:
                print("Error in deleteTrack:api")
                return 1
            if bdd.deleteTrack(idtrack) != 0:
                print("Error in deleteTrack:bdd")
                return 1
            return 0
        except:
            print("Error in deleteTrack")
            return 1

    def deleteAllTracks(self):
        try:
            playlist_sp=api.getPlaylistsIDSfromSpotify()
            if len(playlist)>0:
                if api.deleteTrack(playlist_sp) !=0:
                    return 1
                print("Tracks deleted from spotify")
            if len(bdd.getIDSFromDB)>0:
                if bdd.deleteAllTracks()!=0:
                    return 1
                print("Tracks deleted from database")
            print("Tracks deleted")
            return 0
        except:
            return 1
            print("Error in deleteTrack")

    def close(self):
        try:
            bdd.close()
            bdd=None
            api=None
            Close()
        except:
            print("Error in close")
            return 1

    def makeSync(self):
        try:
            unsync=[]
            unsync=sync.checkBDDvsSpotify()
            unsync.updateSpotifyfromBDD(api,unsync)
            unsync.updateBDDfromSpotify(api.getTrackslistfromSpotify(),bdd)
            return 0
        except:
            print("Error in maakeSync")
            return 1

    
