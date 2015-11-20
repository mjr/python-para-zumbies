# -*- coding: utf-8 -*-
dst_a_pcr = input('Qual distância a percorrer(em km)? ')
vlc_mda_esp = input('Qual a velocidade média esperada para a viagem(em km/h)? ')

def tempo(distancia, velocidade):
    return distancia / velocidade

tempo_da_viagem = tempo(dst_a_pcr, vlc_mda_esp)

print('O tempo da viagem será aproximadamente ' + str(tempo_da_viagem) + ' horas')