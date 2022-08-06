def numero_carniceria():
    for c in range(1, 2000):
        yield f"C - {c}"
def numero_charcuteria():
    for c in range(1, 2000):
        yield f"CH - {c}"
def numero_legumbres():
    for c in range(1, 2000):
        yield f"L - {c}"
def numero_farmacia():
    for c in range(1, 2000):
        yield f"F - {c}"
c = numero_carniceria()
ch = numero_charcuteria()
l = numero_legumbres()
f = numero_farmacia()

def decorador(lugar):
    print("\n" + "*" * 23)
    print("Numero de atencion")
    if lugar == "C":
        print("Carniceria")
        print(next(c))
    elif lugar == "CH":
        print("Charcuteria")
        print(next(ch))
    elif lugar == "L":
        print("Legumbres")
        print(next(l))
    else:
        print("Farmacia")
        print(next(f))
    print("\n" + "*" * 23)

