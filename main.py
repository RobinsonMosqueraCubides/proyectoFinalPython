from camper import *
from docentes import *
from listas import *
from registro import *
from manejoErrores import *
import os
import json
dstudent = 'camper.json'
teach = 'docente.json'
#with open(datos, 'r') as archivo:
#    lista = json.load(archivo)
campers = {}
docente = {}
Ruta = {"NodeJS":[],'Java':[], 'NetCore':[]}
areas = {"Sputnik":[],'Artemiz':[], 'Apollo':[]}

def menuPrincipal():
    while True:
               
        #os.system('clear')
        print(docente)
        print(campers)
        print("Ingrese el numero de la opcion deseada:\n1. Registro\n2. Camper\n3. Docentes\n4. Listas\n5. Salir")
        selec = manejoINT()
        if selec == 1:
            os.system('clear')
            print("ingrese el numero de la opcion deseada:\n1. Registrar Camper\n2. Registrar Docente\n3. Crear Rutas\n4. Registrar Area\n5. Asignar fechas a campers\n6. Menu anterior")
            selec = manejoINT()
            if selec == 1: registroCampers(campers)
            elif selec == 2: registroDocente(docente, Ruta)
            elif selec == 3: registroRutas(Ruta)
            elif selec == 4: registriArea(campers,areas)
            elif selec == 5: registroFecha(campers)
            elif selec == 6: continue                                
            else: print("ingrese un numero del 1 al 6")
        elif selec == 2:
            os.system('clear')
            print("ingrese el numero de la opcion deseada:\n1. Asignar Ruta\n2. Ingreso Nota seleccion\n3. Ingreso notas del filtro\n4. campers inscritos\n5. campers bajo rendimiento\n6. Menu Anterior")
            selec = manejoINT()
            if selec == 1: AsignarRuta(campers,Ruta)
            elif selec == 2: notaSeleccion(campers)
            elif selec == 3: notasFiltro(campers)
            elif selec == 4: campersInscritos(campers)
            elif selec == 5: campersBajoRendimiento(campers)
            elif selec == 6: continue
            else: print("ingrese un numero del 1 al 6")
        elif selec == 3: 
            os.system('clear')
            print("ingrese el numero de la opcion deseada:\n1. Modificar Ruta\n2. Modificar Horario\n3. Modificar area\n 4. docentes vinculados\n 5. Menu Anterior")
            selec = manejoINT()
            if selec == 1: rutaDocente(docente, Ruta)
            elif selec == 2: horarioDocente(docente)
            elif selec == 3: areaDocente(docente)
            elif selec == 4: listarDocente(docente)
            elif selec == 5: continue
            else: print("ingrese un numero del 1 al 5")
        elif selec == 4: 
            os.system('clear')
            print("ingrese el numero de la opcion deseada:\n1. Listar docentes y camper por ruta\n2. Listar campers aprobados y reprobados por rutas\n3. Menu Anterior")
            selec = manejoINT()
            if selec == 1: listaDocenteCamper(docente, campers)
            elif selec == 2: listarCampersAprobados(docente, campers)
            elif selec == 3: continue
        elif selec == 5:                        
            break
    
        else: print("ingrese un numero del 1 al 5")
menuPrincipal()