#!/usr/bin/python
# coding: utf-8

def calcul_polonais(L):
    pile = []
    for e in L:
        if e.isdigit():
            pile.append(e)
        if est_Operateur(e):
            a,b = pile.pop(),pile.pop()
            c = operer(e,a,b)
            pile.append(c)
        print(pile)

def est_Operateur(x):
    if(x in ['*','+','-','/']):
        return True
    return False

def operer(e,x,y):
    if(e == '*'):
        return float(x)*float(y)
    if(e == '+'):
        return float(x)+float(y)
    if(e == '-'):
        return float(x)-float(y)
    if(e == '/'):
        return float(x)/float(y)

def main():
    calcul_polonais([8,7,2,5,'+','*','-'])

if __name__ == "__main__":
    main()
