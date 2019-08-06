# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 10:32:22 2019

@author: tiago.santos
"""
import string

#Pacote de funções recursivas básicas em Python

def fatorial(n):
    if n == 1:
        return 1
    else:
        return n*fatorial(n-1)


def progressaoAritmetica(n):
    if n == 1:
        return 1
    else:
        return n + (progressaoAritmetica(n-1))


def sequencialFibonacci(n):
    if n > 0 and n <= 2 :
        return 1;
    else:
        return sequencialFibonacci(n-1) + sequencialFibonacci(n-2)
    
    
def exponencial(a, b):
    if b <= 0:
        return 1
    else:
        return a * exponencial(a, b-1)
    

#def countWords(frase):
 #   words = frase.split(" ")
    