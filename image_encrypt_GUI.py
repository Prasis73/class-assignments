#for not registered user
from termcolor import colored
def signup():
    name=input(colored("enter your name",'blue'))
    age=input(colored("enter your age", 'blue'))
    while age.isnumeric()==False or int(age)<18 or int(age)>50:
        age=input(colored("invalid age input", 'red'))
    password=input(colored("enter the password for spychat", 'red'))
    while len(password)<8 or len(password)>15:
        password=input(colored("invalid password length", 'red'))
#for registered user
y ='12345'
def login():
    a=input(colored("enter your password", 'blue'))
    while a!=y:
        a=input(colored("enter the valid password",'blue'))
def valid():
    b=input(colored("if you are registered user then write y for yes otherwise write n for no"))
    if b=='n':
        signup()
    elif b=='y':
        login()
    else:
        valid()
valid()
print("WELCOME TO SPYCHAT")


from stegano import lsb
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox as msBox
import datetime
import re
root=Tk()
root.title("Spychat")
root.geometry("700x300")
root.resizable(0,0)
tab=ttk.Notebook(root)
tab1=ttk.Frame(tab)
tab2=ttk.Frame(tab)
'''menubar=Menu(root)
encryption=Menu(menubar)
menubar.add_cascade(label="encryption", menu=encryption)
decryption=Menu(menubar)
menubar.add_cascade(label="decryption", menu=decryption)
root.config(menu=menubar)'''
tab.add(tab1, text="Encoding")
tab.add(tab2, text="Decoding")
tab.pack(expand=1, fill="both")
#encoding
def browse(path):
    filename=filedialog.askopenfilename()
    if re.search('\.jpg$', filename) or re.search('\.png$', filename):
        #path_entry.config(text="path to the file")
        #path_entry.insert(0,filename)
        path.set(filename)

    else:
        msBox.showinfo("you have choosen a wrong file, it is neither jpg nor png")

path=" "
def image(path):
    print(path)
def hide_msg(path,message):
    hide=lsb.hide(path.get(),message.get())
    message_time=datetime.datetime.now().strftime("%y%m%d%H%M%S")
    hide.save('mssg_pic' + message_time + '.jpg')
    msBox.showinfo("saved", "image has been saved with name mssg_pic"+ message_time + '.jpg')
path=StringVar()
but1=Button(tab1, text="Search Image", fg='blue', bg='red',width=20, command=lambda:browse(path))
but1.place(relx=0.25, rely=0.02)

path_entry=Entry(tab1,width=30, borderwidth=2,textvariable=path)
path_entry.place(relx=0.25, rely=0.15)
sms=StringVar()
message=Label(tab1, text="your message here", fg='blue', bg='red', font=(" ", 15))
message.place(relx=0.25, rely=0.30)
msg=StringVar()
msg_entry=Entry(tab1,width=30, borderwidth=2,textvariable=msg)

msg_entry.place(relx=0.25, rely=0.43)
ency=Button(tab1, text="Encode", fg='sky blue', bg='black',command=lambda:hide_msg(path,msg))
ency.place(relx=0.4, rely=0.85)
upload_butn=Button(tab1, text="save", fg='sky blue', bg='black')
upload_butn.place(relx=0.8, rely=0.85)
#for decoding
path2=" "
def browses(path):
    filename=filedialog.askopenfilename()
    if re.search('\.png$',filename) or re.search('\.jpg$', filename):
        path_entry1.config(text="path to the file")
        path_entry1.insert(0,filename)


    else:
        msBox.showinfo("you have choosen a wrong file, it is neither jpg nor png")
def images(path):
    print(path)
def ency(path):
    print(path)
    sms=lsb.reveal(path)
    print(sms)
but2=Button(tab2, text="Search Image", fg="sky blue", bg='red', width=10, command=lambda:browses(path))
but2.place(relx=0.25, rely=0.02)
path_entry1=Entry(tab2, width=30, borderwidth=2)
path_entry1.place(relx=0.25, rely=0.15)
sms1=StringVar()
but3=Button(tab2, text=" View message", fg="sky blue", bg='red', font=(" ", 15))
but3.place(relx=0.25, rely=0.30)
dec=Button(tab2, text="Decode", fg="sky blue", bg="red",command=lambda:images(path))
dec.place(relx=0.4, rely=0.8)

root.mainloop()