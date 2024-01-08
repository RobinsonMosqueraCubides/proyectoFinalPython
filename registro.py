import os
campers = {123:{'nombre':'Robin','direccion':'asdasd','acudiente':'acudiente','tel':'tel','estado':'estado','ruta':'Sin Ruta'}}
docente = {}
Ruta = {'NodeJS':["PSeInt","Python"],'Java':["PSeInt","Python"],'NetCore':["PSeInt","Python"]}

def registroCampers():
    
    while True:
        os.system('cls')
        print("Ingrese el numero de identificacion:")
        cc = input("")
        print("Ingrese el nombre:")
        nombre = input("")
        print("Ingrese la direccion:")
        direccion = input("")
        print("Ingrese la edad:")
        edad = int(input(""))
        if edad >= 18: acudiente = None                
        else:
            acudiente = [] 
            print("Ingrese el nombre del acudiente:")
            acudiente.append(input(""))
            print("Ingrese el telefono del acudiente:")
            acudiente.append(input(""))
        print("Ingrese el Numero de telefono:")
        tel = []
        tel.append(input(""))
        print("Desea agregar otro numero?\n\t1. Sí\n\t2. No")
        selec = int(input(""))
        if selec ==1: tel.append(input(""))
        estado = "PreInscrito"
        datos = {'nombre':nombre,'direccion':direccion,'acudiente':acudiente,'tel':tel,'estado':estado}
        campers[cc] = datos
        print("Desea registrar otro camper?\n\t1. Sí\n\t2. No")
        selec = int(input(""))
        if selec ==1: continue 
        else: 
            print("Campers registrados")
            break
        
def registroDocente():
    while True:
        os.system('cls')
        print("Ingrese el nombre:")
        nombre = input("")
        print("Seleccione el horario del docente:\n\t1. 6am a 10am\n\t2. 10am a 2 pm\n\t3. 2pm a 6 pm\n\t4. 6pm a 10 pm")
        selec = int(input(""))
        if selec == 1: Horario="6am a 10am"
        elif selec == 2: Horario="10am a 2pm"
        elif selec == 3: Horario="2pm a 6pm"
        elif selec == 4: Horario="6am a 10pm"
        print("Selecione el area de trabajo:\n\t1. Apollo\n\t2. Artemis\n\t3. Sputnik")
        selec = int(input(""))
        if selec == 1: Area="Apollo"
        elif selec == 2: Area="Artemis"
        elif selec == 3: Area="Sputnik"
        print("Selecione la ruta:\n\t1. NodeJS\n\t2. Java\n\t3. NetCore")
        selec = int(input(""))
        if selec == 1: ruta="NodeJS"
        elif selec == 2: ruta="Java"
        elif selec == 3: ruta="NetCore"
        docente[nombre] = {'Ruta':Ruta[ruta], 
                        'Horario':Horario, 
                        'Area':Area}
        print("Desea registrar otro docente?\n\t1. Sí\n\t2. No")
        selec = int(input(""))
        if selec ==1: continue 
        else: 
            print("docentes registrados")
            break

