"""
Funcion de funciones. se tiene una funcion que contiene 2 funciones y se retorna una
funcion de acuerdo al nombre (may o min) que viene en tipo
"""

def cambiar_letras(tipo):

    def mayuscula(texto):
        print(texto.upper())

    def minuscula(texto):
        print(texto.lower())

    if tipo == "may":
        return mayuscula
    elif tipo == "min":
        return minuscula

operacion = cambiar_letras('may')

#la variable operacion se convierte en una variable de funcion que se le puede colocar un
#atributo y ejecutarse como si fuera una funcion

operacion('cambio de letra')

