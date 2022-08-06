# def secuencia_infinita():
#     num = 0
#     while True:
#         num += 1
#         yield num
# generador = secuencia_infinita()
# print(next(generador))
# def indefinida():
#     num = 1
#     while True:
#         yield 7 * num
#         num+=1
# generador = indefinida()
# print(next(generador))
# print(next(generador))
# def personaje():
#     num = 3
#     while num >= 0:
#         if num !=0:
#             x = (f"Te quedan {num} vidas ")
#         else:
#             x = ("Game Over")
#         yield x
#         num -= 1
# perder_vida = personaje()
# print(next(perder_vida))
# print(next(perder_vida))
# print(next(perder_vida))
# print(next(perder_vida))

def mensaje():
    x = "Te quedan 3 vidas"
    yield x
    x = "Te quedan 2 vidas"
    yield x
    x = "Te queda 1 vida"
    yield x
    x = "Game Over"
    yield x
perder_vida = mensaje()
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))

