#Primero creamos una lista

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#print (numeros)

#Imprimir el numero en casilla 1
print (numeros[1])

#La importacia de usar slices, es que los devuelve como listas (imprime)
#Extraer numeros del espcio 0 al 5. Desde 0 hasta el anterior al puesto 6
print (numeros[0:6])

#Solo el primer elemento
print (numeros[0:1])

#Si usamos un index fuera de rango nos tira error
#print (numeros[11])

#En cambio usando slice siempre entregara hasta el ultimo
print (numeros[0:999999])

#Para obtener todo sin tener que recurrir a un numero auxiliar grande
print (numeros[0:])

#Para empezar del indice 2 al final
print (numeros[2:])

#Con inicio de partida no indicado, pero si final (en este caso el puesto 3)
print (numeros[:3])

#Para imprimir absolutamente todo
print (numeros[:])

#Se puede hacer el mismo tipo de llamados usando numeros negativos
#Para tomar el 5, 6 y 7 usaremos:
print (numeros[-6:-3])