# -*- coding: utf-8 -*-
vlr_slr = int(input('Qual é o valor do salário? '))
pct_amt = int(input('Qual é o percentual do aumento? '))

def calcular_aumento(valor, aumento):
    return  valor + (valor / 100 * aumento)

total = calcular_aumento(vlr_slr, pct_amt)

print('O valor do novo salário é ' + str(total))