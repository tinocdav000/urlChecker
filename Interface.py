# This will serve as the interface to have the Url checker
from tkinter import *
import time as t
import URLCheck as u


def JICTIF():
    # Definition of variables and window setup
    global urlE
    global repeat5C
    global repeatIndC
    global roots
    roots = Tk()
    roots.title("Url Check")

    # Labels
    introL = Label(roots, text="Program is meant to check links")
    resultL = Label(roots)
    introL.grid(columnspan=2)
    ##########################

    # Declaration and packing of LABELS
    urlL = Label(roots, text="URL: ")
    urlL.grid(row=1, column=0)

    # Declaration and packing of ENTRIES
    urlE = Entry(roots)
    urlE.grid(row=1, column=1)

    # Declaration and packing of CHECK BUTTONS
    repeat5V = IntVar()
    repeatIndV = IntVar()
    repeat5C = Checkbutton(roots, text="Repeat 5 Times", variable=repeat5V)
    repeatIndC = Checkbutton(roots, text="Repeat Indefinitely", variable=repeatIndV)
    repeat5C.grid(columnspan=2)
    repeatIndC.grid(columnspan=2)

    # Declaration and packing of BUTTONS
    checkB = Button(roots, text='Check', command=mainF)
    stopB = Button(roots, text='Reset', command=resetF)
    checkB.grid(row=4, column=0, sticky=E)
    stopB.grid(row=4, column=1)


    roots.mainloop()


def mainF():
    # This function will return whether or not the url is valid
    global urlE
    global repeat5C
    global repeatIndC



def resetF():
    # This function will stop whatever process may be happening above
    pass

JICTIF()