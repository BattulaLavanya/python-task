# To create a digital watch

from tkinter import *
from time import time, sleep
from datetime import datetime
import asyncio
import sys
from tkinter import simpledialog
from tkinter import messagebox
from playsound import playsound



main_window = Tk()

Display = Entry( main_window, width = 30, borderwidth = 10)
Display. grid(row = 10, column = 1, columnspan = 1)
sys.setrecursionlimit(15000)
global e1
e1 = 0
global e2
e2 = 0
global e0
e0 = 0
global z
z=0
global j
j=0
global k
k=0

def clock_24():
    global e0
    global e1
    global e2
    global z
    global j
    global k
    if z==0:
        z+=1
        e0 =1
        e1 =0
        e2=0
    if e1 == 1 or e2 == 1:
        z=0
        return
    #print(e0,e1,e2)
    
    
    now = datetime.now()
    Display.delete(0,'end')
    currentTime = now.strftime("%H:%M:%S")    
    Display.after(1, clock_24)
    Display.insert(30,currentTime)
     
        
def clock_12():
    global e0
    global e1
    global e2

    global z
    global j
    global k
    if j==0:
        j+=1
        e0 =0
        e1 =1
        e2=0

    if e0 == 1 or e2 == 1:
        j=0
        return
    


    now = datetime.now()
    Display.delete(0,'end')
    currentTime = now.strftime("%I:%M:%S:%p")    
    Display.after(1, clock_12)
    Display.insert(30,currentTime)


def stop_watch():
    global e0
    global e1
    global e2
    global z
    global j
    global k
    if k==0:
        k+=1
        e0 =0
        e1 =0
        e2=1
    if e0 == 1 or e1 == 1:
        k=0
        return
    print(e0,e1,e2)



    global i
    global h
    global m

    Display.delete(0,'end')
    x = 60
    if i<x:
        currentTime = i
        i+=1
    else:
        currentTime = 0
        i=0
        i=i+1
        m=m+1
    if m==60:
        h=h+1
        m=0
        i=0
    if h==24:
        m=0
        i=0
        h=0
    
    Display.insert(30,str(h)+":"+ str(m) +":"+ str(i))
    Display.after(1,stop_watch)
    
def alarm():
    h2 = simpledialog.askstring(title="Alarm", prompt = main_window)
    m2 = simpledialog.askstring(title="Alarm", prompt = main_window)
    now = datetime.now()
    Display.delete(0,'end')
    
    #currentTime = now.strftime("%H:%M:%S")
    
    a =int(h2)-now.hour
    b = int(m2)-now.minute 
    cutime=(a*60*60*1000)+(b*1000*60)

    
    print(a, cutime)
    Display.after(cutime, alarm1)
    #Display.insert(30,currentTime)
#new message box for popup message
   
##    if int(h2) == now.strftime("%H") and int(m2)== now.strftime("%M"):
##        simpledialog.messagebox(title="Alarm", prompt = main_window)
##        
##    



def alarm1():
    mess = Tk()
    mess.geometry("300x200")
  
    dis = Label(mess, text ='Alarm', font = "50") 
    dis.pack()
  
    messagebox.showinfo("Alarm", "Time's up")
    playsound('C:\\Users\\Lavanya\\Music\\1.mp3')
    mess.mainloop()
##

global i
i = 0
global m
m = 0
global h
h = 0

Button( main_window, text = "24 Hrs clock",command = clock_24, width = 20, borderwidth = 5). grid(row = 0, column = 0, columnspan = 1)
Label( main_window, text = "", width = 20, borderwidth = 5). grid(row = 2, column = 0, columnspan = 1)

Button( main_window, text = "12 Hrs clock" ,command = clock_12, width = 20, borderwidth = 5). grid(row = 10, column = 0, columnspan = 1)
Label( main_window, text = "", width = 20, borderwidth = 5). grid(row = 11, column = 0, columnspan = 1)

Button( main_window, text = "stop_watch",command = stop_watch, width = 20, borderwidth = 5). grid(row = 20, column = 0, columnspan = 1)
Label( main_window, text = "", width = 20, borderwidth = 5). grid(row = 21, column = 0, columnspan = 1)

Button( main_window, text = "Set alarm", command = alarm1, width = 20, borderwidth = 5). grid(row = 40, column = 0, columnspan = 1)

main_window.mainloop()
