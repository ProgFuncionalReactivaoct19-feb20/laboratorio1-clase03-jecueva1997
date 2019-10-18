"""
	Problema 1
	autor: jecueva11
"""

archivo = open("promedios.txt", "r")
leer_fila = archivo.readlines()
archivo.close()

for lista in leer_fila:
	resultado = filter(lambda x: x >= 16.5, lista)
print(list(lista))
