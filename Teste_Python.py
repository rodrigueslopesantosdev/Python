# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 09:54:39 2019

@author: tiago.santos
"""
import Funcoes_Tiago
import string      
import pandas as pd
import numpy


frase = "Parece que um carro bateu em outro carro"

words = frase.split(" ")
total = len(words)
mapping = []

for pnt in words:
    print (pnt)
    
    
for pos in range (0, total):
    mapping.append(1)

    
di = dict(zip(words,mapping))    



print(di)