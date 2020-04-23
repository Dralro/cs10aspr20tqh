#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 17:09:21 2020

@author: michaelhumphrey
"""

import tkinter
from tkinter import Label

top = tkinter.Tk()
top.geometry('200x400')
top.title("MTg card Finder")
w = Label(top, text="")
#w.grid(row=0, column=0, columnspan=9,)


def show_entry_fields():
    print("power: %s\nToughnesse: %s\nrarity%s\nType" % (power.get(), toughnes.get(), rarity.get(), Type.get()))
    power.delete(0, tkinter.END)
    toughnes.delete(0, tkinter.END)


def oneCallBack():
   w.config(text=w.cget("text")+"1")

def twoCallBack():
   w.config(text=w.cget("text")+"2")
def threeCallback():
   w.config(text=w.cget("text")+"3")
def fourCallback():
   w.config(text=w.cget("text")+"4")
def fiveCallback():
   w.config(text=w.cget("text")+"5")
def sixCallback():
   w.config(text=w.cget("text")+"6")

def clearCallback():
   w.config(text="")
def dotcallback():
   w.config(text=w.cget("text")+".")

Green = tkinter.Button(top, text ="green", command = oneCallBack, height=4, width=4)
Black = tkinter.Button(top, text ="black", command = twoCallBack, height=4, width=4)
Blue = tkinter.Button(top, text ="blue", command = threeCallback, height=4, width=4)
White = tkinter.Button(top, text ="white", command = fourCallback, height=4, width=4)
Red = tkinter.Button(top, text ="Red", command = fiveCallback, height=4, width=4)

#B8 = tkinter.Entry(top, text ="8", command = eightCallback, height=4, width=4)
tkinter.Label(top, text="power").place(y=20, x=2)#e1
tkinter.Label(top, text="toughness").place(y=60, x=2)#e2
#mabey have this text box be buttons instead
tkinter.Label(top, text="rarity").place(y=100, x=2)#e3
tkinter.Label(top, text="type").place(y=140, x=2)#e4

power = tkinter.Entry(top)
toughnes = tkinter.Entry(top)
rarity = tkinter.Entry(top)
Type = tkinter.Entry(top)

tkinter.Button(top, 
          text='Show', command= show_entry_fields).place(y=400, 
                                                       x=100,)
#           y         x
power.place(y=20, x=60)#power
toughnes.place(y=60, x=60)#toughnes
rarity.place(y=100, x= 60)#rarity
Type.place(y=140, x= 60)#type
Green.place(y=180, x=0)#green
Black.place(y=180, x=40)#black
Blue.place(y=180, x=80)#blue
White.place(y=180, x=120)#white
Red.place(y=180, x=160)#red


w.place(x=100, y=100)

top.mainloop()
