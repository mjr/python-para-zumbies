# -*- coding: utf-8 -*-
qtd_km_prc = int(input('Quantos km foram percorridos? '))
qtd_dias_alg = int(input('Quantos dias o carro foi alugado? '))

def calcular_preco_a_pagar(km, dias):
    return km * 0.15 + dias * 60

preco_a_pagar = calcular_preco_a_pagar(qtd_km_prc, qtd_dias_alg)

print ('O preço a pagar pelo aluguel é de R$ ' + str(preco_a_pagar))