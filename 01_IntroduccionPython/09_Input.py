#El imput siempre lo guarda como str

dia_de_semana = input ("Que dia de la semana es hoy: ")

num_del_mes = input ("Que dia del mes es hoy: ")

print ("\n")
print (dia_de_semana)
print ("\n")
print (num_del_mes) #No lo muestra como str, pero segun el curso seria str y no int
print ("\n")

#Castear a int, se puede hacer incluso al solicitarlo

num_del_mes = input ("Que dia del mes es hoy: ")

print (int(num_del_mes))
print ("\n")

dos = int(num_del_mes) + 1
print (dos)