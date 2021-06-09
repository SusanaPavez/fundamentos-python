# Cuenta regresiva : crea una función que acepte un número como entrada. 
# Devuelve una nueva lista que cuenta hacia atrás en uno, desde el número 
# (como el elemento 0) hasta 0 (como el último elemento).
# Ejemplo: la cuenta regresiva (5) debería devolver [5,4,3,2,1,0]

from typing import Counter


def cuentaRegresiva(entrada):
    lista = []
    for x in range (entrada, -1, -1):
        lista.append(x)
    return lista
print (cuentaRegresiva(5))



# Imprimir y volver : crea una función que recibirá una lista con dos números. Imprima el primer valor y devuelva el segundo.
# Ejemplo: print_and_return ([1,2]) debería imprimir 1 y devolver 2

def print_and_return(lista):
    print (lista[0])
    return(lista[1])
lista = [1,2]
print (print_and_return(lista))



# First Plus Length : crea una función que acepta una lista y devuelve la suma del primer valor de la lista más la longitud de la lista.
# Ejemplo: first_plus_length ([1,2,3,4,5]) debería devolver 6 (primer valor: 1 + longitud: 5)


def first_plus_length(lista):
    x=lista[0]+len(lista)
    return x
lista= [1,2,3,4,5]
print (first_plus_length(lista))



# Valores mayores que el segundo : escribe una función que acepte una lista y 
# crea una nueva lista que contenga solo los valores de la lista original que sean
#  mayores que su segundo valor. Imprima cuántos valores son y luego devuelva la 
# nueva lista. Si la lista tiene menos de 2 elementos, haga que la función devuelva False

# Ejemplo: values_greater_than_second ([5,2,3,2,1,4]) debería imprimir 3 y devolver [5,3,4]
# Ejemplo: values_greater_than_second ([3]) debería devolver False

def valuesgreaterthansecond(lista):
    if(len(lista))<2:
        return False
    else:
        for x in range (0, len(lista)+1):
            if(lista[x]>lista[1]):
                print (lista[x])
lista= [5,2,3,2,1,4]
print (valuesgreaterthansecond(lista))



# Esta longitud, ese valor : escribe una función que acepte dos enteros como parámetros: tamaño y valor.
# La función debe crear y devolver una lista cuya longitud es igual al tamaño dado y cuyos valores son 
# todos los valores dados.
# Ejemplo: length_and_value (4,7) debería devolver [7,7,7,7]
# Ejemplo: length_and_value (6,2) debería devolver [2,2,2,2,2,2]


    # hay que hacer un ciclo que meta un append basado en el primer número.

# ESTO FUNCIONA, HAY QUE METERLO A UNA FUNCIÓN

# lista=[4,7]
# x = 1
# while x < lista[0]:
#     lista.append(lista[1])
#     x += 1
# print(lista)

def length_and_value(lista):
    x = 1
    while x < lista[0]:
        lista.append(lista[1])
        x += 1
    return lista
lista=[4,7]
print (length_and_value(lista))