# -*- coding: utf-8 -*-
prc_mrc = int(input('Qual preço da mercadoria? '))
pcl_dsc = int(input('Qual é o percentual do desconto? '))

def calcular_desconto(preco, desconto):
    return  preco - (preco / 100 * desconto)

total = calcular_desconto(prc_mrc, pcl_dsc)

print('O total a pagar é ' + str(total))