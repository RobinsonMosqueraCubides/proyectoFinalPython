import os
from registro import *
def AsignarRuta():
    while True:
        os.system('cls')        
        print("Ingrese el documento del Camper:")
        cc = int(input(""))
        if cc in campers:
            print("Seleccione la ruta asignar:\n\t1. NodeJS\n\t2. Java\n\t3. NetCore")
            selec = int(input(""))
            if selec == 1: campers[cc]['ruta']='NodeJS'
            elif selec == 2: campers[cc]['ruta']='Java'
            elif selec == 3: campers[cc]['ruta']='NetCore'
        else: 
            print("Camper no existe")
            continue
        print("Desea Asignar otra ruta?\n\t1. Sí\n\t2. No")
        selec = int(input(""))
        if selec ==1: continue 
        else: 
            print("Rutas Asignadas")
            break
    print(campers)

def notaSeleccion():
    while True:
        os.system('cls')
        print("Ingrese el documento del Camper:")
        cc = int(input(""))
        if cc in campers:
                print("Ingrese la Nota del camper")
                nota = int(input(""))
                if nota >= 60:
                    campers[cc]['estado']='inscrito'
                    campers[cc]['notas de filtro']=[]
                else:
                    campers[cc]['estado']='No inscrito'
        else: 
            print("Camper no existe")
            continue
        print("Desea ingresar otra nota?\n\t1. Sí\n\t2. No")
        selec = int(input(""))
        if selec ==1: continue 
        else: 
            print("Notas Asignadas")
            break


def notasFiltro():
     os.system('cls')
     while True:        
        print("Ingrese el documento del Camper:")
        cc = int(input(""))
        if cc in campers:
            if 'notas de filtro' in campers[cc]:
                print("Ingrese la nota de Quiz")
                quiz=int(input(""))
                print("Ingrese la nota de Trabajos:")
                Trabajos=int(input(""))
                print("Ingrese la nota de prueba practica:")
                pruebaPactica=int(input(""))
                print("Ingrese la nota de prueba toerica:")
                pruebaTeorica=int(input(""))
                notaFinal = ((((quiz+Trabajos)/2)*0.10)+(pruebaPactica*0.6)+(pruebaTeorica*0.3))
                campers[cc]['notas de filtro'].append(notaFinal)
            else:
                print("Camper no inscrito")
                continue
        else:
            print("Camper no existe")
            continue
        print("Desea ingresar otra nota?\n\t1. Sí\n\t2. No")
        selec = int(input(""))
        if selec ==1: continue 
        else: 
            print("Notas Asignadas")
            break
     

def campersInscritos():
    print("Cedula\tNombre")
    for i in campers:
        if 'inscrito' in campers[i].values():
            print(f"{i}\t{campers[i]['nombre']}")

def campersBajoRendimiento():
     for i in campers:
         promNotas = campers[i]['notas de filtro']/len(campers[i]['notas de filtro'])
         if promNotas < 60:
             print(f"{i}\t{campers[i]['nombre']}")

