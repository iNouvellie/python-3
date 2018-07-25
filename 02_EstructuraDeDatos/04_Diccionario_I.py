#Diccionario, funcionan sin orden de registro

lista_calificaciones = [9, 10, 6, 5]

diccionario_calificaciones = {"Tito": 9, "Naty": 10, "Ana": 6, "Roberto": 5}

print (diccionario_calificaciones)

#Revisar la nota de una llave en especifico
print (diccionario_calificaciones["Tito"])

#Agregar un dato al diccionario
diccionario_calificaciones["Cristian"] = "Nueve"
print (diccionario_calificaciones)

#Para construir un diccionario de otra manera menos convencional
print (dict([["Pepe", 7], ["Maria", 4]]))