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
 """
import config as cf
import model
import csv

csv.field_size_limit(5000*1024*1024)


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""
def newController(Lista):

    control = {
        "model": None
    }
    control["model"] = model.newCatalog(Lista)
    print(Lista)
    return control


# Inicialización del Catálogo de libros

def loadData(control, archivo):
    inicio_tiempo = model.getTime()
    catalog = control["model"]
    artistas = loadArtistas(catalog, archivo) 
    albumes = loadAlbumes(catalog, archivo)
    canciones = loadCanciones(catalog, archivo)
    final_tiempo = model.getTime()
    tiempo = model.deltaTime(inicio_tiempo,final_tiempo)

    return  artistas, albumes, canciones, tiempo

# Funciones para la carga de 

def loadArtistas(catalog, archivo):
    archivoArtistas = cf.data_dir + "Spotify/spotify-artists-utf8-"+str(archivo)+".csv"
    archivo = csv.DictReader(open(archivoArtistas, encoding= "utf-8"))
    for artista in archivo:
        model.addArtista(catalog, artista)
    return model.artistaSize(catalog)

def loadAlbumes(catalog, archivo):
    archivoAlbumes = cf.data_dir + "Spotify/spotify-albums-utf8-"+str(archivo)+".csv"
    archivo = csv.DictReader(open(archivoAlbumes, encoding= "utf-8"))
    for album in archivo:
        model.addAlbum(catalog, album)
    return model.albumSize(catalog)

def loadCanciones(catalog, archivo):
    archivoCanciones = cf.data_dir + "Spotify/spotify-tracks-utf8-"+str(archivo)+".csv"
    archivo = csv.DictReader(open(archivoCanciones, encoding= "utf-8"))
    for cancion in archivo:
        model.addCancion(catalog, cancion)
    return model.cancionSize(catalog)

    
    
 # Funciones de ordenamiento
def primerosArtistas(catalog):  
        return model.primeros(catalog, "artistas")
def primerosAlbumes(catalog):
        return model.primeros(catalog, "albumes")
def primerasCanciones(catalog):
        return model.primeros(catalog, "canciones")

def sortArtistas(control, ordenamiento):
        return model.sortArtists(control["model"], ordenamiento)

# Funciones de consulta sobre el catálogo
