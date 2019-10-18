"""
	Problema 2
	autor: jecueva11
"""
# datos de las notas dadas
notas = [(5, 5, 10), (10, 2, 4), (10, 1, 9), (10, 2, 3)]
# proceso con lambda para la suma de las posiciones
suma = lambda x: x[0] + x[1] + x[2]
# imprecion del mensaje
print(list(map(suma, notas)))