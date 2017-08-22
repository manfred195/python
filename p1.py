#! /usr/bin/python3
#adivina el día de la semana en que naciste.
def tabla_siglo(año):	
	#tabla de rangos de fechas para ajustar el número que se debe poner dependiendo del siglo.
	if año >= 400 and año <= 499 or año >= 1900 and año <= 1999 or año >= 1582 and año <= 1599:
		return 0
	elif año >= 300 and año <= 399:
		return 1
	elif año >= 200 and año <= 299 or año >= 900 and año <= 999 or año >= 1800 and año <= 1899:
		return 2
	elif año >= 100 and año <=199 or año >= 800 and año <= 899 or año >= 1500 and año <=1582:
		return 3
	elif año <=99 or año >= 700 and año <=799 or año >= 1400 and año <=1499 or año >= 1700 and año <= 1799:
		return 4
	elif año >= 600 and año <= 699 or año >= 1300 and año <= 1399:
		return 5
	elif año >= 500 and año <= 599 or año >= 1200 and año <=1299 or año >= 1600 and año <= 1699 or año >= 2000 and año <= 2099:
		return 6

def tabla_mes():
	#tabla para saber que número poner dependiendo del mes.
	tu_mes = input("en que mes naciste: ")
	meses_del_año = {'1': 0,'2': 3,'3': 3,'4': 6,'5': 1,'6': 4,'7': 6,'8': 2,'9': 5,'10': 0,'11': 3,'12': 5}
	return meses_del_año[tu_mes]

def dia_nacido(dia,t_mes,año,t_siglo):
	#algoritmo para calcular el día de la semana que naciste.
	return int((dia + t_mes + int(str(año)[2:]) + (int(str(año)[2:]) / 4) + t_siglo) % 7)

def inicio():
	#función principal del programa.
	dia = int(input("escriba el día que nacio: "))
	t_mes = tabla_mes()
	año = int(input("escriba el año en que nacio: "))
	t_siglo = tabla_siglo(año)
	resultado = dia_nacido(dia,t_mes,año,t_siglo)
	if resultado == 1:
		print("naciste el lunes")
	elif resultado == 2:
		print("naciste el martes")
	elif resultado == 3:
		print("naciste el mielcoles")
	elif resultado == 4:
		print("naciste el jueves")
	elif resultado == 5:
		print("naciste el viernes")
	elif resultado == 6:
		print("naciste el sabado")
	elif resultado == 7:
		print("naciste el domingo")
	
if __name__ == "__main__":
	inicio()
	
