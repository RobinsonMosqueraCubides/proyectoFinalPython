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
        if edad >= 18: acudiente = None                
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
        if selec ==1: tel.append(manejoINT())
        estado = "inscrito"
        datos = {'nombre':nombre,'apellido':apellido,'direccion':direccion,'acudiente':acudiente,'tel':tel,'estado':estado}
        campers[cc] = datos
        print("Desea registrar otro camper?\n\t1. Sí\n\t2. No")
        selec = manejoINT()
        if selec ==1: continue 
        else: 
            print("Campers registrados")
            input()
            break
    print(campers)
        
def registroDocente(docente,Ruta):
    rutaDocente = {}
    while True:
        os.system('clear')
        print("Ingrese el nombre:")
        nombre = manejoStr()
        print("Seleccione el horario del docente:\n\t1. 6am a 10am\n\t2. 10am a 2 pm\n\t3. 2pm a 6 pm\n\t4. 6pm a 10 pm")
        selec = manejoINT()
        if selec == 1: Horario="6am a 10am"
        elif selec == 2: Horario="10am a 2pm"
        elif selec == 3: Horario="2pm a 6pm"
        elif selec == 4: Horario="6am a 10pm"
        print("Selecione el area de trabajo:\n\t1. Apollo\n\t2. Artemis\n\t3. Sputnik")
        selec = manejoINT()
        if selec == 1: Area="Apollo"
        elif selec == 2: Area="Artemis"
        elif selec == 3: Area="Sputnik"
        print("Selecione la ruta:\n\t1. NodeJS\n\t2. Java\n\t3. NetCore")
        selec = manejoINT()
        if selec == 1: ruta="NodeJS"
        elif selec == 2: ruta="Java"
        elif selec == 3: ruta="NetCore"
