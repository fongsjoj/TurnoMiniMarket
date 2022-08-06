def suma():
    n1= int(input("Numero 1: "))
    n2 = int(input("Numero 2: "))
    print(n1 + n2)
    print("listo" + n1)

try:
    #Codigo que se quiere ejecutar
    suma()
except TypeError:
    #Codigo que se ejecuta SI hay un error
    print("Estas intentando concatenar tipos distintos")
except ValueError:
    print("Uno de los valores no es numerico ")
else:
    #Codigo adicional que se realiza si no hay error
    print("Salio bien")
finally:
    #Codigo que se va a ejecutar de todos modos
    print("Proceso finalizado")
