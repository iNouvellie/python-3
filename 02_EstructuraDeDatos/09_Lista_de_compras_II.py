#Agregadas excepciones, reseteo de pantalla para un uso mas amigable al usuario

def agregar_articulo():
	print(chr(27) + "[2J")
	articulo = input("Nombre de articulo a agregar: ")
	#Capitalize hace un upper solo a la primera letra
	lista_articulos.append(articulo.capitalize())
	print ("Articulo agregado")


def remover_articulo():
	print(chr(27) + "[2J")
	#print ("Remover articulo\n")
	articulo = input ("Nombre del articulo a remover: ")
	articulo = str(articulo.capitalize())
	i = 0
	for item in lista_articulos:
		if articulo == lista_articulos[i]:
			#Ambas formas son correctas
			del lista_articulos[i]
			#lista_articulos.remove(articulo)
			print ("Articulo eliminado")
		else:
			print ("Articulo no existe")
		i += 1

def ver_articulos():	
	print(chr(27) + "[2J")
	print ("====LISTA==DE==COMPRAS==BY==NOUVELLIE====")
	i = 1
	for item in lista_articulos:
		print ("El %d articulo es: %s" % (i, item))
		i += 1
	print ("=========================================")

#Asi la inicializamos vacia (se puede usar []), ambas opciones son validas
lista_articulos = list()

print ("\n=========================================")
print ("====LISTA==DE==COMPRAS==BY==NOUVELLIE====")
print ("=========================================\n")

while True:
	print ("Estas son las operaciones que puedes realizar:\n")
	print ("1 - Agregar articulo")
	print ("2 - Remover articulo")
	print ("3 - Ver articulos")
	print ("4 - Salir\n")
	try:
		operacion = int(input("Ingrese la operacion deseada: "))
		print ("\n")
	except ValueError:
		print(chr(27) + "[2J")
		print ("\nPor favor introduce solo numeros\n")
		continue
	else:
		if operacion == 1:
			agregar_articulo()
		elif operacion == 2:
			remover_articulo()
		elif operacion == 3:
			ver_articulos()
		elif operacion == 4:
			break
		else:
			print(chr(27) + "[2J")
			print ("Ingrese un numero valido (1-2-3-4)")
		print ("\n")
print(chr(27) + "[2J")
print ("==========================")
print ("GRACIAS POR SU PREFERENCIA")
print ("==========================\n")