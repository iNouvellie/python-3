vocales = "aeiou"
lista_vocales = list(vocales)

print (vocales)

print (lista_vocales)

variable_basura = "variable basura"

print (variable_basura)

del variable_basura

#No deberia dejar imprimir porque se borro
#print (variable_basura)

del lista_vocales[0]

print (lista_vocales)

del lista_vocales[-1]

#No se puede modificar una cadena, hay que hacerla lista y luego devolverla a cadena
#del vocales[0]

print (lista_vocales)

del vocales

del lista_vocales

#Todo anulado, borrado.