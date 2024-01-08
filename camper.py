import os

def AsignarRuta(campers, Ruta):
    while True:
        os.system('cls')        
        print("Ingrese el documento del Camper:")
        cc = input("")
        if cc in campers:
            print("Seleccione la ruta asignar:\n\t1. NodeJS\n\t2. Java\n\t3. NetCore")
            selec = int(input(""))
            if selec == 1: campers[cc]['ruta']= Ruta['NodeJS']
            elif selec == 2: campers[cc]['ruta']=Ruta['Java']
            elif selec == 3: campers[cc]['ruta']=Ruta['NetCore']
        else: 
            print("Camper no existe")
            continue
        print("Desea Asignar otra ruta?\n\t1. Sí\n\t2. No")
        selec = int(input(""))
        if selec ==1: continue 
        else: 
            print("Rutas Asignadas")
            break

def notaSeleccion(campers):
    while True:
        os.system('cls')
        print(campers)
        print("Ingrese el documento del Camper:")
        cc = input("")
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
    
def notasFiltro(campers):
     os.system('cls')
     notas ={}
     while True:        
        print("Ingrese el documento del Camper:")
        cc = input("")
        if cc in campers:
            if 'notas de filtro' in campers[cc]:
                print("seleccione el modulo:")                
                for i,j in enumerate(campers[cc]['ruta'],start=1):
                    print(f"\t{i}. {j}")
                selec=int(input(""))
                if selec == 1:
                    notas[campers[cc]['ruta'][selec-1]] = {'quiz':float(input("ingrese la nota del quiz")),
                                                           'taller':float(input("ingrese la nota del taller")),
                                                           'PruebaP':float(input("ingrese la nota de la prueba practica")),
                                                           'PruebaT':float(input("ingrese la nota de la prueba teorica"))
                                                           }
                elif selec ==2:
                    notas[campers[cc]['ruta'][selec-1]] = {'quiz':float(input("ingrese la nota del quiz")),
                                                           'taller':float(input("ingrese la nota del taller")),
                                                           'PruebaP':float(input("ingrese la nota de la prueba practica")),
                                                           'PruebaT':float(input("ingrese la nota de la prueba teorica"))}
                elif selec ==3:
                    notas[campers[cc]['ruta'][selec-1]] = {'quiz':float(input("ingrese la nota del quiz")),
                                                           'taller':float(input("ingrese la nota del taller")),
                                                           'PruebaP':float(input("ingrese la nota de la prueba practica")),
                                                           'PruebaT':float(input("ingrese la nota de la prueba teorica"))}
                elif selec ==4:
                    notas[campers[cc]['ruta'][selec-1]] = {'quiz':float(input("ingrese la nota del quiz")),
                                                           'taller':float(input("ingrese la nota del taller")),
                                                           'PruebaP':float(input("ingrese la nota de la prueba practica")),
                                                           'PruebaT':float(input("ingrese la nota de la prueba teorica"))}
                elif selec ==5:
                    notas[campers[cc]['ruta'][selec-1]] = {'quiz':float(input("ingrese la nota del quiz")),
                                                           'taller':float(input("ingrese la nota del taller")),
                                                           'PruebaP':float(input("ingrese la nota de la prueba practica")),
                                                           'PruebaT':float(input("ingrese la nota de la prueba teorica"))}
                elif selec ==6:
                    notas[campers[cc]['ruta'][selec-1]] = {'quiz':float(input("ingrese la nota del quiz")),
                                                           'taller':float(input("ingrese la nota del taller")),
                                                           'PruebaP':float(input("ingrese la nota de la prueba practica")),
                                                           'PruebaT':float(input("ingrese la nota de la prueba teorica"))}
                x = calNotaFinal(notas)
                campers[cc]['notas de filtro'] = x
                
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
     
def campersInscritos(campers):
    print("Cedula\tNombre")
    for i in campers:
        if 'inscrito' in campers[i].values():
            print(f"{i}\t{campers[i]['nombre']}")

def campersBajoRendimiento(campers):
     for i in campers:
         promNotas = campers[i]['notas de filtro']/len(campers[i]['notas de filtro'])
         if promNotas < 60:
             print(f"{i}\t{campers[i]['nombre']}")

def calNotaFinal(notas):
    for i in notas:
        nqt = (notas[i]['quiz']+notas[i]['taller'])/2
        notaFinal = (nqt*0.1)+(notas[i]['PruebaP']*0.6)+(notas[i]['PruebaT']*0.3)
        notas[i]['NotaFinal'] = notaFinal
        return notas



