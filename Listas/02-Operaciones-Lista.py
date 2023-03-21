"""Podemos reasignar el elemento de un indice determinado de una lista"""

nums = [10, 20, 30]
nums[1] = 42

print(nums)

"""Las listas tambien pueden añadirse del mismo modo que las cadenas"""

nums = [1,2,3,4]
print(nums + [5,6,7,8])

"""Tambien podemos multiplicar las listas al igual que se puede hacer con las cadenas"""

print(nums * 3)

"""Podemos comprobar si un elemento esta en una lista con el operador (in)"""

cosas = ["patata","lago","sonar","vivo"]

print("patata" in cosas)
print("cola" in cosas)

"""Tambien podemos usar el operador (in) para determinar si una cadena es o no una subcadena de otra cadena."""

x = "Hola mundo!!"
if "mundo" in x:
    print("Si")
    
"""Para comprobar si un elemento no esta en una lista podemos usar el operador (not)."""

Nums = [1,2,3,4]

print(not 5 in Nums)
#True si el elemento no esta en lista
print(not 4 in Nums)
#False si el elemento si esta en lista

