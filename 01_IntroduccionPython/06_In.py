vocales = "aeiou"

lista_vocales = list(vocales)

#Deberia devolver True
print ("a" in vocales)
print ("a" in lista_vocales)

#Deberia devolver False
print ("z" in vocales)
print ("z" in lista_vocales)

if "a" in vocales:
	print ("'a': Es una vocal")

if "z" not in vocales:
	print ("'z': No es una vocal")

if "a" in lista_vocales:
	print ("'a': Es esta en la lista de vocales")