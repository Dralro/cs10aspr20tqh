"""
Created on Wed Apr 22 17:09:21 2020

@author: Michael Humphrey, Tommy Holloman, David WhatsHisName
"""

import csv
from tkinter import *
import operator

sr = list(csv.DictReader(open("search.csv", 'r'), delimiter=","))

top = Tk()
top.geometry('400x300')
top.title("Magic: The Gathering Card Search")

color_l=[]

def Search():
    
    for i in sr:
        if w.get() == 1 and ("W" in i['mana_cost']) and (rarity in i['rarity']) and op_list[tkvar](i['cmc'], CMC) and Type in i['type']:
            print(i['name'])

    return 0

w = IntVar()
u = IntVar() 
b = IntVar()
r = IntVar() 
g = IntVar()

Checkbutton(top, text ="White", variable = w, fg = "Black").grid(row = 0, column = 1, sticky = W)
Checkbutton(top, text ="Blue", variable = u, fg = "Blue").grid(row = 0, column = 2,  sticky = W)
Checkbutton(top, text ="Black", variable = b, fg = "Black").grid(row = 0, column = 3, sticky = W)
Checkbutton(top, text ="Red", variable = r, fg = "Red").grid(row = 0, column = 4, sticky = W)
Checkbutton(top, text ="Green", variable = g, fg = "Green").grid(row = 0, column = 5, sticky = W)

Label(top, text="Rarity: ").place(y=30, x=2)

#Will add buttons for rarity probably

Label(top, text="Type: ").place(y=60, x=2)
Label(top, text="Converted Mana Cost: ").place(y=90, x=2)

tkvar = StringVar(top)

op_list = {
    
    '<': operator.lt,
    '=': operator.eq,
    '>': operator.gt,
    '<=': operator.le,
    '>=': operator.ge,
    '!=': operator.ne
    
}

tkvar.set('>')

popupMenu = OptionMenu(top, tkvar, *op_list)
popupMenu.grid(row = 1, column = 1)

# on change dropdown value
def change_dropdown(*args):
    print( tkvar.get() )

# link function to change dropdown
tkvar.trace('w', change_dropdown)

cd = IntVar(top, value = 0)

rarity = Entry(top)
Type = Entry(top)
CMC = Entry(top)
Button(top, text='Show', command = Search).place(y=200, x=100)

rarity.place(y = 30, x = 100) #rarity
Type.place(y = 60, x = 100) #type
CMC.place(y = 90, x = 200) #CMC
popupMenu.place(y = 80, x = 140) #operator for CMC

top.mainloop()