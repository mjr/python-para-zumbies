# -*- coding: utf-8 -*-
num_um = int(input('Primeiro valor: '))
num_dois = int(input('Segundo valor: '))

def somar_dois_numeros(numero_um, numero_dois):
    return numero_um + numero_dois

result = somar_dois_numeros(num_um, num_dois)

print ('A soma é igual a: ' + str(result))