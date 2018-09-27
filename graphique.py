#!/usr/bin/python

##################################
#
# Created by Louis Grandvaux
# Not finished yet
#
##################################

import tkinter as tk
import math

def main():
    window = tk.Tk()
    canvas = tk.Canvas(window, width=1000, height=600, background='white')
    axeY = canvas.create_line(20, 0, 20, 600, arrow='first')
    axeX = canvas.create_line(0, 300, 1000, 300, arrow='last')
    canvas.create_line(15, 100, 25, 100)
    canvas.create_line(15, 500, 25, 500)
    canvas.create_text(7, 100, text='1')
    canvas.create_text(7, 500, text='-1')
    for i in range(1,10):
        tickX = 20 + i * 100
        canvas.create_line(tickX, 305, tickX, 295)
        texte = str(i) + 'π'
        canvas.create_text(tickX, 315, text=texte)
    for i in range(20,1000):
        coordY = 200*math.cos((i-20)*math.pi/100)+300
        coordY2 = 200*math.cos((i-19)*math.pi/100)+300
        canvas.create_line(i, coordY, i, coordY2, fill='red')
    canvas.pack()

    window.mainloop()


if __name__ == '__main__':
    main()
