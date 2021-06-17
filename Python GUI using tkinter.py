## To creat sample main window and type window

from tkinter import *

main_window = Tk()    # creat Tk window


# To Creat Lable== used to display Text on out main window

Label(main_window, text= "What is your name?").grid(row = 0 , column = 0)

Label(main_window, text= "What is your age?").grid(row = 1 , column = 0)

#Enter Text

a = Entry(main_window, width= 50 , borderwidth = 5)
a.grid(row = 0, column = 1)

b = Entry(main_window, width= 50 , borderwidth = 5)
b.grid(row = 1, column = 1)

# To Call CLick

def on_click():
    print(f' My name is {a.get()} and my age is {b.get()}')
          
#Button

Button(main_window, text= "CLICK", command = on_click).grid(row = 2 , column = 1)


#display main window
main_window.mainloop()  
