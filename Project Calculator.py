from tkinter import *
from tkinter import messagebox
import math
screen = Tk()
screen.title("Sharan's Calculator")
screen.maxsize(width= 453, height=490)
screen.minsize(width= 453, height=490)
screen.wm_iconbitmap("Logo.ico.ico")

tex = StringVar()
operator = " "

def click(number):
    global operator
    operator += str(number)
    tex.set(operator)

def clear():
    global operator
    operator = " "
    tex.set(operator)
def equal():
    global operator
    try:
        result = eval(tex.get())
        operator = str(result)
        tex.set(result)
    except:
        messagebox.showinfo("Notification","Operand must be selected")
def cmsin():
    global operator
    try:
        result = math.sin(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo("Notification", "Operand must be selected")
def cmcos():
    global operator
    try:
        result = math.cos(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo("Notification", "Operand must be selected")
def cmtan():
    global operator
    try:
        result = math.tan(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo("Notification", "Operand must be selected")
def cmsqrt():
    global operator
    try:
        result = math.sqrt(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo("Notification", "Operand must be selected")
def cmlog():
    global operator
    try:
        result = math.log(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo("Notification", "Operand must be selected")

entry  = Entry(screen,bg="grey",font = ("arial",20),bd=30, justify= "right",textvariable = tex)
entry.grid(row = 0,columnspan = 4)
b7 = Button(text = "7",font = ("arial",20),bd = 8, padx = 16, pady = 16,command = lambda:click(7),activebackground = "grey")
b7.grid(row = 1,column = 0 )
b8 = Button(text = "8",font = ("arial",20),bd = 8, padx = 16, pady = 16,command = lambda:click(8),activebackground = "grey")
b8.grid(row = 1,column = 1)
b9 = Button(text = "9",font = ("arial",20),bd = 8, padx = 16, pady = 16,command = lambda:click(9),activebackground = "grey")
b9.grid(row = 1,column = 2)
bmul = Button(text = "x",font = ("arial",20),bd = 8, padx = 16, pady = 16,command = lambda:click("*"),activebackground = "grey")
bmul.grid(row = 1,column = 3)
b4 = Button(text = "4",font = ("arial",20),bd = 8, padx = 16, pady = 16,command = lambda:click(4),activebackground = "grey")
b4.grid(row = 2,column = 0 )
b5 = Button(text = "5",font = ("arial",20),bd = 8, padx = 16, pady = 16,command = lambda:click(5),activebackground = "grey")
b5.grid(row = 2,column = 1)
b6 = Button(text = "6",font = ("arial",20),bd = 8, padx = 16, pady = 16,command = lambda:click(6),activebackground = "grey")
b6.grid(row = 2,column = 2)
bsub = Button(text = "-",font = ("arial",20),bd = 8, padx = 18, pady = 16,command = lambda:click("-"),activebackground = "grey")
bsub.grid(row = 2,column = 3)
b1 = Button(text = "1",font = ("arial",20),bd = 8, padx = 16, pady = 16,command = lambda:click(1),activebackground = "grey")
b1.grid(row = 3,column = 0 )
b2 = Button(text = "2",font = ("arial",20),bd = 8, padx = 16, pady = 16,command = lambda:click(2),activebackground = "grey")
b2.grid(row = 3,column = 1)
b3 = Button(text = "3",font = ("arial",20),bd = 8, padx = 16, pady = 16,command = lambda:click(3),activebackground = "grey")
b3.grid(row = 3,column = 2)
badd = Button(text = "+",font = ("arial",20),bd = 8, padx = 14, pady = 16,command = lambda:click("+"),activebackground = "grey")
badd.grid(row = 3,column = 3)
bper = Button(text = "/",font = ("arial",20),bd = 8, padx = 18, pady = 16,command = lambda:click("/"),activebackground = "grey")
bper.grid(row = 4,column = 0 )
b0 = Button(text = "0",font = ("arial",20),bd = 8, padx = 16, pady = 16,command = lambda:click(0),activebackground = "grey")
b0.grid(row = 4,column = 1)
bc = Button(text = "c",font = ("arial",20),bd = 8, padx = 16, pady = 16,command = lambda:clear(),activebackground = "grey")
bc.grid(row = 4,column = 2)
beql = Button(text = "=",font = ("arial",20),bd = 8, padx = 14, pady = 16,command = lambda:equal(),activebackground = "grey")
beql.grid(row = 4,column = 3)

bsin = Button(text = "Sin",font = ("arial",15),bd = 8, padx = 14, pady = 22,command = cmsin ,activebackground = "grey")
bsin.grid(row = 0 ,column = 4 )
bcos = Button(text = "Cos",font = ("arial",15),bd = 8, padx = 10, pady = 22,command = cmcos,activebackground = "grey")
bcos.grid(row = 1 ,column = 4 )
btan = Button(text = "Tan",font = ("arial",15),bd = 8, padx = 10, pady = 22,command = cmtan,activebackground = "grey")
btan.grid(row = 2 ,column = 4 )
bsqrt = Button(text = "x²",font = ("arial",15),bd = 8, padx = 18, pady = 22,command = cmsqrt,activebackground = "grey")
bsqrt.grid(row = 3 ,column = 4 )
blog = Button(text = "log",font = ("arial",15),bd = 8, padx = 14, pady = 23,command = cmlog,activebackground = "grey")
blog.grid(row = 4 ,column = 4 )


screen.mainloop()
