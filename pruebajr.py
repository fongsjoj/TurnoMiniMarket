#### EJERCICIO TIPO PARA PRUEBAS JUNIOR DE PYTHON ***********
#1) Invertir una cadena
#Dado cualquier string invertir el string y mostrarlo
"""a="esta es la prueba"
b=list(a)
b.reverse()
a="".join(b)
print(a)"""
"""#2) cuantas veces se repite un caracter en una cadena

a = "klsldkk45fll4467opfogofofeaasqw9331234567890"
b = list(a)
print(b.count("k"))"""
"""#3)Distancia de Hamming
texto1 ="paracaida"
texto2 ="panaderia"
distancia = 0
if (len(texto1)) != (len(texto2)):
    print(("Longitudes distintas"))
else:
    #COMO RECORRER UNA CADENA CON UN  BUCLE  -----    F   O   R   --------
    for i in range(len(texto1)):
        if texto1[i] != texto2[i]:
            distancia += 1
    print(distancia)"""
"""#4) Contar el numero de palabras en una cadena
texto =  "el      cura,        el         del       abrigo      negro,      es de la pedrera y tenia frio"
a = len(texto.split())
print(a)"""
#5) Cuantos numeros hay en una cadena
a = "klsldkk45fll4467opfogofofeaasqw9331234567890"
n = len(a.count())



