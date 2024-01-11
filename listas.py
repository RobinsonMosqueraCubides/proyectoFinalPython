import os

def listaDocenteCamper(docente,campers):
    os.system('cls')
    print("Ruta Java")
    print("\tDocentes:")
    for clave in docente:
        for ruta in docente[clave]['Ruta']:
            if ruta == 'Java':
                print(f"Nombre: {clave}")
    print("\tCampers:")
    for clave in campers:
        for ruta in campers[clave]['ruta']:
            if ruta == 'Java':
                print(f"Nombre: {campers[clave]['nombre']}")
    print("Ruta NodeJS")
    print("\tDocentes:")
    for clave in docente:
        for ruta in docente[clave]['Ruta']:
            if ruta == 'NodeJS':
                print(f"\t\tNombre: {clave}")
    print("\tCampers:")
    for clave in campers:
        for ruta in campers[clave]['ruta']:
            if ruta == 'NodeJS':
                print(f"\t\tNombre: {campers[clave]['nombre']}")
    print("Ruta NetCore")
    print("\tDocentes:")
    for clave in docente:
        for ruta in docente[clave]['Ruta']:
            if ruta == 'NetCore':
                print(f"\t\tNombre: {clave}")
    print("\tCampers:")
    for clave in campers:
        for ruta in campers[clave]['ruta']:
            if ruta == 'NetCore':
                print(f"\t\tNombre: {campers[clave]['nombre']}")
    input()

def listarCampersAprobados(docente, campers):
    os.system('cls')
    print("Ruta Java\n\tAprobados\n\t\tCampers:")
    for clave in campers:
        for ruta in campers[clave]['ruta']:
            if ruta == 'Java':
                if 'notas de filtro' in campers[clave]:
                    for j in campers[clave]['notas de filtro']:
                        if 'NotaFinal' in campers[clave]['notas de filtro'][j]:
                                NotaFinal=campers[clave]['notas de filtro'][j]['NotaFinal']
                                if NotaFinal > 60:
                                    print(f"\t\t\tCC: {clave} | Nombre:{campers[clave]['nombre']} | Modulo: {j} | Nota: {NotaFinal}")

    print("\t\tDocentes:")
    for clave in docente:
        for ruta in docente[clave]['Ruta']:
            if ruta == 'Java':
                print(f"\t\t\tNombre: {clave}")
    print("\tReprobados:\n\t\tCampers:")
    for clave in campers:
        for ruta in campers[clave]['ruta']:
            if ruta == 'Java':
                if 'notas de filtro' in campers[clave]:
                    for j in campers[clave]['notas de filtro']:
                        if 'NotaFinal' in campers[clave]['notas de filtro'][j]:
                                NotaFinal=campers[clave]['notas de filtro'][j]['NotaFinal']
                                if NotaFinal < 60:
                                    print(f"\t\t\tCC: {clave} | Nombre:{campers[clave]['nombre']} | Modulo: {j} | Nota: {NotaFinal}")
    
    print("Ruta NodeJS\n\tAprobados\n\t\tCampers:")
    for clave in campers:
        for ruta in campers[clave]['ruta']:
            if ruta == 'NodeJS':
                if 'notas de filtro' in campers[clave]:
                    for j in campers[clave]['notas de filtro']:
                        if 'NotaFinal' in campers[clave]['notas de filtro'][j]:
                                NotaFinal=campers[clave]['notas de filtro'][j]['NotaFinal']
                                if NotaFinal > 60:
                                    print(f"\t\t\tCC: {clave} | Nombre:{campers[clave]['nombre']} | Modulo: {j} | Nota: {NotaFinal}")

    print("\t\tDocentes:")
    for clave in docente:
        for ruta in docente[clave]['Ruta']:
            if ruta == 'NodeJS':
                print(f"\t\t\tNombre: {clave}")
    print("\tReprobados:\n\t\tCampers:")
    for clave in campers:
        for ruta in campers[clave]['ruta']:
            if ruta == 'NodeJS':
                if 'notas de filtro' in campers[clave]:
                    for j in campers[clave]['notas de filtro']:
                        if 'NotaFinal' in campers[clave]['notas de filtro'][j]:
                                NotaFinal=campers[clave]['notas de filtro'][j]['NotaFinal']
                                if NotaFinal < 60:
                                    print(f"\t\t\tCC: {clave} | Nombre:{campers[clave]['nombre']} | Modulo: {j} | Nota: {NotaFinal}")

    print("Ruta NetCore\n\tAprobados\n\t\tCampers:")
    for clave in campers:
        for ruta in campers[clave]['ruta']:
            if ruta == 'NetCore':
                if 'notas de filtro' in campers[clave]:
                    for j in campers[clave]['notas de filtro']:
                        if 'NotaFinal' in campers[clave]['notas de filtro'][j]:
                                NotaFinal=campers[clave]['notas de filtro'][j]['NotaFinal']
                                if NotaFinal > 60:
                                    print(f"\t\t\tCC: {clave} | Nombre:{campers[clave]['nombre']} | Modulo: {j} | Nota: {NotaFinal}")

    print("\t\tDocentes:")
    for clave in docente:
        for ruta in docente[clave]['Ruta']:
            if ruta == 'NetCore':
                print(f"\t\t\tNombre: {clave}")
    print("\tReprobados:\n\t\tCampers:")
    for clave in campers:
        for ruta in campers[clave]['ruta']:
            if ruta == 'NetCore':
                if 'notas de filtro' in campers[clave]:
                    for j in campers[clave]['notas de filtro']:
                        if 'NotaFinal' in campers[clave]['notas de filtro'][j]:
                                NotaFinal=campers[clave]['notas de filtro'][j]['NotaFinal']
                                if NotaFinal < 60:
                                    print(f"\t\t\tCC: {clave} | Nombre:{campers[clave]['nombre']} | Modulo: {j} | Nota: {NotaFinal}")
    input()