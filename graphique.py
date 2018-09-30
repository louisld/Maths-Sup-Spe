#!/usr/bin/python

##################################
#
# Created by Louis Grandvaux
# La bibliothèque TKinter est requise
#
##################################

import tkinter as tk
import math
import time
import threading

#TODO: Pouvoir régler l'angle de départ

"""
Fonction qui tourne dans un thread séparé
Met à jour le canvas toutes les 0.1s
"""
def updateCanvas():
    th0 = -math.pi/4 #Angle de départ
    fil = canvas.create_line(1250, 350, math.sin(th0)*200+1250,math.cos(th0)*200+350 , fill='brown')
    masse = canvas.create_oval(math.sin(th0)*200+1240, math.cos(th0)*200+340, math.sin(th0)*200+1460, math.cos(th0)*200+360, fill="black")
    pos = canvas.create_oval(0, 0, 0, 0)
    #Initialisation des coordonnées
    coordY = 0
    coordX = -1
    coordY1 = 0 #Y à t-1
    coordX1 = 0 #X à t-1
    th1 = 0 #theta-1
    devth = 0 #derivé de theta
    devth1 = 0 #derivé à t-1 de theta
    for i in range(1,300): # Correspond à la taille du graphique : 1300px en abcisse
        time.sleep(0.1)
        th = th0*math.sin(math.sqrt(9.81/2)*i/10+math.pi/2)
        canvas.coords(fil,1250, 350, math.sin(th)*200+1250,math.cos(th)*200+350) #Màj du fil
        canvas.coords(masse,math.sin(th)*200+1240, math.cos(th)*200+340, math.sin(th)*200+1260, math.cos(th)*200+360) #Màj de la masse
        if coordX != -1: #Si ce n'est pas le premier tout de boucle
            #On met à jour toutes les coordonées
            coordY1 = coordY
            coordY = th/(math.pi/4)*200+300
            coordX1 = coordX
            coordX = (i*100/30)+20
            devth1 = devth
            devth = th0*math.sqrt(9.81/2)/10*math.cos(math.sqrt(9.81/2)*i/10+math.pi/2)
            #Puis on met à jour les différents éléments graphiques
            canvas.create_line(coordX1, coordY1, coordX, coordY, fill='blue')
            canvas.create_line(th1*100+1250, devth1*100+150, th*100+1250, devth1*100+150, fill="red")
            canvas.coords(pos, th1*100+1245, devth1*100+145, th*100+1255, devth1*100+155)
            th1 = th
        else: #Initialisation au premier tour de boucle
            coordX=20
            th1 =th
            coordY= th/(math.pi/4)*200+300

"""
Fonction principale
Dessin des axes
"""
def main():
    window = tk.Tk() #Fenêtre TKinter
    global canvas #Canvas poru dessiner les formes
    canvas = tk.Canvas(window, width=1500, height=600, background='white')
    #Création des axes
    axeY = canvas.create_line(20, 0, 20, 600, arrow='first')
    axeX = canvas.create_line(0, 300, 1000, 300, arrow='last')
    phaseX = canvas.create_line(1150, 150, 1350, 150, arrow="last")
    phaseY = canvas.create_line(1250, 50, 1250, 250, arrow='first')
    #Ordonnées
    canvas.create_line(15, 100, 25, 100)
    canvas.create_line(15, 500, 25, 500)
    canvas.create_text(15, 100, text='pi/4')
    canvas.create_text(15, 500, text='-pi/4')
    for i in range(1,34): # Abcisses
        canvas.create_text(7, 500, text='-1')
        tickX = 20 + i * 28.3
        canvas.create_line(tickX, 305, tickX, 295)
        texte = str(i)
        canvas.create_text(tickX, 315, text=texte)
    #for i in range(20,1000):
    #    coordY = 200*math.cos((i-20)*math.pi/100)+300
    #    coordY2 = 200*math.cos((i-19)*math.pi/100)+300
    #    canvas.create_line(i, coordY, i, coordY2, fill='red')
    canvas.create_oval(1240, 340, 1260, 360, fill='grey')
    canvas.pack()
    t = threading.Thread(target=updateCanvas) # Lancement du Thread de màj du canvas
    t.start()
    window.mainloop()

if __name__ == '__main__':
    main()
