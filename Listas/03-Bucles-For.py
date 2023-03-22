"""Los bucles (for) se utilizan para iterar sobre una secuencia dada, como listas o cadenas"""

#añade "!" al final de las palabras
palabras = ["hello", "world", "spam", "eggs"]
for signo in palabras:
  print(signo + "!")
  
"""El bucle "for" define una variable que toma el valor del elemento actual de la lista en cada iteracion. En el codigo anterior la variable "signo" representa el elemento correspondiente de la lista en cada iteracion del bucle."""

str = "testeando las vueltas"
count = 0

for x in str:
  if x == 't':
    count += 1

print(count)

"""El codigo anterior define una variable "count" itera sobre la cadena y calcula la cuenta de letras "T" en ella. Durante cada iteracion, la variable x representa la letra actual de la cadena."""

text = "some text"
for x in text:
  if x == 'e':
    break
  print(x)
  
"""Las sentencias "break" y "continue" tambien pueden ser usadas en los bucles "for" para detener el bucle o saltar a la siguiente iteracion"""


