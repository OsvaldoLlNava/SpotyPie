import spotipy
from spotipy import util
import sys
import sqlite3
from spotyPie import SpotyPie

sp=SpotyPie("./data/credenciales.txt","./data/Arma_tu_biblio.db")

def main():


    while(True):
        menu_spotyPyConsole(sp)
        try:
            continuar =int(input(" [*] Ingrese 0 para salir u otro dato para continuar\n [*] > "))
            print()
            if continuar==0:
                break
        except ValueError:
            print(" [-] Ingresa datos validos\n")
        print()

def menu_spotyPyConsole(sp):
    c=True #continue
    try:
        option = int(input(' 1. Buscar track' + '\n' +
        ' 2. Ver tu biblioteca' + '\n' +
        ' 3. Borrar track' + '\n'
        ' 4. Borrar todos los tracks\n' +
        ' 5. Salir'+'\n'+" > "))
    except ValueError:
        print(" \n[-] Error en el valor del dato [opciones menu]\n")
        c=False
    if c:
        if option == 1:
            print("\n [+] Buscar track\n\n")
            try:
                song=str(input(" [*] Introduzca nombre de la cancion: "))
                artist=str(input(" [*] Introduzca nombre del artista: "))

            except ValueError:
                c=False
                print(" [-] Error en el valor del dato\n")
            if c:

                track= sp.searchTrack(song, artist)
                if track!=None:
                    try:
                        print('\n [!] ¿Quieres agregar la siguiente cancion a tu biblioteca?\n')
                        print(" ",track)
                        save = int(input('\n [*] ( 1- Si | 2- No )\n'+" > "))
                        c=True
                    except ValueError:
                        c=False
                        print(" [-] Error en el valor del dato\n")
                    if c:
                        print()
                        if save==1:
                            sp.addTrackToMyPlaylist(track)
                        elif save==2:
                            print(" [+] No se guardo el track\n")
                        else:
                            print(" [!] Ingresa datos validos")
                    else:
                        print(" [-] Datos invalidos!\n")
                else:
                    print(" [-] No se encontro track\n")
        elif option == 2:

            print("\n [+] Ver Playlist \n\n")
            playStr=sp.showMyPlaylist()
            print(" ", playStr) if len(playStr)>0 else print(" [-] No hay informacion\n")
            print()

        elif option == 3:

            print("\n [+] Dellete Track \n\n")
            print(" [*] Mostrando tracks acuales\n")
            playlist=sp.showMyPlaylist()
            if len(playlist)>0:
                print(len(playlist))
                c=True
            else:
                c=False
            if c:
                if playlist!=1 and len(playlist)>0:
                    print()
                    print(" [*] Selecciona el ID a borrar")
                    try:
                        idInput=int(input(" [*] ID> "))
                        c=True
                    except:
                        c=False
                        print(" [-] Error en el valor del dato")
                    if c:
                        #print(type(idInput))
                        if type(idInput)==int and idInput>=0 and idInput<len(playlist):
                            tracks=playlist.split("\n")
                            spr=tracks[idInput].split(",")
                            id= spr[0].split(" ")[2].lstrip("[")
                            try:
                                idInput=int(input(" [!] Seuro de eliminar el track ( 1- SI | 2- NO )\n [*] > "))
                                c=True
                            except:
                                c=False
                                print(" [-] Error en el valor del dato\n")
                            if c:
                                if(idInput)==1:

                                    print(id+" [*] sera borrado ...")
                                    try:
                                        sp.deleteTrack(id)
                                    except:
                                        print(" [-] Error borrando el track\n")
                                else:
                                    (" [+] El track no se eliminara\n")
                        else:
                            print(" [-] verifica la entrada\n")
                else:
                    print(" [-] No hay informacion\n")
            else:
                print(" [-] No hay informacion\n")
        elif option==4:
            print(" [!] Estas seguro que desas eliminar todos tus tracks (de spotify y tu bdd)?")
            try:
                idInput=int(input(" [*] 1 - SI \n Otro dato: No \n > "))

                c=True
            except:
                c=False
                print(" [-] Error en el valor del dato\n")
            if c:
                try:
                    print(" [*] Borrando...")
                    val=sp.deleteAllTracks()
                except:
                    print(" [-] Ocurrio un error eliminando los datos\n")
        elif option==5:
            sp.close()
            sys.exit(0)

        else:
            print(" [-] Ingresa datos correctos por favor :c\n")

if __name__ == '__main__':
    main()
