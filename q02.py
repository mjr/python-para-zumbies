# -*- coding: utf-8 -*-
qtd_metros = int(input('Metros: '))

def converter_metros_para_milimetros(metros):
    return metros * 1000

milimetros = converter_metros_para_milimetros(qtd_metros)

print('Milímetros: ' + str(milimetros))