"""Los operadores 'in-place' permiten escribir codigo como (x = x + 3) de forma mas concisa, como (x +=2)"""

a = 2

#suma
a += 1
print(a)
#resta
a -= 1
print(a)
#multiplicacion
a *= 2
print(a)
#division
a /= 7
print(a)
#modulo
a %= 1
print(a)
#exponenciacion
a **= 9
print(a)
#division entera
a //= 6
print(a)

"""Tambien podemos usar los operadores In-place para concatenar cadenas"""

h = "hola "

h += "python"
print(h)

x = "a"

x *= 3
print(x)
