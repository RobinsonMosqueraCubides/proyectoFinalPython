from camper import *
from docentes import *
from listas import *
from registro import *
from manejoErrores import *
import os
import json

datos = 'data.json'
dstudent = 'camper.json'
teach = 'docente.json'

# Cargar datos desde el archivo JSON si existe
try:
    with open(datos, 'r') as archivo:
        lista = json.load(archivo)
        campers = lista.get('campers', {})
        docente = lista.get('docente', {})
        Ruta = lista.get('Ruta', {"NodeJS": [], 'Java': [], 'NetCore': []})
        areas = lista.get('areas', {"Sputnik": [], 'Artemis': [], 'Apollo': []})
except FileNotFoundError:
    campers = {}
    docente = {}
    Ruta = {"NodeJS": [], 'Java': [], 'NetCore': []}
    areas = {"Sputnik": [], 'Artemis': [], 'Apollo': []}

def menuPrincipal():
    while True:
        # Guardar datos en el archivo JSON
        lista = {'campers': campers, 'docente': docente, 'Ruta': Ruta, 'areas': areas}
        with open(datos, 'w') as archivo:
            json.dump(lista, archivo)
        
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print(docente)
        print(campers)
        print("Ingrese el número de la opción deseada:\n1. Registro\n2. Camper\n3. Docentes\n4. Listas\n5. Salir")
        selec = manejoINT()
        
        if selec == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Ingrese el número de la opción deseada:\n1. Registrar Camper\n2. Registrar Docente\n3. Crear Rutas\n4. Registrar Área\n5. Asignar fechas a campers\n6. Menú anterior")
            selec = manejoINT()
            if selec == 1:
                registroCampers(campers)
            elif selec == 2:
                registroDocente(docente, Ruta)
            elif selec == 3:
                registroRutas(Ruta)
            elif selec == 4:
                registroArea(campers, areas)
            elif selec == 5:
                registroFecha(campers)
            elif selec == 6:
                continue
            else:
                print("Ingrese un número del 1 al 6")
        
        elif selec == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Ingrese el número de la opción deseada:\n1. Asignar Ruta\n2. Ingreso Nota selección\n3. Ingreso notas del filtro\n4. Campers inscritos\n5. Campers bajo rendimiento\n6. Registrar fechas de inicio y fin\n7. Menú anterior")
            selec = manejoINT()
            if selec == 1:
                AsignarRuta(campers, Ruta)
            elif selec == 2:
                notaSeleccion(campers)
            elif selec == 3:
                notasFiltro(campers)
            elif selec == 4:
                campersInscritos(campers)
            elif selec == 5:
                campersBajoRendimiento(campers)
            elif selec == 6:
                registroFecha(campers)
            elif selec == 7:
                continue
            else:
                print("Ingrese un número del 1 al 7")
        
        elif selec == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Ingrese el número de la opción deseada:\n1. Modificar Ruta\n2. Modificar Horario\n3. Modificar área\n4. Docentes vinculados\n5. Menú anterior")
            selec = manejoINT()
            if selec == 1:
                rutaDocente(docente, Ruta)
            elif selec == 2:
                horarioDocente(docente)
            elif selec == 3:
                areaDocente(docente)
            elif selec == 4:
                listarDocente(docente)
            elif selec == 5:
                continue
            else:
                print("Ingrese un número del 1 al 5")
        
        elif selec == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Ingrese el número de la opción deseada:\n1. Listar docentes y camper por ruta\n2. Listar campers aprobados y reprobados por rutas\n3. Menú anterior")
            selec = manejoINT()
            if selec == 1:
                listaDocenteCamper(docente, campers)
            elif selec == 2:
                listarCampersAprobados(docente, campers)
            elif selec == 3:
                continue
            else:
                print("Ingrese un número del 1 al 3")
        
        elif selec == 5:
            break
        else:
            print("Ingrese un número del 1 al 5")

menuPrincipal()
