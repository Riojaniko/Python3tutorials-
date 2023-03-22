"""Python hace que sea muy facil crear secuencias de numeros utilizando la funcion range() por defecto, comienza en cero, se incrementa en uno, y se detiene antes del numero especificado."""

numeros = range(21)
print(numeros)

"""Para que el rango salga como una lista, tenemos que comvertirlo explicitamente en una lista usando la funcion list()"""

numeros = list(range(21))
print(numeros)

"""Si el rango es llamado con un argumento, producira un objeto con valores desde 0 hasta ese argumento.Si se llama con dos argumentos producira valores desde el primero al segundo"""

numeros = list(range(21))
print(numeros)

numspars = list(range(5, 11))
print(numspars)

"""Tambien hay un tercer argumento llamado 'step' y este determina el intervalo de la secuencia producida"""

numeros = list(range(0,21,2))
print(numeros)

"""Podemos crear listas decrecientes usando valores negativos en el tercer argumento"""

numeros = list(range(21,0,-1))
print(numeros)

"""Podemos usar bucles 'for' con la funcion 'range' sin necesidad de convertirlos a listas. Se usa comunmente para repetir codigo un cierto numero de veces."""

for i in range(5):
    print("Me estoy repitiendo con la funcion range()")
    