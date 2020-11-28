def validar_fecha(dia, mes, anio):
	return (1<= dia <= 31) and (1 <= mes <= 12) and (1 <= anio <= 9999)

def validar_bisiesto(anio):
	es_bisiesto = (anio%4 == 0) and (anio%100 != 0) or (anio%400 == 0)
	return ('no es bisiesto', 'es bisiesto')[es_bisiesto]

def obtener_estacion(dia, mes):
	estacion = (mes * 10) + dia
	if(50 <= estacion < 80):
		return 'Primavera'
	elif(80 <= estacion < 112):
		return 'Verano'
	elif(112 <= estacion < 141):
		return 'Otoño'
	elif(141 <= estacion or estacion < 50):
		return 'Invierno'

def principal():
	verificador_entrada = False
	anio = 0
	mes = 0
	dia = 0
	bisiesto = ''
	estacion = ''

	# Entrada de datos
	while(not verificador_entrada):
		try:
			anio = int(input('Ingrese por favor un año entre 0001 y 9999: '))
			mes = int(input('Ingrese un mes del año del 1 al 12: '))
			dia = int(input('Ingrese un día del mes: '))
			# Validacon de fechas
			if(validar_fecha(dia, mes, anio)):
				verificador_entrada = True
			else:
				print('\n** Error: Fecha invalida, intente de nuevo por favor\n')
		except ValueError:
			print('\nEl valor introducido contiene cáracteres no validos.\n')

	# Verificacion de año bisiesto
	bisiesto = validar_bisiesto(anio)
	estacion = obtener_estacion(dia, mes)

	print("La fecha que ingresaste es valida, la estación es %s y el año es %s."%(estacion, bisiesto))

principal()
