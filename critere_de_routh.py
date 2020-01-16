#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np
import math

"""
Fonction appliquant le critère de route à un polynome
de la forme P = [a0, a1, ..., an].
"""
def critereDeRouth(P):
    #Polynôme P de la forme [b(n), b(n-1), ..., b(0)]
    #Degré du polynôme
    d = len(P)-1

    #Initialisation du tableau
    width = math.floor(d/2)+1
    tableau = np.zeros([d+1,width])

    #On remplit les deux premières lignes
    j=0
    for i in range(0,d+1,2):
        tableau[0][j] = P[i]
        j += 1
    j=0
    for i in range(1,d+1,2):
        tableau[1][j] = P[i]
        j+=1

    #On remplit les autres lignes
    for i in range(2,d+1):
        for j in range(width-1):
            tableau[i][j] = (-1/tableau[i-1][0])*(tableau[i-2][0]*tableau[i-1][j+1]-tableau[i-1][0]*tableau[i-2 ][j+1])

    #On vérifie le critère de Routh
    critere = True
    epsilon = 1
    if tableau[0][0] < 0:
        epsilon = -1
    for i in range(1,d+1):
        if tableau[i][0] != epsilon*abs(tableau[i][0]):
            critere = False

    return critere

#Exemple
P = [5, 6, 2.1, 7.8, -5, -0.24]
print(critereDeRouth(P))
