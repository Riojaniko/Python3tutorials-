"""Una cosa que se puede hacer con los boleanos es utilizar declaraciones (if) para ejecutar un codigo en una deteeminada condicion, por ejemplo, si el booleanose ejecuta como True"""

#If debe estar indentado
x = 42
if x > 5:
    print("42 es mayor que 5.")
    
"""los dos puntos al final de la declaracion son importantes acuerdate de ponerlos si no no funcionara"""

if x > 30:
    print("Si!!! 42 es mayor que 30.")
 
"""Las declaraciones If pueden estar anidadas unas dentro de otras"""

num = 20

if num < x:
    print("20 es menor que 42.")
    if num <= x:
        print("20 es menor o igual que 42.")

                
x = 'a'

if x < 'c':
    x += 'b'
if x > 'z':
    x += 'c'    
print(x)

"""La declaracion (Else) puede usarse para ejecutar algunas declaraciones cuando la condicion de la declaracion (If) es False"""
y = 15
x = 30

if x <= y:
    print("Soy pequeño y que!!")
else:
    print("Soy el mayor")

"""Cada bloque de if solo puede tener una condicion else"""

"""Demasiadas declaraciones (if/else) hacen del codigo largo y tedioso de leer. La mejor manera de resolver esto es usando la declaracion (elif)"""

num = 3
if num == 1:
  print("One")
elif num == 2:
  print("Two")
elif num == 3: 
  print("Three")
else: 
  print("Something else")