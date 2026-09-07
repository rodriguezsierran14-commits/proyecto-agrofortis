estado civil= input('ingrese estado civil')
edad = int(input('ingrese edad'))
buena_persona= input ('es buena persona? (s,n):')
linda= input ('es linda? (s,n):')
if esatdo_civil=='c':
	print ('no me caso! me comprometo')
elif edad <=30 and linda == 's' or buena_persona == 's':
	print('si me caso')
else:
	 print ('solo' me comprometo)