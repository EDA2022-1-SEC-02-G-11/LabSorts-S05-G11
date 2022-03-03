"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """

import config as cf
import time
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as shel
from DISClib.Algorithms.Sorting import selectionsort as sel
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import quicksort as qui 
from DISClib.Algorithms.Sorting import mergesort as mer
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog(Lista):

    catalog = {"artista" : None,
               "albumes" : None,
               "canciones" : None,}
    
    catalog["artistas"] = lt.newList(Lista)
    catalog["albumes"] = lt.newList(Lista)
    catalog["canciones"] = lt.newList(Lista)

    return catalog
# Funciones para agregar informacion al catalogo

def addArtista(catalog, artista):
    lt.addLast(catalog["artistas"],artista)
    return catalog

def addAlbum(catalog, album):
    lt.addLast(catalog["albumes"],album)
    return catalog

def addCancion(catalog, cancion):
    lt.addLast(catalog["canciones"], cancion)
    return catalog

# Funciones para creacion de datos

# Funciones de consulta

def artistaSize(catalog):
    return lt.size(catalog["artistas"])

def albumSize(catalog):
    return lt.size(catalog["albumes"])

def cancionSize(catalog):
    return lt.size(catalog["canciones"])

def primeros(catalog, tipo):
    primero = catalog[tipo][0]
    segundo = catalog[tipo][1]
    tercero = catalog[tipo][2]

    return primero, segundo, tercero

# Funciones utilizadas para comparar elementos dentro de una lista

def cmpArtistsByFollowers(artist1, artist2):
    """ 
    Devuelve verdadero (True) si los 'followers' de artist1 son menores que los del artist2
    Args:
    artist1: información del primer artista que incluye su valor 'followers'
    artist2: información del segundo artista que incluye su valor 'followers'
    """
    cantidad = False
    if artist1["followers"] < artist2["followers"]:
        cantidad = True
    
    return cantidad
# Funciones de ordenamiento

def sortArtists(catalogo, ordenamiento):
    if ordenamiento == "shell":
        inicio_tiempo = getTime()
        lista_ordenada = shel.sort(catalogo["artistas"],cmpArtistsByFollowers)
        final_tiempo = getTime()
        delta_tiempo = deltaTime(inicio_tiempo, final_tiempo)
    if ordenamiento == "selection":
        inicio_tiempo = getTime()
        lista_ordenada = sel.sort(catalogo["artistas"],cmpArtistsByFollowers)
        final_tiempo = getTime()
        delta_tiempo = deltaTime(inicio_tiempo, final_tiempo)
    if ordenamiento == "insertion":
        inicio_tiempo = getTime()
        lista_ordenada = ins.sort(catalogo["artistas"],cmpArtistsByFollowers)
        final_tiempo = getTime()
        delta_tiempo = deltaTime(inicio_tiempo, final_tiempo)
    if ordenamiento == "merge":
        inicio_tiempo = getTime()
        lista_ordenada = mer.sort(catalogo["artistas"],cmpArtistsByFollowers)
        final_tiempo = getTime()
        delta_tiempo = deltaTime(inicio_tiempo, final_tiempo)
    if ordenamiento == "quick":
        inicio_tiempo = getTime()
        lista_ordenada = qui.sort(catalogo["artistas"],cmpArtistsByFollowers)
        final_tiempo = getTime()
        delta_tiempo = deltaTime(inicio_tiempo, final_tiempo)

    return lista_ordenada, delta_tiempo
#Funciones para medir tiempos de ejecucion
def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def deltaTime(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

