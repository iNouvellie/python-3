dias_semana = {"lunes":9, "martes":10, "miercoles":11}

print (dias_semana)

#Para agregar los dias restantes
dias_semana["jueves"] = 12
print (dias_semana)

#Borro un elemento del diccionario
del dias_semana["lunes"]
print (dias_semana)

#Agrego 3 dias usando update
dias_semana.update({"viernes":13, "sabado":14, "domingo":15})
print (dias_semana)

#Actualizo 2 dias existentes, en caso de no tener sabado o domingo, se agregan
dias_semana.update({"sabado":15, "domingo":16})
print (dias_semana)