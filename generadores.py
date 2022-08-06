"""def mi_funcion():
    return 4
def mi_generador():
    yield  4
print(mi_funcion())
print(mi_generador())
g = mi_generador()
print(next(g))
#Si despues de imprimir la el generador se quiere imprimir de nuevo el generador, se
# produce un error
"""
def mi_funcion():
    lista = []
    for x in range(1, 5):
        lista.append(x * 10)
    return lista
def mi_generador():
    for x in range(1, 5):
        yield  x * 10
print(mi_funcion())
print(mi_generador())
g = mi_generador()
print(next(g))
print(next(g))