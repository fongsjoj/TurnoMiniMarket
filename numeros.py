def numeros_perfumeria():
    for n in range(1, 10000):
        yield f"P - {n}"

def numeros_farmacia():
    for n in range(1, 10000):
        yield f"F - {n}"
def numeros_cosmetica():
    for n in range(1, 10000):
        yield f"C - {n}"

p = numeros_perfumeria()
f = numeros_farmacia()
c = numeros_cosmetica()

def decorador(rubro):
    print("\n"  + "*" * 23)
    print("Su numero es : ")
    if rubro == "P" or rubro == "p":
        print(next(p))
    elif rubro == "F" or rubro == "f":
        print(next(f))
    else:
        print(next(c))
    print("Aguarde y sera atendido")
    print("*" * 23 + "\n")
# resp = "s"
# while resp != "n" and resp != "N":
#     print("\n Indique a que area quiere un numero \n")
#     opcion = input("(P)perfumeria (F) Farmacia (C) Cosmetica ")
#     decorador(opcion)
#     resp = input("Desea continuar (s/n)?: ")


