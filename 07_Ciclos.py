#Ciclos while, repiten bloque de codigo mientras la condicion sea cierta
#Ciclo for, recorren elementos en una coleccion

frutas = 10

while frutas > 0:
	print ("Estoy comiendo una fruta " + str(frutas))
	#frutas = frutas - 1
	frutas -= 1
	if frutas == 0:
		print ("\n")
		print ("Me quede sin frutas")

#--- o ---

lista_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in lista_nums:
	#Palabras reservadas continuo y break
	#Break rompe ciclo si se llega a dicha condicion
	if numero > 5:
		break
	print (numero)

print ("\n")

for numero in lista_nums:
	#Palabras reservadas continuo y break
	#Continuo salta la itereacion si cumple dicha condicion
	if numero == 5:
		continue
	print (numero)