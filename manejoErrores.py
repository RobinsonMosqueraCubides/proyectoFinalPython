def manejoStr():
    while True:
        x = input()
        if x.isalpha():
            return x
        else:
            print("Ingrese solo palabras")

def manejoINT():
    while True:
        try:
            x =float(input())
            return int(x)
        except:
            print("digite un numero")

def manejoNotasDic(asignatura):
    while True:
        try: 
            x=float(input(f"Ingrese la nota de {asignatura}"))
            if x >= 0 and x <= 100:
                return x
            else: 
                print("ingrese un numero de 0 al 100")
                continue
        except:
            print("ingrese un numero valido")