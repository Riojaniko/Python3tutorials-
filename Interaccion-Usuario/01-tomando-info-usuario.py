"""El comando input() pregunta al usuario y devuelve lo introducido como una cadena"""

text = input()
print(text)

"""Aunque el usuario introduzca un numero como entrada se procesa como una cadena(string)"""

num = input()
print("esto es un numero: " + num)

"""Para poder introducir un numero con el comando input necesitamos usar la funcion int()"""

age = int(input())
print(age)

"""De manera similar a la funcion int(), la funcion float() convierte una cadena en un float"""

ocho = float(input())
print(ocho)

"""Podemos usar la funcion str() para convertir un numero a una cadena"""

edad = input()
print("esta es mi edad: " + str(edad))

"""Podemos usar multiples input() para tomar varias entradas de usuario"""

Nombre = input()
Edad = input()
print("mi nombre es: "  + Nombre + " mi edad es: " + Edad)

