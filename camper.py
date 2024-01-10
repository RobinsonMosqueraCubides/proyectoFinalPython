import os
from manejoErrores import *
def AsignarRuta(campers, Ruta):
    while True:
        os.system('clear')   
        
        print(campers)     
        print("Ingrese el documento del Camper:")
        cc = input("")
        print(cc)
        
        rutaCamper = {}        
        if cc in campers:
            print("Seleccione la ruta asignar:\n\t1. NodeJS\n\t2. Java\n\t3. NetCore")
            selec = manejoINT()
            if selec == 1: campers[cc]['ruta']= rutaCamper['NodeJS']=Ruta['NodeJS']
            elif selec == 2: campers[cc]['ruta']=rutaCamper['Java']=Ruta['Java']
            elif selec == 3: campers[cc]['ruta']=rutaCamper['NetCore']=Ruta['NetCore']
        else: 
            print("Camper no existe")
            continue
        print("Desea Asignar otra ruta?\n\t1. Sí\n\t2. No")
        selec = manejoINT()
        if selec ==1: continue 
        else: 
            print("Rutas Asignadas")
            break

def notaSeleccion(campers):
    while True:
        os.system('clear')
        
        print("Ingrese el documento del Camper:")
        cc = input("")
        if cc in campers:
                #print("Ingrese la Nota del camper")
                nota = manejoNotasDic('Nota de Seleccion')
                if nota >= 60:
                    campers[cc]['estado']='Aprobado'
                    campers[cc]['notas de filtro']=None
                else:
                    campers[cc]['estado']='inscrito'
        else: 
            print("Camper no existe")
            continue
        print("Desea ingresar otra nota?\n\t1. Sí\n\t2. No")
        selec = manejoINT()
        if selec ==1: continue 
        else: 
            print("Notas Asignadas")
            break
    
def notasFiltro(campers):
     os.system('clear')
     notas ={}
     while True:        
        print("Ingrese el documento del Camper:")
        cc = input("")
        if cc in campers:
            if 'notas de filtro' in campers[cc]:
                print("seleccione el modulo:")                
                for i,j in enumerate(campers[cc]['ruta'],start=1):
                    print(f"\t{i}. {j}")
                selec=manejoINT()
                if selec == 1:
                    notas[campers[cc]['ruta'][selec-1]] = {'quiz':manejoNotasDic('quiz'),
                                                           'taller':manejoNotasDic('taller'),
                                                           'PruebaP':manejoNotasDic('Prueba Practica'),
                                                           'PruebaT':manejoNotasDic('Prueba Teorica')
                                                           }
                elif selec ==2:
                    notas[campers[cc]['ruta'][selec-1]] = {'quiz':manejoNotasDic('quiz'),
                                                           'taller':manejoNotasDic('taller'),
                                                           'PruebaP':manejoNotasDic('Prueba Practica'),
                                                           'PruebaT':manejoNotasDic('Prueba Teorica')
                                                           }
                elif selec ==3:
                    notas[campers[cc]['ruta'][selec-1]] = {'quiz':manejoNotasDic('quiz'),
                                                           'taller':manejoNotasDic('taller'),
                                                           'PruebaP':manejoNotasDic('Prueba Practica'),
                                                           'PruebaT':manejoNotasDic('Prueba Teorica')
                                                           }
                elif selec ==4:
                    notas[campers[cc]['ruta'][selec-1]] = {'quiz':manejoNotasDic('quiz'),
                                                           'taller':manejoNotasDic('taller'),
                                                           'PruebaP':manejoNotasDic('Prueba Practica'),
                                                           'PruebaT':manejoNotasDic('Prueba Teorica')
                                                           }
                elif selec ==5:
                    notas[campers[cc]['ruta'][selec-1]] = {'quiz':manejoNotasDic('quiz'),
                                                           'taller':manejoNotasDic('taller'),
                                                           'PruebaP':manejoNotasDic('Prueba Practica'),
                                                           'PruebaT':manejoNotasDic('Prueba Teorica')
                                                           }
                elif selec ==6:
                    notas[campers[cc]['ruta'][selec-1]] = {'quiz':manejoNotasDic('quiz'),
                                                           'taller':manejoNotasDic('taller'),
                                                           'PruebaP':manejoNotasDic('Prueba Practica'),
                                                           'PruebaT':manejoNotasDic('Prueba Teorica')
                                                           }
                x = calNotaFinal(notas)
                campers[cc]['notas de filtro'] = x
                
            else:
                print("Camper no inscrito")
                continue
        else:
            print("Camper no existe")
            continue
        print("Desea ingresar otra nota?\n\t1. Sí\n\t2. No")
        selec = manejoINT()
        if selec ==1: continue 
        else: 
            print("Notas Asignadas")
            break
     
def campersInscritos(campers):
    print("Cedula\tNombre")
    for i in campers:
        if 'inscrito' in campers[i].values():
            print(f"{i}\t{campers[i]['nombre']}")
    input()

def campersBajoRendimiento(campers):
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
        return notas



