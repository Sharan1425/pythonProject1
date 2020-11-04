from tkinter import *
import random
screen = Tk()
screen.title("PingID")
screen.iconbitmap("Pass.ico")
screen.maxsize(width=240,height=250)
screen.minsize(width=240,height=250)
screen.geometry("100x100")
Tex = StringVar()
operator = " "
def Passcode():
    res = random.randrange(100000,500000)
    operator  = Tex.set(res)
lab1 = Label(screen,text = "One-Time Passcode",font = (("arialbold",15)),compound = "top")
lab1.grid(row = 0, column = 0, padx = 0,pady = 5,sticky = "n")
entry = Entry(screen,bg = '#856ff8',bd = 8,width = 15,font = ("arial",15),textvariable = Tex,justify = "center")
entry.grid(row = 1,column = 0,padx = 25,pady = 50,ipady = 4,sticky = "e")

button = Button(text = "New Passcode",font =("arial",10),background = "grey",activebackground = "#856ff8",anchor= "center",command = Passcode)
button.grid(row = 2,column = 0)
screen.mainloop ()