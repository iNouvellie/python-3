calificaciones = {"tito": 10, "naty":6, "amaro": 5}

#Al recorrer e imprimir con un for, solo muestra la llave
for calificacion in calificaciones:
	print (calificacion)

#De esta forma obtenemos el numero de la calificacion
for calificacion in calificaciones:
	print (calificaciones[calificacion])

#Imprime la key, pero usando su metodo
for key in calificaciones.keys():
	print (key)

#Imprime el value, pero usando su metodo
for value in calificaciones.values():
	print (value)

#De esta forma obtenemos una tupla donde se muestra key y value
for item in calificaciones.items():
	print (item)