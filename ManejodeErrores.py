def suma():
    n1= int(input("Numero 1: "))
    n2 = int(input("Numero 2: "))
    print(n1 + n2)
    print("listo")

try:
    #Codigo que se quiere ejecutar
    suma()
except:
    #Codigo que se ejecuta SI hay un error
    print("Algo no ha salido bien")
else:
    #Codigo adicional que se realiza si no hay error
    print("Salio bien")
finally:
    #Codigo que se va a ejecutar de todos modos
    print("Proceso finalizado")
