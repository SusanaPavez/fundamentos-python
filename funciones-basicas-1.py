#1
def a():
    return 5
print(a())
# da como resultado 5


#2
def a():
    return 5
print(a()+a())
# da como resultado 10


#3
def a():
    return 5
    return 10
print(a())
# devuelve 5. Hay un tema con la indentación


#4
def a():
    return 5
    print(10)
print(a())
# devuelve 5. Hay un tema con la indentación


#5
def a():
    print(5)
x = a()
print(x)
# la x en estos momentos es 5. Por lo tanto en estos momentos debería imprimir 5



#6
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))
# daría como resultado 3 + 5 = 8



#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5))
# Hay algo raro aquí



#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
        return 7
print(a())
# Esto devuelve 100 y 10


#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3 # no está en la misma indentación y de todas formas el return sale de la función, así que esto queda en el limbo
print(a(2,3)) # devuelve 7
print(a(5,3)) # devuelve 14
print(a(2,3) + a(5,3)) # devuelve 21
# Esto devuelve 7, 14, 21


#10
def a(b,c):
    return b+c # 3+5=8
    return 10 # tiene un tema con la indentación, debería estar más atrás porque ya pidió un return. Si fuera de otra forma, sería return b+c, 10
print(a(3,5))
# Esto devuelve 8



#11
b = 500
print(b) # 500
def a():
    b = 300
    print(b) # ahora es 300. Pero no se imprime porque no se llama.
print(b) # 300
a() # 300. Aquí sí se llama a la función
print(b) #300
# debería ser 500, 500, 300, 300 



#12
b = 500
print(b) # 500
def a():
    b = 300
    print(b) # 300
    return b # 200 y sale de la función
print(b) # 500
a() # Aquí se llama la función, sería 300
print(b) # 500
# Sería 500, 500, 300, 300 



#13
b = 500
print(b) # 500
def a():
    b = 300
    print(b)
    return b 
print(b) # 500
b=a() # 300
print(b) # 500
# Sería 500, 500, 300, 300



#14
def a():
    print(1) # 1
    b()
    print(2) # 2
def b():
    print(3) # 3
a() # No caché :(



#15
def a():
    print(1) # aquí se imprime 1
    x = b() # está vacío
    print(x) # no debería imprimir nada
    return 10 # devuelve 10 y cierra la función
def b():
    print(3) # imprime 3
    return 5 # devuelve 5 y cierra la función
y = a() # significa que y ahora vale 10
print(y) # imprime 10
# esto imprime 1, luego 3, luego 5 (porque x = 5, debido a que def b devuelve 5, por lo tanto ahora imprime esa x como 5), y luego 10
