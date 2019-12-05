#Let's GET GRAPHICAL
from tkinter import *
def click():
    txt.set("Subscribed")
def click1():
    txt.set("liked")
root=Tk()
root.title("Neptech")
root.geometry("700x600")
root.config(background='blue')
root.resizable(1,1)
txt=StringVar()
txt.set("Not subscribed")

#var=Label(root,text="hello").grid(row=0,column=0)
var=Label(root,textvariable=txt)
var.config(font=("",30),background='red',fg='green')
var.pack()
#for button

but=Button(root,text="Subscribe",font=("",20),command=lambda :click())
logo=PhotoImage(file="nep.png")
small_logo=logo.subsample(3,3)
but.config(image=small_logo,compound=LEFT)
but.pack(padx=(10,10),pady=(10,10))
#var=Label(root,text="hello").place(relx=0.5,rely=0.5)
but1=Button(root,text="like",font=("",20),command=lambda : click1())
but.pack(padx=(10,10),pady=(10,10))
but1.pack()
entry=Entry(root,bd=7)
entry.pack()
#var.pack()
root.mainloop()