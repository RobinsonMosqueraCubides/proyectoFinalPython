import os
from manejoErrores import *
def AsignarRuta(campers, Ruta):
    while True:
        os.system('cls')        
        print("Ingrese el documento del Camper:")
        cc = input("")
        if cc in campers:
            print("Seleccione la ruta asignar:\n\t1. NodeJS\n\t2. Java\n\t3. NetCore")
            selec = manejoINT()
            if selec == 1: campers[cc]['ruta']= {"NodeJS": Ruta.get("NodeJS", {})}
            elif selec == 2: campers[cc]['ruta']={"Java": Ruta.get("Java", {})}
            elif selec == 3: campers[cc]['ruta']={"NetCore": Ruta.get("NetCore", {})}
        else: 
            print("Camper no existe")
            continue
        print("Desea Asignar otra ruta?\n\t1. Sí\n\t2. No")
        selec = manejoINT()
        if selec ==1: continue 
        else: 
            print("Rutas Asignadas")
            input()
            break

def notaSeleccion(campers):
    while True:
        os.system('cls')
        #print(campers)
        print("Ingrese el documento del Camper:")
        cc = input("")
        if cc in campers:
                #print("Ingrese la Nota del camper")
                nota = manejoNotasDic('Nota de Seleccion')
                if nota >= 60:
                    campers[cc]['estado']='inscrito'
                    campers[cc]['notas de filtro']=[]
                else:
                    campers[cc]['estado']='No inscrito'
        else: 
            print("Camper no existe")
            continue
        print("Desea ingresar otra nota?\n\t1. Sí\n\t2. No")
        selec = manejoINT()
        if selec ==1: continue 
        else: 
            print("Notas Asignadas")
            input()
            break
    
def notasFiltro(campers):
     os.system('cls')
     notas ={}
     while True:        
        print("Ingrese el documento del Camper:")
        cc = input("")
        if cc in campers:
            if 'notas de filtro' in campers[cc]:
                if 'ruta' in campers[cc]:
                    print("seleccione el modulo:")  
                    cont=0              
                    for ruta in campers[cc]['ruta']:                        
                        for modulo in campers[cc]['ruta'][ruta]:
                        # print(modulo)
                            cont+=1
                            print(f"{cont}. {campers[cc]['ruta'][ruta][modulo]}")
                    selec=manejoINT()
                    if selec == 1:
                        notas['Fundamentos'] = {'quiz':manejoNotasDic('quiz'),
                                                            'taller':manejoNotasDic('taller'),
                                                            'PruebaP':manejoNotasDic('Prueba Practica'),
                                                            'PruebaT':manejoNotasDic('Prueba Teorica')
                                                            }
                    elif selec ==2:
                        notas['Programacion Web'] = {'quiz':manejoNotasDic('quiz'),
                                                            'taller':manejoNotasDic('taller'),
                                                            'PruebaP':manejoNotasDic('Prueba Practica'),
                                                            'PruebaT':manejoNotasDic('Prueba Teorica')
                                                            }
                    elif selec ==3:
                        notas['Programacion formal'] = {'quiz':manejoNotasDic('quiz'),
                                                            'taller':manejoNotasDic('taller'),
                                                            'PruebaP':manejoNotasDic('Prueba Practica'),
                                                            'PruebaT':manejoNotasDic('Prueba Teorica')
                                                            }
                    elif selec ==4:
                        notas['Bases de datos'] = {'quiz':manejoNotasDic('quiz'),
                                                            'taller':manejoNotasDic('taller'),
                                                            'PruebaP':manejoNotasDic('Prueba Practica'),
                                                            'PruebaT':manejoNotasDic('Prueba Teorica')
                                                            }
                    elif selec ==5:
                        notas['Backend'] = {'quiz':manejoNotasDic('quiz'),
                                                            'taller':manejoNotasDic('taller'),
                                                            'PruebaP':manejoNotasDic('Prueba Practica'),
                                                            'PruebaT':manejoNotasDic('Prueba Teorica')
                                                            }
                else:
                    print("Camper sin Ruta, asigna una ruta")
                    input()
                    break    
                calNotaFinal(notas)
                if selec == 1 : campers[cc]['notas de filtro'] = {"Fundamentos": notas.get("Fundamentos", {})}
                elif selec == 2 : campers[cc]['notas de filtro'] = {'Programacion Web': notas.get('Programacion Web', {})}
                elif selec == 3 : campers[cc]['notas de filtro'] = {'Programacion formal': notas.get('Programacion Web', {})}
                elif selec == 4 : campers[cc]['notas de filtro'] = {'Bases de datos': notas.get('Programacion Web', {})}
                elif selec == 5 : campers[cc]['notas de filtro'] = {'Backend': notas.get('Programacion Web', {})}
                
                
                
            else:
                print("Camper no inscrito")
                input()
                continue
        else:
            print("Camper no existe")
            input()
            continue
        print("Desea ingresar otra nota?\n\t1. Sí\n\t2. No")
        selec = manejoINT()
        if selec ==1: continue 
        else: 
            print("Notas Asignadas")
            input()
            break
     
def campersInscritos(campers):
    print("Cedula\tNombre")
    for i in campers:
        if 'inscrito' in campers[i].values():
            print(f"{i}\t{campers[i]['nombre']}")
    input()

def campersBajoRendimiento(campers):
    print("campers con bajo rendimiento")
    for i in campers:
        if 'notas de filtro' in campers[i]:
            for j in campers[i]['notas de filtro']:
                if 'NotaFinal' in campers[i]['notas de filtro'][j]:
                    NotaFinal=campers[i]['notas de filtro'][j]['NotaFinal']
                    if NotaFinal < 60:
                        print(f"CC: {i} | Nombre:{campers[i]['nombre']} | Modulo: {j} | Nota: {NotaFinal}")
    input()

def calNotaFinal(notas):
    for i in notas:
        nqt = (notas[i]['quiz']+notas[i]['taller'])/2
        notaFinal = (nqt*0.1)+(notas[i]['PruebaP']*0.6)+(notas[i]['PruebaT']*0.3)
        notas[i]['NotaFinal'] = notaFinal

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
            input()
            break
        



