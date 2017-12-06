# This will serve as the interface to have the Url checker
from tkinter import *
import time as t
import URLCheck as u

result = "Please Some Options"

def JICTIF():
    # Definition of variables and window setup
    global urlE
    global repeat5C
    global repeatIndC
    global repeat5V
    global repeatIndV
    global repeat10V
    global roots
    roots = Tk()
    roots.title("Url Check")

    # Declaration and packing of LABELS
    introL = Label(roots, text="Program is meant to check links")
    resultL = Label(roots, text=result)
    introL.grid(columnspan=2)
    ##########################
    urlL = Label(roots, text="URL: ")
    urlL.grid(row=1, column=0)
    resultL.grid(columnspan=2)
    # Declaration and packing of ENTRIES
    urlE = Entry(roots)
    urlE.grid(row=1, column=1)
    # Declaration and packing of CHECK BUTTONS
    repeat5V = IntVar()
    repeatIndV = IntVar()
    repeat10V = IntVar()
    repeat5C = Checkbutton(roots, text="Repeat 5 Times", variable=repeat5V)
    repeat10C = Checkbutton(roots, text= "Repeat 10 Times", variable=repeat10V)
    repeatIndC = Checkbutton(roots, text="Repeat Indefinitely", variable=repeatIndV)
    repeat5C.grid(columnspan=2)
    repeat10C.grid(columnspan=2)
    repeatIndC.grid(columnspan=2)
    # Declaration and packing of BUTTONS
    checkB = Button(roots, text='Check', command=mainF)
    checkB.grid(columnspan=2)
    # Begin the mainloop
    roots.mainloop()


def mainF():
    # This function will return whether or not the url is valid
    global urlE
    global repeat5V
    global repeatIndV
    global repeat10V

    # Get the variables from the roots
    url = urlE.get()
    repeat5 = repeat5V.get()
    repeatInd = repeatIndV.get()
    repeat10 = repeat10V.get()

    # Print the responses on the terminal
    print(url)
    print('Rep 5 ', repeat5)
    print('Rep 10 ', repeatInd)

    # Run 5 times
    if repeat5:
        for i in range(0,5):
            u.urlCheck()
            result = 'test5'

    # Run 10 times
    if repeat10:
        for i in range(0,10):
            u.urlCheck()
            result = 'test10'

    # Run indefinitely
    if repeatInd:
        while True:
            u.urlCheck()
            result = 'testind'

JICTIF()
