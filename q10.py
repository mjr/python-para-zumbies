# -*- coding: utf-8 -*-
qtd_cig_fma_por_dia = input ('Quantos cigarros você fuma por dia? ')
qtd_anos_fmou = input ('Quantos anos você já fumou? ')

perda_dia = qtd_cig_fma_por_dia * 10
perda_mes = perda_dia * 30
perda_ano = perda_mes * 12
total_minutos = perda_ano * qtd_anos_fmou

def conversao_minutos_em_dias(minutos):
    return minutos / 60 / 24

total = conversao_minutos_em_dias(total_minutos)

print (str(total) + ' dias perdidos.')