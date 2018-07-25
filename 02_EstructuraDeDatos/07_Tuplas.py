#A diferencia de listas, no pueden modificarse

#Solo se refiere a items separados por coma, pero usaremos parentesis aca
tupla_1 = (1, 2, 3, 4)
print (tupla_1)

#Ahora corroboramos que se puede sin parentesis
tupla_2 = 1, 2, 3, 4
print (tupla_2)

#Hacer una tupla de 1 solo item
tupla_3 = (1,)
print (tupla_3)

tupla_4 = 1,
print (tupla_4)

#Para acceder a elementos se hace de la misma forma que en listas
print (tupla_1[2])

#No podemos modificar items no mutables, pero si mutables, pero hasta dejar al menos 1
tupla_5 = (1, "tito", [4, 5, 6])
print (tupla_5)
tupla_5[2][0] = 99
print (tupla_5)