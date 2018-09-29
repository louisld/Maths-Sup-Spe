#!/usr/bin/python

##################################
#
# Created by Louis Grandvaux
# Not finished yet
#
##################################

import tkinter as tk
import math
import time
import threading

def updatePendule():
    th0 = math.pi/4
    fil = canvas.create_line(1250, 300, math.sin(th0)*200+1250,math.cos(th0)*200+300 , fill='brown')
    masse = canvas.create_oval(math.sin(th0)*200+1240, math.cos(th0)*200+290, math.sin(th0)*200+1460, math.cos(th0)*200+310, fill="black")
    coordY = 0
    coordX = 0
    coordY1 = 0
    coordX1 = 0
    for i in range(1,200):
        time.sleep(0.1)
        th = th0*math.sin(math.sqrt(9.81/2)*i/10+math.pi/2)
        th1 = th0*math.sin(math.sqrt(9.81/2)*(i+2)/10+math.pi/2)
        canvas.coords(fil,1250, 300, math.sin(th)*200+1250,math.cos(th)*200+300)
        canvas.coords(masse,math.sin(th)*200+1240, math.cos(th)*200+290, math.sin(th)*200+1260, math.cos(th)*200+310)
        coordY = th/(math.pi/4)*200+300
        canvas.create_line((i)*100/30+20, coordY, (i+1)*100/30+20, coordY2, fill='blue')
def main():
    window = tk.Tk()
    global canvas
    canvas = tk.Canvas(window, width=1500, height=600, background='white')
    axeY = canvas.create_line(20, 0, 20, 600, arrow='first')
    axeX = canvas.create_line(0, 300, 1000, 300, arrow='last')
    canvas.create_line(15, 100, 25, 100)
    canvas.create_line(15, 500, 25, 500)
    canvas.create_text(7, 100, text='1')
    canvas.create_text(7, 500, text='-1')
    for i in range(1,10):
        canvas.create_text(7, 500, text='-1')
        tickX = 20 + i * 100
        canvas.create_line(tickX, 305, tickX, 295)
        texte = str(i) + 'π'
        canvas.create_text(tickX, 315, text=texte)
    for i in range(20,1000):
        coordY = 200*math.cos((i-20)*math.pi/100)+300
        coordY2 = 200*math.cos((i-19)*math.pi/100)+300
        canvas.create_line(i, coordY, i, coordY2, fill='red')
    canvas.create_oval(1240, 290, 1260, 310, fill='grey')
    canvas.pack()
    t = threading.Thread(target=updatePendule)
    t.start()
    window.mainloop()

if __name__ == '__main__':
    main()
