"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
lista = ""

def newController(lista):
    control = controller.newController(lista)
    return control

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")  

    print("6- Escoger tipo de lista y algoritmo de ordenamiento")


catalog = None

def loadData(archivo):
    artistas, canciones, albumes, tiempo = controller.loadData(control, archivo)
    return artistas, canciones, albumes, tiempo
    


# Se crea el controlador asociado a la vista
control = newController(lista)

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        archivo = input("Seleccione el tipo de archivo a cargar(small, 5pct, 10pct, 20pct, 30pct, 50pct, 80pct, large ): ")
        print("Cargando información de los archivos ....")
        art, alb, canc, tiempo = loadData(archivo)
        print('Artistas cargados: ' + str(art))
        print('Albumes cargados: ' + str(alb))
        print('Albumes cargados: ' + str(canc))
        print(tiempo)
        #primeros = controller.primerosArtistas()

        #print(primeros)
    elif int(inputs[0]) == 6:
        lista = input("Escriba el tipo de lista para organizar: ")
        ordenamiento = input("Escribe el tipo de ordenamiento iterativo a usar: ")

        resultado = controller.sortArtistas(control, ordenamiento)
        newController(lista)  
        print(resultado[1])

    #! AVISO  TIPO DE lista     

    else:
        sys.exit(0)
sys.exit(0)
