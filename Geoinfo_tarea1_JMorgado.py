# -*- coding: utf-8 -*-
"""
Created on Sun May 30 00:14:44 2021

@author: julio
"""

"""
Comprobar si una frase es palíndromo

Por medio de una función...

Ejemplos de palíndromos:
    
    Oso
    Anita lava la tina

"""

"""
Función para reconocer un palíndromo

"""

def es_palindromo(frase):
    frase= frase.lower()
    frase= frase.replace(' ', '')
    longitud = len(frase)
    if longitud % 2==0:
        izquierda = frase[:longitud // 2]
        derecha = frase[longitud // 2:]
    else: 
        izquierda = frase[:longitud // 2]
        derecha = frase[longitud // 2 + 1: ]
    
    return izquierda == derecha [::-1]

print(es_palindromo("1001"))


print(es_palindromo("oso"))

print(es_palindromo("anita lava la tina"))




"""
Crear un algoritmo que compare las edades de dos usuarios
e imprima al usuario de mayor edad
"""

a, b= 'Dafne', 34
c, d= 'Julio', 36

if (b>=d):
    print(a, b)
elif (d>=b):
    print(c,d)







