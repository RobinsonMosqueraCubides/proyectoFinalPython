import os

def listaDocenteCamper(docente,campers):
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
    input()

def listarCampersAprobados(docente, campers):
    os.system('cls')
    print("Ruta Java\n\tAprobados\n\t\tCampers:")
    for i in campers:
        if 'Java' in campers[i].values():
            for j in campers[i]['notas de filtro']:
                if campers[i]['notas de filtro'][j]['NotaFinal'] >= 60:
                    print(f"\t\t\tNombre: {campers[i]['nombre']} | Modulo:{campers[i]['notas de filtro'][j]} | Nota: {campers[i]['notas de filtro'][j]['NotaFinal']}")
    print("\t\tDocentes:")
    for i in docente:
        if 'Java' in docente[i]:
            print(f"\t\t\t{i}")
    print("\tReprobados:")
    for i in campers:
        if 'Java' in campers[i].values():
            for j in campers[i]['notas de filtro']:
                if campers[i]['notas de filtro'][j]['NotaFinal'] < 60:
                    print(f"\t\t\tNombre: {campers[i]['nombre']} | Modulo:{campers[i]['notas de filtro'][j]} | Nota: {campers[i]['notas de filtro'][j]['NotaFinal']}")
    print("\t\tDocentes:")
    for i in docente:
        if 'Java' in docente[i]:
            print(f"\t\t\t{i}")
    
    print("Ruta NodeJS\n\tAprobados\n\t\tCampers:")
    for i in campers:
        if 'NodeJS' in campers[i].values():
            for j in campers[i]['notas de filtro']:
                if campers[i]['notas de filtro'][j]['NotaFinal'] >= 60:
                    print(f"\t\t\tNombre: {campers[i]['nombre']} | Modulo:{campers[i]['notas de filtro'][j]} | Nota: {campers[i]['notas de filtro'][j]['NotaFinal']}")
    print("\t\tDocentes:")
    for i in docente:
        if 'NodeJS' in docente[i]:
            print(f"\t\t\t{i}")
    print("\tReprobados:")
    for i in campers:
        if 'NodeJS' in campers[i].values():
            for j in campers[i]['notas de filtro']:
                if campers[i]['notas de filtro'][j]['NotaFinal'] < 60:
                    print(f"\t\t\tNombre: {campers[i]['nombre']} | Modulo:{campers[i]['notas de filtro'][j]} | Nota: {campers[i]['notas de filtro'][j]['NotaFinal']}")
    print("\t\tDocentes:")
    for i in docente:
        if 'NodeJS' in docente[i]:
            print(f"\t\t\t{i}")

    print("Ruta NetCore\n\tAprobados\n\t\tCampers:")
    for i in campers:
        if 'NetCore' in campers[i].values():
            for j in campers[i]['notas de filtro']:
                if campers[i]['notas de filtro'][j]['NotaFinal'] >= 60:
                    print(f"\t\t\tNombre: {campers[i]['nombre']} | Modulo:{campers[i]['notas de filtro'][j]} | Nota: {campers[i]['notas de filtro'][j]['NotaFinal']}")
    print("\t\tDocentes:")
    for i in docente:
        if 'NetCore' in docente[i]:
            print(f"\t\t\t{i}")
    print("\tReprobados:")
    for i in campers:
        if 'NetCore' in campers[i].values():
            for j in campers[i]['notas de filtro']:
                if campers[i]['notas de filtro'][j]['NotaFinal'] < 60:
                    print(f"\t\t\tNombre: {campers[i]['nombre']} | Modulo:{campers[i]['notas de filtro'][j]} | Nota: {campers[i]['notas de filtro'][j]['NotaFinal']}")
    print("\t\tDocentes:")
    for i in docente:
        if 'NetCore' in docente[i]:
            print(f"\t\t\t{i}")
    input()