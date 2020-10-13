entrada = input();
while(entrada != '0 0') :
	valor = entrada.split(' ')
	real = valor[1].replace(valor[0], '')
	if (real == '') : real = 0
	print (int(real))
	entrada = input();
