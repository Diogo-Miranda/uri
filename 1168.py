def calculaLeds(num) :
	switcher = {
		1 : 2,
		2 : 5,
		3 : 5,
		4 : 4,
		5 : 5,
		6 : 6,
		7 : 3,
		8 : 7,
		9 : 6,
		0 : 6,	
	}
	return switcher.get(num);	

numEntrada = input()

for i in range (int(numEntrada)) :
	led = input()
	qntLeds = 0
	for j in range (len(led)) :
		qntLeds += calculaLeds(int(led[j]))
	print ('%i leds' % (qntLeds)) 	
