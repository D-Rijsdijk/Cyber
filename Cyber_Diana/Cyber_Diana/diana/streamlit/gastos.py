'''
import streamlit as st
import pandas as pd
'''
#Renda mensal
def validador(resposta):
    resposta = input().lower()
    while resposta not in ['s','n']:
        print('Resposta inválida! Responda apenas com (s/n)')
        resposta = input().lower()

salario = float(input('Salário ($): '))
renda_extra = validador('Você possui uma renda extra? (s/n)')

if renda_extra == 's':
    renda = input('Renda extra ($): ')

#Gastos
energia = input('Energia: ')
agua = input('Água: ')
internet = input('Internet: ')
alimentacao = input('Alimentação: ')
despesa_extra = validador('Você possui alguma despesa extra? (s/n)')
