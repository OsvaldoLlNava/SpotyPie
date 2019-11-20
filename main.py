import spotipy
from spotipy import util
import sys
import sqlite3


apisfy = APISFY()
dbsfy =  DBSFY('Arma_tu_biblio.db')
sp = spotipy.Spotify(auth=token)

#Devuelve informacion del track
def search_info(): #***************************************
    song = input("Como se llama la rola: ")                    #*
    artist = input('¿Quien la canta?: ')                       #+

    info = apisfy.getTrackfromSpotify(song, artist)                 #*
    if song:                                   #no esto nooo
        print(info)
        return info                                             #*
    else:
        return 1#***********************************

 #Guarda info en DB #*****************************

def main():
    list_tracks=[]
    library = sp.current_user_saved_tracks()

    print('Bienvenido akralma, ¿Que quieres hacer?') #cambiar esa chingadera de abrakadabra
    cont = False
    while True:

        option = int(input('1. Agregar track' + '\n' +
                           '2. Ver tu biblioteca' + '\n' +
                           '3. Borrar track' + '\n'
                           '4. Salir' + '\n' +
                           '5. Migrar Datos' + '\n'))
        if option == 1:

            track = search_info()
            print('¿Quieres agregar esta cancion a tu biblioteca?')
            save = int(input('1. Si' + '\n' + '2. No' + '\n'))

            if save == 1:
                list_tracks.append(track.id)
                sp.current_user_saved_tracks_add(list_tracks)  # Guarda en biblioteca
                if (dbsfy.saveTrack(track))!=1: #Guarda archivo en DB
                    print('La canción ha sido agregada' + '\n')
                #si guarda que revise
            elif save == 2:
                print(option)

        elif option == 2:
            dbsfy.showTrack()##cambiar esto no es aqui

        elif option ==3:
            name = input('¿Cual cancion quieres eliminar?: ' + '\n')
            dbsfy.del_track(name)

            print('¿Quieres seguir eliminando?' + '\n')
            stop = int(input('1.Si ' + '2. No' + '\n'))

            if stop == 1:
                print(name)
            else:
                print(option)


        elif option == 4:
            break

        elif option == 5:
            library = sp.current_user_saved_tracks()



        else:
            print("Introduce una opcion valida")

        sys.exit()

if __name__ == '__main__':
    main()
