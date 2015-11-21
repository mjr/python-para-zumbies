# -*- coding: utf-8 -*-
qtd_dias = int(input('Dias: '))
qtd_horas = int(input('Horas: '))
qtd_minutos = int(input('Minutos: '))
qtd_segundos = int(input('Segundos: '))

def converter_dias_horas_minutos_segundos_em_segundos(dias, horas, minutos, segundos):
    return dias * 86400 + horas * 3600 + minutos * 60 + segundos

total_sgd = converter_dias_horas_minutos_segundos_em_segundos(qtd_dias, qtd_horas, qtd_minutos, qtd_segundos)

print('Total de segundos: ' + str(total_sgd))