# coding: utf-8

import math

"""
Nombre binaire sous la forme d'un talbeau vers un entier
"""
def binaire_vers_decimal(nb_binaire):
    nb_decimal = 0
    nb_binaire = nb_binaire[::-1]
    for i,valeur in enumerate(nb_binaire):
        nb_decimal += valeur*(2**i)
    return nb_decimal

"""
Nombre entier vers un nombre binaire sous forme d'un tableau
"""
def decimal_vers_binaire(nb_decimal):
    nb_binaire = []
    while(nb_decimal != 0):
        nb_binaire.append(nb_decimal % 2);
        nb_decimal = math.floor(nb_decimal / 2)
    return nb_binaire[::-1]

print(binaire_vers_decimal([0]))
print(binaire_vers_decimal([1]))
print(binaire_vers_decimal([1,0]))
print(binaire_vers_decimal([1,1]))
print(binaire_vers_decimal([1,0,0]))
print(binaire_vers_decimal([1,1,1,1]))
print(decimal_vers_binaire(6))
print(decimal_vers_binaire(255))
