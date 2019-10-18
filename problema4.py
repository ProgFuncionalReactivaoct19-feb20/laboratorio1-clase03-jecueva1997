"""
	Problema 4
	autor: jecueva11
"""

# notas cualitativas
notas = [(5, 5, 10, "Regular"), (10, 2, 4, "Bueno"), (10, 1, 9, "Muy Bueno"), (7, 2, 3, "Sobresaliente")]
# utilizacion del lambda para comparar las notas cualitativas
resultado = filter(lambda x: x[3] == "Bueno" or x[3] == "Regular", notas)
# imprecion del resultado
print(list(resultado))

"""
def not_cual(x):
	# datos
	cual = [ "Bueno", "Regular"]
	# condicional
	for i in cual:
		if x[3] in cual:
			return True
		else:
			return False


notas = [(5, 5, 10, "Regular"), (10, 2, 4, "Bueno"), (10, 1, 9, "Muy Bueno"), (7, 2, 3, "Sobresaliente")]

resultado = filter(not_cual, notas)
# imprecion del resultado
print(list(resultado))
"""