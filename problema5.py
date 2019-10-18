"""
	Problema 5
	autor: jecueva11
"""

# metodo para sacar las black_edades
def edad(x):
	# datos de las black_edades
	black_edades = [10, 14, 30, 32, 40, 16]
	# condicional para sacar las black_edades
	if x in black_edades:
		return False
	else:
		return True


edades = [10, 12, 13, 14, 16, 18, 20, 30, 31, 32, 33, 40, 50]

resultado = filter(edad, edades )
# imprecion del resultado
print(list(resultado))

