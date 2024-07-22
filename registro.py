import os
from manejoErrores import *

def registroCampers(campers):
    while True:
        os.system('clear')
        print("Ingrese el numero de identificacion:")
        cc = input("")
        print("Ingrese el nombre:")
        nombre = manejoStr()
        print("Ingrese el apellido:")
        apellido = manejoStr()
        print("Ingrese la direccion:")
        direccion = input("")
        print("Ingrese la edad:")
        edad = manejoINT()
        if edad >= 18:
            acudiente = None                
        else:
            acudiente = [] 
            print("Ingrese el nombre del acudiente:")
            acudiente.append(manejoStr())
            print("Ingrese el telefono del acudiente:")
            acudiente.append(manejoINT())
        print("Ingrese el Numero de telefono:")
        tel = []
        tel.append(manejoINT())
        print("Desea agregar otro numero?\n\t1. Sí\n\t2. No")
        selec = manejoINT()
        if selec == 1:
            tel.append(manejoINT())
        estado = "inscrito"
        datos = {'nombre': nombre, 'apellido': apellido, 'direccion': direccion, 'acudiente': acudiente, 'tel': tel, 'estado': estado}
        campers[cc] = datos
        print("Desea registrar otro camper?\n\t1. Sí\n\t2. No")
        selec = manejoINT()
        if selec == 1:
            continue 
        else: 
            print("Campers registrados")
            input()
            break
    print(campers)
        
def registroDocente(docente, Ruta):
    rutaDocente = {}
    while True:
        os.system('clear')
        print("Ingrese el nombre:")
        nombre = manejoStr()
        print("Seleccione el horario del docente:\n\t1. 6am a 10am\n\t2. 10am a 2 pm\n\t3. 2pm a 6 pm\n\t4. 6pm a 10 pm")
        selec = manejoINT()
        Horario = ["6am a 10am", "10am a 2pm", "2pm a 6pm", "6pm a 10pm"][selec - 1]
        
        print("Seleccione el area de trabajo:\n\t1. Apollo\n\t2. Artemis\n\t3. Sputnik")
        selec = manejoINT()
        Area = ["Apollo", "Artemis", "Sputnik"][selec - 1]

        print("Seleccione la ruta:\n\t1. NodeJS\n\t2. Java\n\t3. NetCore")
        selec = manejoINT()
        ruta = ["NodeJS", "Java", "NetCore"][selec - 1]
        
        docente[nombre] = {'Ruta': {ruta: Ruta.get(ruta, {})}, 
                           'Horario': Horario, 
                           'Area': Area}
        print("Desea registrar otro docente?\n\t1. Sí\n\t2. No")
        selec = manejoINT()
        if selec == 1:
            continue 
        else: 
            print("docentes registrados")
            input()
            break
    print(docente)

def registroRutas(Ruta):
    while True:
        os.system('clear')
        print("Seleccione La ruta que desea crear:\n\t1. NodeJS\n\t2. Java\n\t3. NetCore")
        selec = manejoINT()
        ruta = ["NodeJS", "Java", "NetCore"][selec - 1]
        Ruta[ruta] = {}
        
        print("Programacion Web:\n\t1. HTML\n\t2. CSS\n\t3. Bootstrap")
        selec = manejoINT()
        web = ["HTML", "CSS", "Bootstrap"][selec - 1]
        Ruta[ruta]['Programacion Web'] = web
        
        print("Programacion formal:\n\t1. Java\n\t2. JavaScript\n\t3. C#")
        selec = manejoINT()
        formal = ["Java", "JavaScript", "C#"][selec - 1]
        Ruta[ruta]['Programacion formal'] = formal
        
        print("Bases de datos:\n\t1. Mysql\n\t2. MongoDb\n\t3. Postgresql")
        selec = manejoINT()
        db = ["Mysql", "MongoDb", "Postgresql"][selec - 1]
        Ruta[ruta]['Bases de datos'] = db
        
        print("Backend:\n\t1. NetCore\n\t2. Spring Boot\n\t3. NodeJS\n\t4. Express")
        selec = manejoINT()
        backend = ["NetCore", "Spring Boot", "NodeJS", "Express"][selec - 1]
        Ruta[ruta]['Backend'] = backend
        
        print("Desea crear otra Ruta?\n\t1. Sí\n\t2. No")
        selec = manejoINT()
        if selec == 1:
            continue 
        else: 
            print("Rutas Creadas")
            input()
            break

def registriArea(campers, areas):
    os.system('clear')
    while True:                
        print("Ingrese el documento del Camper:")
        cc = input("")
        if cc in campers:
            if campers[cc].get('estado') == 'inscrito':
                print("Seleccione el area de trabajo:\n\t1. Apollo\n\t2. Artemis\n\t3. Sputnik")
                selec = manejoINT()
                area = ["Apollo", "Artemis", "Sputnik"][selec - 1]
                if areas[area] < 33:
                    areas[area] += 1 
                    campers[cc]['Area'] = area                    
                else:
                    print("Area llena, seleccione otra")
                    continue
        print("Desea asignar otra area?\n\t1. Sí\n\t2. No")
        selec = manejoINT()
        if selec == 1:
            continue 
        else: 
            print("Areas asignadas")
            input()
            break

def registroFecha(campers):
    while True:
        print("Ingrese la cc del camper:")
        cc = input("")
        if cc in campers:
            if campers[cc].get('estado') == 'inscrito':
                print("Ingrese el dia de ingreso:")
                dia = manejoINT()
                print("Ingrese el mes de ingreso:")
                mes = manejoINT()
                print("Ingrese el año de ingreso:")
                anio = manejoINT()
                print("Ingrese el dia esperado de finalizacion:")
                diaF = manejoINT()
                print("Ingrese el mes esperado de finalizacion:")
                mesF = manejoINT()
                print("Ingrese el año esperado de finalizacion:")
                anioF = manejoINT()                        
                campers[cc]['Fecha Inicio'] = f"{dia}/{mes}/{anio}"
                campers[cc]['Fecha Fin'] = f"{diaF}/{mesF}/{anioF}"
            else:
                print("Camper no inscrito")
        else:
            print("Camper no registrado")
        print("Desea ingresar otra fecha?\n\t1. Sí\n\t2. No")
        selec = manejoINT()
        if selec == 1:
            continue 
        else: 
            print("Fechas Asignadas")
            break
