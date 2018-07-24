#Ingresar vocales como lista e imprimirlas en mayuscula

vocales = "aeiou"

#Cambiamos las vocales iniciales a mayuscula
vocales_mayus = vocales.upper()

#Luego hacemos que el str sea list
vocales_list = list(vocales_mayus)

#print (vocales_list)

print ("\nPrimera forma usando for\n")

for vocal in vocales_list:
	print (vocal)

print ("\nSegunda forma usando for\n")

for i, vocal in enumerate(vocales_mayus):
	print (vocal)

print ("\nTercera forma usando while\n")

#Obtenemos el largo del string para poder recorrerlo desde 0
contador = len(vocales_list)

n = 0
while n < contador:
	print (vocales_list[n])
	n += 1