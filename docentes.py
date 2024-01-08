import os


def rutaDocente(docente, Ruta):
    os.system('cls')
    while True:        
        print("Ingrese el nombre del docente:")
        nombre = input('')
        if nombre in docente:
            print("Selecione la ruta:\n\t1. NodeJS\n\t2. Java\n\t3. NetCore")
            selec = int(input(""))
            if selec == 1: docente[nombre]['Ruta']=Ruta['NodeJS']
            elif selec == 2: docente[nombre]['Ruta']=Ruta['Java']
            elif selec == 3: docente[nombre]['Ruta']=Ruta['NetCore']
        else:
            print("Docente no existe")
            continue
        print("Desea modificar otra ruta?\n\t1. Sí\n\t2. No")
        selec = int(input(""))
        if selec ==1: continue 
        else: 
            print("Rutas modificadas")
            break

def horarioDocente(docente):
    os.system('cls')
    while True:        
        print("Ingrese el nombre del docente:")
        nombre = input('')
        if nombre in docente:
            print("Seleccione el horario del docente:\n\t1. 6am a 10am\n\t2. 10am a 2 pm\n\t3. 2pm a 6 pm\n\t4. 6pm a 10 pm")
            selec = int(input(""))
            if selec == 1: docente[nombre]['Horario']="6am a 10am"
            elif selec == 2: docente[nombre]['Horario']="10am a 2pm"
            elif selec == 3: docente[nombre]['Horario']="2pm a 6pm"
            elif selec == 4: docente[nombre]['Horario']="6am a 10pm"
        else:
            print("Docente no existe")
            continue
        print("Desea modificar otro horario?\n\t1. Sí\n\t2. No")
        selec = int(input(""))
        if selec ==1: continue 
        else: 
            print("Horarios modificados")
            break

def areaDocente(docente):
    os.system('cls')
    while True:        
        print("Ingrese el nombre del docente:")
        nombre = input('')
        if nombre in docente:
            print("Selecione el area de trabajo:\n\t1. Apollo\n\t2. Artemis\n\t3. Sputnik")
            selec = int(input(""))
            if selec == 1: docente[nombre]['Area']="Apollo"
            elif selec == 2: docente[nombre]['Area']="Artemis"
            elif selec == 3: docente[nombre]['Area']="Sputnik"
        else:
            print("Docente no existe")
            continue
        print("Desea modificar otro horario?\n\t1. Sí\n\t2. No")
        selec = int(input(""))
        if selec ==1: continue 
        else: 
            print("Horarios modificados")
            break

def listarDocente(docente):
    print("Nombre\tArea\tHorario\tRuta")
    for i in docente:
        print(f"{i}\t{docente[i]['Area']}\t{docente[i]['Horario']}\t{docente[i]['Ruta']}")