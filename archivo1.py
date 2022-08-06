# """
# Este es un archivo que imprime
# """
#
#
# def una_func():
#     """
#     Esto es una
#     :rtype: object
#
#     """
#     numero1 = 500
#     print(numero1)
#
#
# una_func()
# print("Todo bien")
lista = [1,2,3,4,5,20]
lista1 = []
lista.sort()
for i in lista:
    if i < 10:
        print(i)
        lista1.append(i)
for i in lista1:
    lista.remove(i)
print(lista1)
print(lista)



