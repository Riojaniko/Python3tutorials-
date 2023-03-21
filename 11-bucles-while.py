"""Los bucles permiten repetir un bloque de codigo varias veces"""

i = 1
while i <=20:
   print(i)
   i = i + 1

print("He acabado de contar!!!")

#arriba
"""Un bucle while que contiene una variable incremental que cuenta del uno al veinte y este finaliza imprimiendo un string al acabar de contar los 20."""

x = 0
while x<10:
  print(x)
  x += 1
  
#arriba
"""Las declaraciones deben de ir indentadas igual a las de las sentencias if/else si no este no funcionara"""

x = 1

while x < 41:
  if x%2 == 0:
    print(str(x) + " is even")
  else:
    print(str(x) + " is odd")

  x += 1
  
#arriba
"""tambien podemos usar while con if/else como ejemplo el codigo de arriba que separa los pares e impares"""

x = 8

while x > 3:
  print(x)
  
#arriba
"""Bucle infinito"""