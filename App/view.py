"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
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
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller 
import csv
from ADT import list as lt
from ADT import orderedmap as map
from DataStructures import listiterator as it

import sys


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones  y  por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def printMenu():
    print("Bienvenido al Laboratorio 6")
    print("1- Cargar información")
    print("2- Total de accidentes antes de una fecha(req 1)")
    print("3- Total de accidentes en una fecha reportando cuantos de cada severidad(req 2 )")
    print("4- Consultar accidentes, por ciudad, en un rango de fechas(req 3)")
    print("5- Consultar estado con más accidentes, en una fecha específica (req 4)")
    print("0- Salir")


def initCatalog ():
    """
    Inicializa el catalogo
    """
    return controller.initCatalog()


def loadData (catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)


"""
Menu principal 
""" 
def main():
    while True: 
        printMenu()
        inputs =input('Seleccione una opción para continuar\n')
        if int(inputs[0])==1:
            print("Cargando información de los archivos ....")
            print("Recursion Limit:",sys.getrecursionlimit())
            catalog = initCatalog ()
            loadData (catalog)
            print ('Tamaño árbol usado para ciudades: ' + str(map.size(catalog['cityTree'])))
            print ('Tamaño árbol usado para estados: ' + str(map.size(catalog['statesTree'])))
            print ('Tamaño árbol accidentes por fecha : ' + str(map.size(catalog['dateTree'])))
            print ('Altura árbol usado para ciudades: ' + str(map.height(catalog['cityTree'])))
            print ('Altura árbol por fecha: ' + str(map.height(catalog['dateTree'])))
        elif int(inputs[0])==2:
            date = input("Fecha del accidente (YYYY-MM-DD): ")
            counter = controller.getAccidentsBeforeDate(catalog, date)
            if counter > 0 :
                print("Hay ", counter, " accidentes en fechas menores a " + date )
            else:
                print("Fecha fuera de limites: ",date)
        elif int(inputs[0])==3:
            date = input("Ingrese la fecha a consultar (YYYY-MM-DD): ")
            response = controller.getAccidentByDateSeverity(catalog,date)
            if response > 0:
                print( 'Total de accidentes para dicha fecha:',response)
            else:
                print("No se encontraron accidentes para esta fecha",date) 
        elif int(inputs[0])==4:
            dates = input("Ingrese los las fechas desde y hasta (YYYY-MM-DD YYYY-MM-DD): ")
            counter = controller.getAccidentsByDateRange(catalog, dates) 
            if counter:
                print("Cantidad de accidentes entre las fechas por ciudad",dates,":",counter)
            else:
                print("No se encontraron accidentes para el rango de fechas",dates) 
        elif int(inputs[0])==5:
            date = input("Ingrese una fecha (YYYY-MM-DD): ")
            resp = controller.getAccidentsByDateState(catalog, date) 
            if resp:
                print("\nEstado con más accidentes en la fecha",date,": ",resp[0], ", con ",resp[1]," accidentes\n")
            else:
                print("No se encontraron accidentes en esa fecha",date) 
        else:
            sys.exit(0)
    sys.exit(0)

if __name__ == "__main__":
    #sys.setrecursionlimit(11000)
    main()