<<<<<<< HEAD
        docente[nombre] = {'Ruta':{ruta: Ruta.get(ruta, {})}, 
=======
        rutaDocente[ruta] = Ruta[ruta]
        docente[nombre] = {'Ruta':rutaDocente, 
>>>>>>> e1c8399374e6ed4db9e5de760dec865c81ec3f83
                        'Horario':Horario, 
                        'Area':Area}
        print("Desea registrar otro docente?\n\t1. Sí\n\t2. No")
        selec = manejoINT()
        if selec ==1: continue 
        else: 
            print("docentes registrados")
            input()
            break
    print(docente)

def registroRutas(Ruta):#Crear una funcion que evalue si ya la ruta fue creada
    while True:
        os.system('clear')
        print("Selecione La ruta que desea crear:\n\t1. NodeJS\n\t2. Java\n\t3. NetCore")
        selec = manejoINT()
        if selec == 1: 
            print("Programacion Web:\n\t1. HTML\n\t2. CSS\n\t3. Bootstrap")
            selec = manejoINT()
            if selec == 1: Ruta["NodeJS"]['Programacion Web'] = 'HTML'
            elif selec == 2: Ruta["NodeJS"]['Programacion Web'] = "CSS"
            elif selec == 3: Ruta["NodeJS"]['Programacion Web'] = "Bootstrap"
            print("Programacion formal:\n\t1. Java\n\t2. JavaScript\n\t3. C#")
            selec = manejoINT()
            if selec == 1: Ruta["NodeJS"]['Programacion formal'] = "Java"
            elif selec == 2: Ruta["NodeJS"]['Programacion formal'] = "JavaScript"
            elif selec == 3: Ruta["NodeJS"]['Programacion formal'] = "C#" 
            print("Bases de datos:\n\t1. Mysql\n\t2. MongoDb\n\t3. Postgresql")
            selec = manejoINT()
            if selec == 1: Ruta["NodeJS"]['Bases de datos'] = "Mysql"
            elif selec == 2: Ruta["NodeJS"]['Bases de datos'] = "MongoDb"
            elif selec == 3: Ruta["NodeJS"]['Bases de datos'] = "Postgresql" 
            print("Backend:\n\t1. NetCore\n\t2. Spring Boot\n\t3. NodeJS\n\t4. Express")
            selec = manejoINT()
            if selec == 1: Ruta["NodeJS"]['Backend'] = "NetCore"
            elif selec == 2: Ruta["NodeJS"]['Backend'] = "Spring Boot"
            elif selec == 3: Ruta["NodeJS"]['Backend'] = "NodeJS" 
            elif selec == 4: Ruta["NodeJS"]['Backend'] = "Express" 
            
        elif selec == 2:
            print("Programacion Web:\n\t1. HTML\n\t2. CSS\n\t3. Bootstrap")
            selec = manejoINT()
            if selec == 1: Ruta["Java"]['Programacion Web'] = 'HTML'
            elif selec == 2: Ruta["Java"]['Programacion Web'] = "CSS"
            elif selec == 3: Ruta["Java"]['Programacion Web'] = "Bootstrap"
            print("Programacion formal:\n\t1. Java\n\t2. JavaScript\n\t3. C#")
            selec = manejoINT()
            if selec == 1: Ruta["Java"]['Programacion formal'] = "Java"
            elif selec == 2: Ruta["Java"]['Programacion formal'] = "JavaScript"
            elif selec == 3: Ruta["Java"]['Programacion formal'] = "C#" 
            print("Bases de datos:\n\t1. Mysql\n\t2. MongoDb\n\t3. Postgresql")
            selec = manejoINT()
            if selec == 1: Ruta["Java"]['Bases de datos'] = "Mysql"
            elif selec == 2: Ruta["Java"]['Bases de datos'] = "MongoDb"
            elif selec == 3: Ruta["Java"]['Bases de datos'] = "Postgresql" 
            print("Backend:\n\t1. NetCore\n\t2. Spring Boot\n\t3. NodeJS\n\t4. Express")
            selec = manejoINT()
            if selec == 1: Ruta["Java"]['Backend'] = "NetCore"
            elif selec == 2: Ruta["Java"]['Backend'] = "Spring Boot"
            elif selec == 3: Ruta["Java"]['Backend'] = "NodeJS" 
            elif selec == 4: Ruta["Java"]['Backend'] = "Express"
        elif selec == 3: 
            print("Programacion Web:\n\t1. HTML\n\t2. CSS\n\t3. Bootstrap")
            selec = manejoINT()
            if selec == 1: Ruta["NetCore"]['Programacion Web'] = 'HTML'
            elif selec == 2: Ruta["NetCore"]['Programacion Web'] = "CSS"
            elif selec == 3: Ruta["NetCore"]['Programacion Web'] = "Bootstrap"
            print("Programacion formal:\n\t1. Java\n\t2. JavaScript\n\t3. C#")
            selec = manejoINT()
            if selec == 1: Ruta["NetCore"]['Programacion formal'] = "Java"
            elif selec == 2: Ruta["NetCore"]['Programacion formal'] = "JavaScript"
            elif selec == 3: Ruta["NetCore"]['Programacion formal'] = "C#" 
            print("Bases de datos:\n\t1. Mysql\n\t2. MongoDb\n\t3. Postgresql")
            selec = manejoINT()
            if selec == 1: Ruta["NetCore"]['Bases de datos'] = "Mysql"
            elif selec == 2: Ruta["NetCore"]['Bases de datos'] = "MongoDb"
            elif selec == 3: Ruta["NetCore"]['Bases de datos'] = "Postgresql" 
            print("Backend:\n\t1. NetCore\n\t2. Spring Boot\n\t3. NodeJS\n\t4. Express")
            selec = manejoINT()
            if selec == 1: Ruta["NetCore"]['Backend'] = "NetCore"
            elif selec == 2: Ruta["NetCore"]['Backend'] = "Spring Boot"
            elif selec == 3: Ruta["NetCore"]['Backend'] = "NodeJS" 
            elif selec == 4: Ruta["NetCore"]['Backend'] = "Express"
        print("Desea crear otra Ruta?\n\t1. Sí\n\t2. No")
        selec = manejoINT()
        if selec ==1: continue 
        else: 
            print("Rutas Creadas")
            input()
            break

def  registriArea(campers,areas):
    os.system('clear')
    while True:                
        print("Ingrese el documento del Camper:")
        cc = input("")
        if cc in campers:
            if 'inscrito' in campers[cc].values():
                print("Selecione el area de trabajo:\n\t1. Apollo\n\t2. Artemis\n\t3. Sputnik")
                selec = manejoINT()
                if selec == 1:
                    if areas["Apollo"]<= 33:
                        areas["Apollo"] += 1 
                        campers[cc]['Area'] = "Apollo"                    
                    else:
                        print("Area llena, seleccione otra")
                        continue
                elif selec == 2:
                    if areas["Artemis"]<= 33:
                        areas["Artemis"] += 1 
                        campers[cc]['Area'] = "Artemis"                    
                    else:
                        print("Area llena, seleccione otra")
                        continue
                elif selec == 3: 
                    if areas["Sputnik"]<= 33:
                        areas["Sputnik"] += 1 
                        campers[cc]['Area'] = "Sputnik"                    
                    else:
                        print("Area llena, seleccione otra")
                        continue
        print("Desea asignar otra area?\n\t1. Sí\n\t2. No")
        selec = manejoINT()
        if selec ==1: continue 
        else: 
            print("Areas asignadas")
            input()
            break

def registroFecha(campers):

    while True:
        print("ingrese la cc del camper:")
        cc = input("")
        if cc in campers:
            if 'inscrito'in campers[cc].values():
                print("ingrese el dia de ingreso:")
                dia = manejoINT()
                print("ingrese el mes de ingreso:")
                mes = manejoINT()
                print("ingrese el año de ingreso:")
                annio = manejoINT()
                print("ingrese el dia esperado de finalizacion:")
                diaF = manejoINT()
                print("ingrese el mes esperado de finalizacion:")
                mesF = manejoINT()
                print("ingrese el año esperado de finalizacion:")
                annioF = manejoINT()                        
                campers[cc]['Fecha Inicio'] = str(f"{dia}/{mes}/{annio}")
                campers[cc]['Fecha Fin'] = str(f"{diaF}/{mesF}/{annioF}")
            else: print("camper no inscrito")
        else: print("Camper no registrado")
        print("Desea ingresar otra fecga?\n\t1. Sí\n\t2. No")
        selec = manejoINT()
        if selec ==1: continue 
        else: 
            print("fechas Asignadas")
            break