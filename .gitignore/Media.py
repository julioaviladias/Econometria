# -*- coding: utf-8 -*-
"""
Created on Sat May 19 10:34:22 2018

@author: Acer
"""

#Entrada
soma=0
i=0
x=[1, 7 ,15, 31]

#Processamento
while i<len(x):
    soma=soma+x[i]
    i=i+1
    media=soma/len(x)

#Saída
print("A media dos números é igual a:", media)
    
    