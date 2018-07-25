'''
Crear calculadora que haga suma, resta, multiplicacion y division.
Debe pedir 2 numeros.
Al finalizar debe preguntar si se requiere de otra operacion.
Debe contener excepciones para todos los casos de ingresos erroneos por parte de usuarios.
'''
def operacion(eleccion, primer_numero, segundo_numero):
	if eleccion == 1:
		print ("La suma de los numeros es %i" % (primer_numero + segundo_numero))

	elif eleccion == 2:
		print ("La resta de los numeros es %i" % (primer_numero - segundo_numero))

	elif eleccion == 3:
		print ("La multiplicacion de los numeros es %i" % (primer_numero * segundo_numero))

	elif eleccion == 4:
		print ("La division de los numeros es %i" % (primer_numero / segundo_numero))	
	
	else:
		print ("Operacion incorrecta")

print ("\n=========================================")
print ("BIENVENIDOS A LA CALCULADORA BY NOUVELLIE")
print ("=========================================\n")

continuar = "si"

while continuar == "si" or continuar == "SI" or continuar == "Si":
	print ("Estas son las operaciones disponibles: ")
	print ("1 - Suma")
	print ("2 - Resta")
	print ("3 - Multiplicacion")
	print ("4 - Division")
	
	try:
		eleccion = int(input ("\nIntroduzca el numero de la operacion a realizar: "))
		if eleccion < 1 or eleccion > 4:
			print ("\nPor favor introduce numeros del 1 al 4\n")
			continue
		primer_numero = int(input ("\nIngrese el primer numero: "))
		segundo_numero = int(input ("\nIngrese el segundo numero: "))
		print ("\n")

	except ValueError:
		print ("\nPor favor introduce solo numeros\n")
		continue

	else:
		operacion(eleccion, primer_numero, segundo_numero)
		continuar = input("\nDesea continuar: (si/no)   ")
		while continuar != "si" and continuar != "no" and continuar != "Si" and continuar != "No" and continuar != "SI" and continuar != "NO":
			continuar = input("\nDebe ingresar si o no: ")
		print ("\n")
		if continuar == "no" or continuar == "NO" or continuar == "No":
			print ("Gracias por su preferencia\n")
			break