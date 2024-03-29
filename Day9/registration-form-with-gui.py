from tkinter import *
from tkinter import messagebox as msgbx
from matplotlib.pyplot import text
import mysql.connector
window = Tk()
window.title("Registration Form")
window.geometry('400x400')
window.config(bg='cadetblue')


def reset():
    firstname.set(" ")
    lastname.set(" ")
    emailid.set(" ")
    contact_no.set(None)


def register():
    conn=mysql.connector.connect(host='127.0.0.1',port='3306',user='root',password='root',database='database')
    mycursor=conn.cursor()
    fname=a1.get()
    lname=b1.get()
    email=c1.get()
    contact=e1.get()
    mycursor.execute("insert into register values(%s,%s,%s,%s)",(fname,lname,email,contact))
    msgbx.showinfo("Registration","Submitted")
    conn.commit()


d= Label(window, text="Registration form",font=("bold", 15),bg='cadetblue').grid(row = 0,column = 0)
a = Label(window ,text = "First Name:",padx=10,pady=10,bg='cadetblue',font=("bold", 15)).grid(row = 1,column = 0)
b = Label(window ,text = "Last Name:",padx=10,pady=10,bg='cadetblue',font=("bold", 15)).grid(row = 2,column = 0)
c = Label(window ,text = "Email Id:",padx=10,pady=10,bg='cadetblue',font=("bold", 15)).grid(row = 3,column = 0)
e = Label(window ,text = "Contact Number:",padx=10,pady=10,bg='cadetblue',font=("bold", 15)).grid(row = 4,column = 0)
btn1  = Button(window ,text="Submit",command=register,width=15, bg= 'green',fg='yellow',pady=10,).grid(row=5,column=0)
btn2= Button(window,text="Reset",width=15, bg= 'green',fg='yellow',pady=10,command=reset).grid(row=5,column=1)



firstname = StringVar()
lastname = StringVar()
emailid= StringVar()
contact_no = IntVar()

a1 = Entry(window,textvariable=firstname)
a1.grid(row = 1,column = 1)
b1 = Entry(window,textvariable=lastname)
b1.grid(row = 2,column = 1)
c1 = Entry(window,textvariable=emailid)
c1.grid(row = 3,column = 1)
e1 = Entry(window,textvariable=contact_no)
e1.grid(row = 4,column = 1)
window.mainloop()


