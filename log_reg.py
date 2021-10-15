# Abdulrazzak Jouhar 2020

from tkinter import *
import time
import os

statue = 'in'
rt1 = Tk()
rt1.title ("login or register")
rt1.geometry('400x200')

def done(action,color):

    rt4 = Tk()
    rt4.title ('title')
    rt4.geometry('400x200')
    qoq = Label(rt4,text = action,fg=color)
    qoq.config(font=("Courier", 40))
    qoq.place(x = 40, y = 80)
    
    rt4.mainloop()


def register_data():

    file = open("log_reg.txt","a")
    name = re_username.get()
    password = re_password.get()
    if name and password:
        file.write(f'\n{name},{password}')
        done('registered','green')

    file.close()
    return
        
def login_data():
    
    success = False
    file = open("log_reg.txt","r")
    name = lo_username.get()
    password =  lo_password.get()
    if name and password:
        for i in file:
            a,b = i.split(',')
            b = b.strip()
            if a == name and b == password:
                success = True
                break

    if success is True:
        done('logged_in','green')
    else:
        done('invalid login','red')    

    file.close()
    return


def logorreg():
    Label(rt1,text = "Login").place(x = 40, y = 60) 
    Label(rt1, text = "Register").place(x = 40, y = 100)

    Button(rt1,text='Click Here',command=login).place(x = 110, y = 60)
    Button(rt1,text='Click Here',command=register).place(x = 110, y = 100)

    rt1.mainloop()

def login():

    rt1.destroy()

    global rt2
    global lo_username
    global lo_password

    rt2 = Tk()
    rt2.title ("Login")
    rt2.geometry('400x200')

    Label(rt2,text = "Username").place(x = 40, y = 60) 
    Label(rt2, text = "Password").place(x = 40, y = 100)

    lo_username = Entry(rt2)
    lo_username.place(x = 110, y = 60)
    lo_password = Entry(rt2)
    lo_password.place(x = 110, y = 100)

    Button(rt2,text ='Submit',command=login_data).place(x = 170, y = 130)

    rt2.mainloop()

def register():

    rt1.destroy()
    
    global rt3
    global re_username
    global re_password

    rt3= Tk()
    rt3.title ("Register")
    rt3.geometry('400x200')

    Label(rt3,text = "Username").place(x = 40, y = 60) 
    Label(rt3, text = "Password").place(x = 40, y = 100)

    re_username = Entry(rt3)
    re_username.place(x = 110, y = 60)
    re_password = Entry(rt3)
    re_password.place(x = 110, y = 100)

    Button(rt3,text ='Submit',command=register_data).place(x = 170, y = 130)

    rt3.mainloop()


logorreg()
