"""
	Problema 3
	autor: jecueva11
"""
# frase dada
frase = ["No", "hay", "medicina", "que", "cure", "lo", "que", "no", "cura", "la", "felicidad"]
# utlizacion del lambda para la comparacoin de las palabras en su numero
resultado = filter(lambda x: len(x) == 2 or len(x)<=3, frase)
# presentacion del mensaje
print(list(resultado))