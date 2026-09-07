edad = int(input("ingrese su edad"))
if edad >=18:
	print ('puede votar')
else: 
	if edad >=17:
		print ('en un año o menos podra votar')
	else:
		print ('no puede votar')