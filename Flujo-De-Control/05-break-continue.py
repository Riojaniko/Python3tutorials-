"""Para acabar un bucle while prematuramente podemos usar la declaracion (break)"""

i = 0
while True:
  print(i)
  i = i + 1
  if i >= 5:
    print("DETENIDO!!!")
    break

print("Finalizado!")

"""Otra declaracion que se puede usar dentro de los bucles es (continue). A diferencia de (break) (continue) salta de nuevo a la parte superior del bloque en lugar de detenerlo."""

i = 0
while i<11:
  i += 1
  if i==3:
    print("Pasamos a 3")
    continue
  print(i)
  


