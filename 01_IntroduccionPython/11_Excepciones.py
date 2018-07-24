#Pedir 2 numeros y entregar la suma con correcion de errores

#Engloba el conjunto que puede arrojar error
try:
	primer_numero = int(input ("Ingrese un numero: "))
	
	segundo_numero = int(input ("Ingrese otro numero: "))
	#Podria ser casteado al ingresar
	#primer_numero = int(input ("Ingrese un numero: "))

#Se especifica que debe mostrar al caer en un error en este caso ValueError
except ValueError:
	print ("\nEse no es un numero")

else:
	print ("\n")
	print ("La suma de esos 2 numeros es: %i" %  (int(primer_numero) + int(segundo_numero)))