def registroRutas():#Crear una funcion que evalue si ya la ruta fue creada
    while True:
        os.system('cls')
        print("Selecione La ruta que desea crear:\n\t1. NodeJS\n\t2. Java\n\t3. NetCore")
        selec = int(input(""))
        if selec == 1: 
            print("Programación Web:\n\t1. HTML\n\t2. CSS\n\t3. Bootstrap")
            selec = int(input(""))
            if selec == 1: Ruta["NodeJS"].append("HTML")
            elif selec == 2: Ruta["NodeJS"].append("CSS")
            elif selec == 3: Ruta["NodeJS"].append("Bootstrap")
            print("Programación formal:\n\t1. Java\n\t2. JavaScript\n\t3. C#")
            selec = int(input(""))
            if selec == 1: Ruta["NodeJS"].append("Java")
            elif selec == 2: Ruta["NodeJS"].append("JavaScript")
            elif selec == 3: Ruta["NodeJS"].append("C#") 
            print("Bases de datos:\n\t1. Mysql\n\t2. MongoDb\n\t3. Postgresql")
            selec = int(input(""))
            if selec == 1: Ruta["NodeJS"].append("Mysql")
            elif selec == 2: Ruta["NodeJS"].append("MongoDb")
            elif selec == 3: Ruta["NodeJS"].append("Postgresql") 
            print("Backend:\n\t1. NetCore\n\t2. Spring Boot\n\t3. NodeJS\n\t4. Express")
            selec = int(input(""))
            if selec == 1: Ruta["NodeJS"].append("NetCore")
            elif selec == 2: Ruta["NodeJS"].append("Spring Boot")
            elif selec == 3: Ruta["NodeJS"].append("NodeJS") 
            elif selec == 4: Ruta["NodeJS"].append("Express") 
            
        elif selec == 2:
            print("Programación Web:\n\t1. HTML\n\t2. CSS\n\t3. Bootstrap")
            selec = int(input(""))
            if selec == 1: Ruta["Java"].append("HTML")
            elif selec == 2: Ruta["Java"].append("CSS")
            elif selec == 3: Ruta["Java"].append("Bootstrap")
            print("Programación formal:\n\t1. Java\n\t2. JavaScript\n\t3. C#")
            selec = int(input(""))
            if selec == 1: Ruta["Java"].append("Java")
            elif selec == 2: Ruta["Java"].append("JavaScript")
            elif selec == 3: Ruta["Java"].append("C#") 
            print("Bases de datos:\n\t1. Mysql\n\t2. MongoDb\n\t3. Postgresql")
            selec = int(input(""))
            if selec == 1: Ruta["Java"].append("Mysql")
            elif selec == 2: Ruta["Java"].append("MongoDb")
            elif selec == 3: Ruta["Java"].append("Postgresql") 
            print("Backend:\n\t1. NetCore\n\t2. Spring Boot\n\t3. NodeJS\n\t4. Express")
            selec = int(input(""))
            if selec == 1: Ruta["Java"].append("NetCore")
            elif selec == 2: Ruta["Java"].append("Spring Boot")
            elif selec == 3: Ruta["Java"].append("NodeJS") 
            elif selec == 4: Ruta["Java"].append("Express")
        elif selec == 3: 
            print("Programación Web:\n\t1. HTML\n\t2. CSS\n\t3. Bootstrap")
            selec = int(input(""))
            if selec == 1: Ruta["NetCore"].append("HTML")
            elif selec == 2: Ruta["NetCore"].append("CSS")
            elif selec == 3: Ruta["NetCore"].append("Bootstrap")
            print("Programación formal:\n\t1. Java\n\t2. JavaScript\n\t3. C#")
            selec = int(input(""))
            if selec == 1: Ruta["NetCore"].append("Java")
            elif selec == 2: Ruta["NetCore"].append("JavaScript")
            elif selec == 3: Ruta["NetCore"].append("C#")
            print("Bases de datos:\n\t1. Mysql\n\t2. MongoDb\n\t3. Postgresql")
            selec = int(input(""))
            if selec == 1: Ruta["NetCore"].append("Mysql")
            elif selec == 2: Ruta["NetCore"].append("MongoDb")
            elif selec == 3: Ruta["NetCore"].append("Postgresql") 
            print("Backend:\n\t1. NetCore\n\t2. Spring Boot\n\t3. NodeJS\n\t4. Express")
            selec = int(input(""))
            if selec == 1: Ruta["NetCore"].append("NetCore")
            elif selec == 2: Ruta["NetCore"].append("Spring Boot")
            elif selec == 3: Ruta["NetCore"].append("NodeJS") 
            elif selec == 4: Ruta["NetCore"].append("Express")
        print("Desea crear otra Ruta?\n\t1. Sí\n\t2. No")
        selec = int(input(""))
        if selec ==1: continue 
        else: 
            print("Rutas Creadas")
            break

