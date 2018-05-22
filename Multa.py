# -*- coding: utf-8 -*-
"""
Created on Tue May 22 16:13:12 2018

@author: Acer
"""

#Entrada (v em km/h e m como a multa)
v=float(input("Insira a velocidade registrada:"))
m=(v-80)*5

#Processamento
if v>80:
    print("A multa cobrada em R$ será de:", m)
    
