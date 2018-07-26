#Crear agenda telefonica, que guarde numero y nombre

#Creamos la agenda
agenda_telefonica = dict()

def agregar_contacto():
	#print ("Contacto agregado")
	nombre = input("Nombre del nuevo contacto: ")
	nombre = nombre.capitalize()
	numero = ("a")
	while numero == ("a") :
		try:
			numero = int(input("Numero del nuevo contacto: "))
		except ValueError:
			print(chr(27) + "[2J")
			print ("\nTelefono debe contener solo numeros\n")
			continue
		else:
			agenda_telefonica[nombre] = numero

def remover_contacto():
	print ("Contacto removido")

def actualizar_contacto():
	print ("Contacto actualizado")

def ver_contacto():
	print(chr(27) + "[2J")
	#print ("Ver contacto")
	contacto = input("Nombre del nuevo contacto a buscar: ")
	contacto = contacto.capitalize()
	for item in agenda_telefonica.items():
		if contacto == item[0]:
			print ("\nEl numero de %s es %d" % (item[0], item[1]))
			auxiliar = 1
	if auxiliar != 1:
		print ("Contacto no existe")

def ver_todos_contactos():
	print(chr(27) + "[2J")
	print ("\n=========================================")
	print ("====AGENDA==TELEFONICA==BY==NOUVELLIE====")
	print ("=========================================\n")
	i = 1
	for item in agenda_telefonica.items():
		print ("%d. El numero de %s es %d." % (i, item[0], item[1]))
		i += 1

print ("\n=========================================")
print ("====AGENDA==TELEFONICA==BY==NOUVELLIE====")
print ("=========================================\n")

while True:
	print ("Estas son las operaciones que puedes realizar:\n")
	print ("1 - Agregar contacto")
	print ("2 - Remover contacto")
	print ("3 - Actualizar contacto")
	print ("4 - Ver contacto")
	print ("5 - Ver todos los contactos")
	print ("6 - Salir\n")
	try:
		operacion = int(input("Ingrese la operacion deseada: "))
		print ("\n")
	except ValueError:
		print(chr(27) + "[2J")
		print ("\nPor favor introduce solo numeros\n")
		continue
	else:
		if operacion == 1:
			agregar_contacto()
		elif operacion == 2:
			remover_contacto()
		elif operacion == 3:
			actualizar_contacto()
		elif operacion == 4:
			ver_contacto()
		elif operacion == 5:
			ver_todos_contactos()
			
		elif operacion == 6:
			break
		else:
			print(chr(27) + "[2J")
			print ("Ingrese un numero valido (1-2-3-4-5)")
		print ("\n")

print(chr(27) + "[2J")
print ("==========================")
print ("GRACIAS POR SU PREFERENCIA")
print ("==========================\n")