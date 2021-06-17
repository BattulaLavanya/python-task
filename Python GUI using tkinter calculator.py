from tkinter import *

main_window = Tk()

Display = Entry( main_window, width = 50, borderwidth = 30)
Display.grid(row = 0, column = 0, columnspan = 4)
global d
d=''
   
def Click(inp):
    global d
    if d == '=':
        Display.delete(0, 'end')
    d=''    
    Display.insert(50,inp)

def add():
    global x1
    global b
    x = Display.get()
    Display.delete(0,'end')
    x1 = int(x)
    b = '+'
def sub():
    global x1
    global b
    x = Display.get()
    Display.delete(0,'end')
    x1 = int(x)
    b = '-'
def mul():
    global x1
    global b
    x = Display.get()
    Display.delete(0,'end')
    x1 = int(x)
    b = '*'
def div():
    global x1
    global b
    x = Display.get()
    Display.delete(0,'end')
    x1 = int(x)
    b = '/'
def mod():
    global x1
    global b
    x = Display.get()
    Display.delete(0,'end')
    x1 = int(x)
    b = '%'
    
def equal():
    global d
    d='='
    a = Display.get()
    Display.delete(0,'end')
    if b == '+':
        a1 = int(a) + x1
        c = Display.insert(50, a1)
        
    elif b == '-':
        a1 = x1 - int(a)
        c = Display.insert(50, a1)
        
    elif b == '*':
        a1 = x1 * int(a)
        c = Display.insert(50, a1)

    elif b == '/':
        a1 = x1 / int(a)
        c = Display.insert(50, a1)
    elif b == '%':
        a1 = x1 % int(a)
        c = Display.insert(50, a1)
    

a1 = Button( main_window,text = "1", command = lambda: Click("1"), width = 10, borderwidth = 5).grid(row = 1, column = 0,columnspan = 1)
a2 = Button( main_window,text = "2",  command = lambda: Click("2"),width = 10, borderwidth = 5).grid(row = 1, column = 1,columnspan = 1)
a3 = Button( main_window,text = "3", command = lambda: Click("3"), width = 10, borderwidth = 5).grid(row = 1, column = 2,columnspan = 1)

a4 = Button( main_window,text = "4", command = lambda: Click("4"), width = 10, borderwidth = 5).grid(row = 2, column = 0,columnspan = 1)
a5 = Button( main_window,text = "5", command = lambda: Click("5"), width = 10, borderwidth = 5).grid(row = 2, column = 1,columnspan = 1)
a6 = Button( main_window,text = "6", command = lambda: Click("6"), width = 10, borderwidth = 5).grid(row = 2, column = 2,columnspan = 1)

a7 = Button( main_window,text = "7", command = lambda: Click("7"), width = 10, borderwidth = 5).grid(row = 3, column = 0,columnspan = 1)
a8 = Button( main_window,text = "8", command = lambda: Click("8"), width = 10, borderwidth = 5).grid(row = 3, column = 1,columnspan = 1)
a9 = Button( main_window,text = "9", command = lambda: Click("9"), width = 10, borderwidth = 5).grid(row = 3, column = 2,columnspan = 1)

a0 = Button( main_window,text = "0", command = lambda: Click("0"), width = 10, borderwidth = 5).grid(row = 2, column = 3,columnspan = 1)

x=0
sign1 = Button( main_window,text = "+", command = add, width = 10, borderwidth = 5).grid(row = 4, column = 0,columnspan = 1)
sign2 = Button( main_window,text = "-", command = sub, width = 10, borderwidth = 5).grid(row = 4, column = 1,columnspan = 1)
sign3 = Button( main_window,text = "*", command = mul, width = 10, borderwidth = 5).grid(row = 4, column = 2,columnspan = 1)
sign4 = Button( main_window,text = "/", command = div, width = 10, borderwidth = 5).grid(row = 4, column = 3,columnspan = 1)
sign5 = Button( main_window,text = "=", command = equal, width = 10, borderwidth = 5).grid(row = 1, column = 3,columnspan = 1)
sign5 = Button( main_window,text = "%", command = mod, width = 10, borderwidth = 5).grid(row = 3, column = 3,columnspan = 1)

main_window.mainloop()


##Python lambda function can be used in GUI programming
##    with Tkinter. It allows to create small, inline
##    functions for the command parameter. We have three buttons that share one callback.
##    The lambda function allows us to send specific data to the callback function.
