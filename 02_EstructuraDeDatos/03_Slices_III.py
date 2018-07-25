#Reemplazar y borrar

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Con esto borramos 1 elemento de la lista indicando posicion
del numeros[0]
print (numeros)

#Borra los numeros del indice 0 al 3
numeros2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del numeros2[0:4]
print (numeros2)

#Luego tendremos del 4 al 10, queremos borrar el 7 y 8
del numeros2[3:5]
print (numeros2)

#Para reemplazar
numeros2[2:3] = [6, 7, 8]
print (numeros2)

#Reemplazar el 9 y 10 por 80 y 80
numeros2[5:7] = [80, 80]
print (numeros2)

numeros2[5:] = [9, 10]
print (numeros2)