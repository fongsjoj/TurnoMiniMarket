def pedir_numero():

    while True:
        try:
            numero = int(input("Ingrese un numero:  "))
        except:
            print("No ingresaste un numero")
        else:
            print(f'Ingresaste el numero:  {numero}')
            break
    print('Finalizo')
pedir_numero()