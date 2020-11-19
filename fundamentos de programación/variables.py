PI = 3.14159
radio = 0
radio_is_float = False

# Mientras que la variable radio contenga valores alfanumericos
# radio_is_float permanecerá como False
while(not radio_is_float):
	try:
		radio = float(input('Por favor escribe el radio del circulo: '))
		radio_is_float = True
	except ValueError:
		print('\nEl valor introducido contiene cáracteres alfanuméricos. \n')


# Calcula los valores
perimetro = 2 * PI * radio
area = PI * (radio * radio)
volumen = (4/3)* PI * (radio * radio * radio)

# Muestra el resultado de los tres valores
print('perimetro =', perimetro)
print('area =', area)
print('volumen =', volumen)
