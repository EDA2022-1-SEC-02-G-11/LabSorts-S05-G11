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
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():

    catalog = {"artista" : None,
               "albumes" : None,
               "canciones" : None,}
    
    catalog["artistas"] = lt.newList("ARRAY_LIST")
    catalog["albumes"] = lt.newList("ARRAY_LIST")
    catalog["canciones"] = lt.newList("ARRAY_LIST")

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


# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento