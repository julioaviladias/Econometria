# -*- coding: utf-8 -*-
"""
Created on Tue May 22 16:37:38 2018

@author: Acer
"""

#Entrada
import math
a=float(input("Digite o coeficiente a:"))
b=float(input("Digite o coeficiente b:"))
c=float(input("Digite o coeficiente c:"))

#Processamento
x=(b**2)-(4*a*c)
x=math.sqrt(x)
x1=(-b+x)/2*a
x2=(-b-x)/2*a

#Saída
print("A primeira raiz será:", x1)
print("A segunda raiz será:", x2)
