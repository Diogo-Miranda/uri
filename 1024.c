#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#define TAM_WORD 1000

char deslocar3dir(char c) {
	return ( (char) (c + 3) );
}

void criptOne(char *in) 
{
	char out[TAM_WORD] = "";
	
	int i;
	for(i = 0; i < strlen(in); i++) {
		if( (in[i] >= 'A') && (in[i] <= 'z'))
			out[i] = deslocar3dir(in[i]);
		else 
			out[i] = in[i];
	}
         
	strcpy(in, out);
}

void criptTwo(char *in) 
{
	char out[TAM_WORD] = "";

	int i;
	for(i = 0; i < strlen(in); i++) {
		out[i] = in[strlen(in) - 1 - i];
	}
	
	strcpy(in, out);
}

char deslocar1esq(char c) {
	return ( (char) (c - 1) );
}

void criptThree(char *in)
{
	char out[TAM_WORD] = "";

	int tam = (strlen(in) - 1); 
	
	int corte = 0;
	if( (tam % 2) == 0) corte = (tam / 2);
		else corte = (tam / 2) + 1;
	
	int i;
	for(i = 0; i < corte; i++) {
		out[i] = in[i];
	}
	
	for(i = corte; i < strlen(in); i++) {
		out[i] = deslocar1esq(in[i]);
	}

	strcpy(in, out);
}

int main(void) 
{
	int qntEntrada;
	scanf("%i", &qntEntrada);		
		
	char entrada[qntEntrada][TAM_WORD];
	
	int numEntrada;
	for(numEntrada = 0; numEntrada < qntEntrada; numEntrada++) { 
		scanf(" %[^\n]s", entrada[numEntrada]);

	}
	
	int i;
	for(i = 0; i < qntEntrada; i++) {
		criptOne(entrada[i]);
		criptTwo(entrada[i]);
		criptThree(entrada[i]);
	
		printf("%s\n", entrada[i]);
	}	

	return 0;
}
