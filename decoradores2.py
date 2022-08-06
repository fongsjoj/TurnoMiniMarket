def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print('hola')
        funcion(palabra)
        print('adios')
    return  otra_funcion

def mayusculas(texto):
    print(texto.upper())

def minusculas(texto):
    print(texto.lower())

variabledecorar = decorar_saludo(mayusculas)

variabledecorar("otra cosa")

mayusculas("lo que sea")