texto = "abcdefg"

#De esta forma transformamos un texto a lista 

lista_texto = list(texto)

print (lista_texto)

#Revisemos indices

#Deberia imprimir la primera letra
print (lista_texto[0])

#Deberia imprimir la ultima letra
print (lista_texto[-1])
print (lista_texto[6])

#Deberia indicarme donde esta la "a" (seria 0)
print (texto.index("a"))
print (lista_texto.index("a"))

#Donde esta bc (deberia indicar el primer item encontrado, seria 1)
print (texto.index("bc"))
print (lista_texto.index("b"))

#Deberia tirar error ya que no esta en la lista (puede ser cualquier elemento que no este en la lista inicial original)
print (texto.index("h"))