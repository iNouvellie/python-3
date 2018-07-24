def PermitidoManejar (edad):
	if edad > 17:
		print ("Puedes tener un auto y manejarlo")
	elif edad > 14 & edad < 18:
		print ("Puedes tener un auto, pero manejarlo con la supervision de un adulto")
	else:
		print ("No puedes manejar el auto")

edad = int(input("Ingrese edad: "))

PermitidoManejar(edad)