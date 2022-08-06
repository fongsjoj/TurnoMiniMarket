import selecPro81
import  os
def pedir_seleccion():
    print("\tBienvenido al MiniMarket Detodo")
    print("\t----------------------------------")
    while True:
        print("[C] Carniceria – [Ch] Charcuteria – [L] Legumbres – [F] Farmacia - [S] Salir")
        try:
            opcion = input("Para tomar un numero escoja un Area: ").upper()
            ["C","CH","L","F","S"].index(opcion)
        except:
            print("Esa no es una opcion valida")
        else:
            break
    if opcion != "S":
        selecPro81.decorador(opcion)
def inicio():
    while True:
        os.system('cls')
        pedir_seleccion()
        try:
            turno = input("¿Quiere tomar otro turno: [S] [N]?").upper()
            ["S","N"].index(turno)
        except:
            print("Opcion no es valida: ")
        else:
            if turno == "N":
                os.system('cls')
                print("\n" + "*" * 23)
                print("Gracias por visitar a su Minimarket Detodo")
                print("\n" + "*" * 23)
                break
inicio()
