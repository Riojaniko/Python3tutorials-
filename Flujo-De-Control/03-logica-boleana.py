"""El operador (and) es True si ambas condiciones se evaluan como True"""

print(1 == 1 and 2 == 2)
print(1 == 1 and 2 == 3)
print(1 != 1 and 2 == 2)
print(2 > 1 and 3 > 2)

"""Ejemplo condicion if/else"""
if (1 == 1) and (2 + 2 > 3):

  print("true")

else:

  print("false")
  
"""El operador (or) es True si alguna o ambas de sus condiciones son True, y False si ambas condiciones son False"""

print(1 == 1 or 2 == 2)

print(1 == 1 or 2 == 3)

print(1 != 1 or 2 == 2)

print(2 < 1 or 3 > 6)

"""Tambien se pueden comparar variables para formar condiciones"""

edad = 24
limite = 18
altura = 191

if edad > limite and altura > 180:
  print("Yes")
  
"""El operador (not) toma un argumento y lo invierte"""

# not True si False
# not False si True

print(not 1 == 1)
print(not 1 > 7)

"""podemos encadenar varias declaraciones condicionales en una declaracion (if) usando los operadores boleanos"""

estado = "US"
edad = 42

if(estado == "US" or estado == "GB") and (edad > 0 and edad < 100): 
  print("Cool")
  
"""El orden de las operaciones en python es igual que las operaciones normales: primero los parentesis, luego la exponeciacion, luego la  multiplicacion/divion y luego la suma/resta"""

