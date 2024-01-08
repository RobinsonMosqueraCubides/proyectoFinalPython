import os
from registro import *
def listaDocenteCamper():
    os.system('cls')
    print("Ruta Java")
    print("\tDocentes:")
    for i in docente:
        if 'Java' in docente[i].values():
            print(f"\t  {i}")
    print("\tCampers:")
    for i in campers:
        if 'Java' in campers[i].values():
            print(f"\t  {campers[i]['nombre']}")
    print("Ruta NodeJS")
    print("\tDocentes:")
    for i in docente:
        if 'NodeJS' in docente[i].values():
            print(f"\t  {i}")
    print("\tCampers:")
    for i in campers:
        if 'NodeJS' in campers[i].values():
            print(f"\t  {campers[i]['nombre']}")
    print("Ruta NetCore")
    print("\tDocentes:")
    for i in docente:
        if 'NetCore' in docente[i].values():
            print(f"\t  {i}")
    print("\tCampers:")
    for i in campers:
        if 'NetCore' in campers[i].values():
            print(f"\t  {campers[i]['nombre']}")

